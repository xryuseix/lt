import os
import shutil
from distutils.dir_util import copy_tree

### Linuxコマンド ###


def mv(from_path: str, to_path: str):
    assert os.path.exists(from_path), f"[ERROR] {from_path} is not found"
    assert os.path.exists(to_path), f"[ERROR] {to_path} is not found"
    new_path = shutil.move(from_path, to_path)
    return new_path


def mkdir(path: str):
    os.makedirs(path, exist_ok=True)
    assert os.path.exists(path), f"[ERROR] {path} is not found"
    assert os.path.isdir(path), f"[ERROR] {path} is not dir"


def ls(path: str):  # -> list:
    return os.listdir(path)


def pwd():
    return os.getcwd()


def cd(path: str):
    crr_path = pwd()
    os.chdir(f"{crr_path}/{path}")
    # assert os.getcwd() == os.path.join(crr_path, path)


def cp(from_path: str, to_path: str):
    assert os.path.exists(from_path), f"[ERROR] {from_path} is not found"
    if os.path.isdir(from_path):
        copy_tree(from_path, to_path)
        assert os.path.exists(to_path), f"[ERROR] {to_path} is not found"
        assert os.path.isdir(to_path), f"[ERROR] {to_path} is not dir"
    else:
        shutil.copyfile(from_path, to_path)
        assert os.path.exists(to_path), f"[ERROR] {to_path} is not found"
        assert os.path.isfile(to_path), f"[ERROR] {to_path} is not dir"


def rm(path: str):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
            assert not os.path.exists(path), f"[ERROR] {path} is not found"
        else:
            os.remove(path)
            assert not os.path.exists(path), f"[ERROR] {path} is not found"


### ファイルIO ###


def write_file(path: str, content: str):
    with open(path, mode="w") as f:
        f.write(content)
    assert os.path.exists(path), f"[ERROR] {path} is not found"
    assert os.path.isfile(path), f"[ERROR] {path} is not file"


def read_file(path: str):
    with open(path) as f:
        return f.read()


ng_folder_list = [
    ".github",
    "dist",
    ".dist",
    "public",
    "node_modules",
    "src",
    ".vscode",
    "__pycache__",
]
