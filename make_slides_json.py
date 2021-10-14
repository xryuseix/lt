import re
import os
import json
import pathlib
import datetime

import utils


def main():
    lt_folders = [
        folder
        for folder in utils.ls(f"{utils.pwd()}/slides")
        if os.path.isdir(folder)
        and folder[0] != "."
    ]
    slides = []
    for folder in lt_folders:
        # ファイル更新日取得
        path = pathlib.Path(f"./slides/{folder}/slides.md")
        date = datetime.datetime.fromtimestamp(path.stat().st_ctime)
        update_time = date.strftime("%Y/%m/%d %H:%M")

        # ファイルのタイトル取得
        slidesmd = utils.read_file(f"./slides/{folder}/slides.md")
        title = re.search(r"title: ?(.*)(\r\n|\r|\n)?", slidesmd).group(1)
        slides.append(
            {
                "id": folder,
                "title": title,
                "link": f"https://xryuseix.github.io/lt/{folder}",
                "download": f"https://xryuseix.github.io/lt/{folder}/slidev-exported.pdf",
                "update": update_time,
            }
        )
    slides = sorted(
        slides,
        reverse=True,
        key=lambda slide: datetime.datetime.strptime(slide["update"], "%Y/%m/%d %H:%M"),
    )
    utils.write_file("./src/assets/slides.json", json.dumps(slides, indent=2))
    print("[LT] slides.json is updated!")


if __name__ == "__main__":
    main()
