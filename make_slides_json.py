import os
import re
import json
import pathlib
import datetime


def pwd():
    return os.getcwd()


def ls(path: str):  # -> list:
    return os.listdir(path)


def write_file(path: str, content: str):
    with open(path, mode="w") as f:
        f.write(content)
    assert os.path.exists(path), f"[ERROR] {path} is not found"
    assert os.path.isfile(path), f"[ERROR] {path} is not file"


def read_file(path: str):
    with open(path) as f:
        return f.read()


def main():
    lt_folders = [
        folder
        for folder in ls(pwd())
        if os.path.isdir(folder)
        and folder[0] != "."
        and folder
        not in [
            ".github",
            "dist",
            ".dist",
            "public",
            "node_modules",
            "src",
            ".vscode",
        ]
    ]
    slides_dict = []
    for folder in lt_folders:
        # ファイル更新日取得
        path = pathlib.Path(f"./{folder}/slides.md")
        date = datetime.datetime.fromtimestamp(path.stat().st_ctime)
        update_time = date.strftime("%Y/%m/%d %H:%M")

        # ファイルのタイトル取得
        slidesmd = read_file(f"./{folder}/slides.md")
        title = re.search(r"title: ?(.*)(\r\n|\r|\n)?", slidesmd).group(1)
        slides_dict.append(
            {
                "id": folder,
                "title": title,
                "link": f"https://xryuseix.github.io/lt/{folder}",
                "download": f"https://xryuseix.github.io/lt/{folder}/download/slidev-exported.pdf",
                "update": update_time,
            }
        )
    write_file("./src/assets/slides.json", json.dumps(slides_dict, indent=2))


if __name__ == "__main__":
    main()
