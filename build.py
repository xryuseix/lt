import os
import sys
import utils
import subprocess

### その他の関数 ###

# ファイル内部の文字列を置換する
# pattern は [(A, B), (C, D)] とすると A が B に，Cが D に置換される
def replace_content_in_file(path: str, patterns):
    file = utils.read_file(path)
    for pattern in patterns:
        file = file.replace(pattern[0], pattern[1])
    utils.write_file(path, file)


def endswith_array(string: str, keyword: list):
    for key in keyword:
        if string.endswith(key):
            return True
    return False


def main():
    # 準備とか
    assert os.path.exists("dist"), f"[ERROR] dist is not found"

    if len(sys.argv) > 1 and (sys.argv[1] == "--test" or sys.argv[1] == "-t"):
        dist_files = utils.ls("dist")
        for file in dist_files:
            utils.rm(f"dist/{file}")

    lt_folders = [
        folder
        for folder in utils.ls(f"{utils.pwd()}/slides")
        if os.path.isdir(f"{utils.pwd()}/slides/{folder}") and folder[0] != "."
    ]

    # ビルド
    utils.cd("slides")
    for folder in lt_folders:
        utils.cd(f"{folder}")
        _ = subprocess.run(["yarn", "install"])
        _ = subprocess.run(["yarn", "run", "build", "--base", f"/lt/{folder}/"])
        if os.path.exists(f"{utils.pwd()}/{folder}/dist"):
            print(f"[ERROR] build failed! ({folder})")
        utils.cd("..")
    utils.cd("..")

    # ファイルのコピーと HTML 作成
    root_path = utils.pwd()
    utils.cd("dist")
    for folder in lt_folders:
        utils.cp(f"{root_path}/slides/{folder}/dist", f"{utils.pwd()}/{folder}")
        utils.cd(folder)
        # 絶対パスの修正
        # index.html の href, src
        index_replace_patterns = [
            ('href="/', 'href="/lt/'),
            ('src="/', 'src="/lt/'),
            ('href="/lt/lt/', 'href="/lt/'),
            ('src="/lt/lt/', 'src="/lt/'),
        ]
        replace_content_in_file(f"{utils.pwd()}/index.html", index_replace_patterns)
        # assets/vender??????????.js の画像ファイル
        utils.cd("assets")
        image_ext = ["png", "jpg", "gif", "jpeg", "mp4", "mov"]
        patterns = [
            (f'src:"/{image}"', f'src:"/lt/{folder}/{image}"')
            for image in [
                image
                for image in utils.ls(utils.pwd())
                if endswith_array(image, image_ext)
            ]
        ]
        patterns.extend(
            [
                (f'image:"/{image}', f'image:"/lt/{folder}/{image}')
                for image in [
                    image
                    for image in utils.ls(utils.pwd())
                    if endswith_array(image, image_ext)
                ]
            ]
        )
        patterns.extend([('href="/lt/lt/', 'href="/lt/')])
        vendor_file_name = [
            file
            for file in utils.ls(utils.pwd())
            if os.path.isfile(file) and file[0:7] == "vendor." and file[-3:] == ".js"
        ]
        assert len(vendor_file_name) == 1 and os.path.exists(
            vendor_file_name[0]
        ), f"[ERROR] 'vendor_file' is not found"
        replace_content_in_file(f"{utils.pwd()}/{vendor_file_name[0]}", patterns)
        utils.cd("../..")
    utils.cd("..")


if __name__ == "__main__":
    main()
