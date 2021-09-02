import re
import os
import json
import pathlib
import datetime

import utils


def main():
    lt_folders = [
        folder
        for folder in utils.ls(utils.pwd())
        if os.path.isdir(folder)
        and folder[0] != "."
        and folder not in utils.ng_folder_list
    ]
    slides_dict = []
    for folder in lt_folders:
        # ファイル更新日取得
        path = pathlib.Path(f"./{folder}/slides.md")
        date = datetime.datetime.fromtimestamp(path.stat().st_ctime)
        update_time = date.strftime("%Y/%m/%d %H:%M")

        # ファイルのタイトル取得
        slidesmd = utils.read_file(f"./{folder}/slides.md")
        title = re.search(r"title: ?(.*)(\r\n|\r|\n)?", slidesmd).group(1)
        slides_dict.append(
            {
                "id": folder,
                "title": title,
                "link": f"https://xryuseix.github.io/lt/{folder}",
                "download": f"https://xryuseix.github.io/lt/{folder}/slidev-exported.pdf",
                "update": update_time,
            }
        )
    utils.write_file("./src/assets/slides.json", json.dumps(slides_dict, indent=2))
    print("[LT] slides.json is updated!")


if __name__ == "__main__":
    main()
