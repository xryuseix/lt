import os
import shutil
import subprocess
from distutils.dir_util import copy_tree

### Linuxコマンド ###


def mv(from_path: str, to_path: str):
    assert os.path.exists(from_path)
    assert os.path.exists(to_path)
    new_path = shutil.move(from_path, to_path)
    return new_path


def mkdir(path: str):
    os.makedirs(path, exist_ok=True)
    assert os.path.exists(path)
    assert os.path.isdir(path)


def ls(path: str):  # -> list:
    return os.listdir(path)


def pwd():
    return os.getcwd()


def cd(path: str):
    crr_path = pwd()
    os.chdir(f"{crr_path}/{path}")
    # assert os.getcwd() == os.path.join(crr_path, path)


def cp(from_path: str, to_path: str):
    assert os.path.exists(from_path)
    if os.path.isdir(from_path):
        copy_tree(from_path, to_path)
        assert os.path.exists(to_path)
        assert os.path.isdir(to_path)
    else:
        shutil.copyfile(from_path, to_path)
        assert os.path.exists(to_path)
        assert os.path.isfile(to_path)


def rm(path: str):
    if os.path.isdir(path):
        shutil.rmtree(path)
        assert not os.path.exists(path)
    else:
        os.remove(path)
        assert not os.path.exists(path)


### ファイルIO ###


def write_file(path: str, content: str):
    with open(path, mode="w") as f:
        f.write(content)
    assert os.path.exists(path)
    assert os.path.isfile(path)


def read_file(path: str):
    with open(path) as f:
        return f.read()


### その他の関数 ###

# ファイル内部の文字列を置換する
# pattern は [(A, B), (C, D)] とすると A が B に，Cが D に置換される
def replace_content_in_file(path: str, patterns):
    file = read_file(path)
    for pattern in patterns:
        file = file.replace(pattern[0], pattern[1])
    write_file(path, file)


def main():
    # 準備とか
    rm("public")
    mkdir("public")
    lt_folders = [
        folder
        for folder in ls(pwd())
        if os.path.isdir(folder) and folder[0] != "." and folder != "public"
    ]

    # ビルド
    for folder in lt_folders:
        cd(folder)
        _ = subprocess.run(["yarn", "install"])
        _ = subprocess.run(["yarn", "run", "build"])
        if os.path.exists(f"{pwd()}/{folder}/dist"):
            print(f"[ERROR] build failed! ({folder})")
        cd("..")

    # ファイルのコピー
    root_path = pwd()
    cd("public")
    for folder in lt_folders:
        cp(f"{root_path}/{folder}/dist", f"{pwd()}/{folder}")
        cd(folder)
        # 絶対パスの修正
        # index.html の href, src
        replace_content_in_file(f"{pwd()}/index.html", [('href="/', 'href="./'), ('src="/', 'src="./')])
        # assets/vender??????????.js の画像ファイル
        patterns = [
            (f'[wr("img",{{src:"/{image}"}})]', f'[wr("img",{{src:"./{folder}/{image}"}})]')
            for image in [
                image for image in ls(pwd()) if image[-3:] in ["png", "jpg", "gif"]
            ]
        ]
        cd("assets")
        vendor_file_name = [
            file
            for file in ls(pwd())
            if os.path.isfile(file) and file[0:7] == "vendor." and file[-3:] == ".js"
        ]
        assert len(vendor_file_name) == 1 and os.path.exists(vendor_file_name[0])
        vendor_file_name = vendor_file_name[0]
        replace_content_in_file(f"{pwd()}/{vendor_file_name}", patterns)
        cd("../..")

    # 最後の仕上げ
    lt_link = [
        f'<li><a href="./{folder}/index.html"> {folder} </a></li>'
        for folder in lt_folders
    ]
    index_html = (
        """
<!DOCTYPE html>
<html lang="en">
<head>
<body>
  <ul>
"""
        + "".join(lt_link)
        + """
    </ul>
</body>
</html>
"""
    )
    write_file("index.html", index_html)


if __name__ == "__main__":
    main()