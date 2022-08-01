import os
from collections.abc import Iterable


def gen_files_path(to_find_path: str, path_folder: str) -> Iterable[str]:
    path = os.path.abspath(os.path.join(os.path.sep, to_find_path))
    for elem in os.listdir(path):
        file_path = os.path.abspath(os.path.join(path, elem))
        if os.path.isdir(file_path) and elem != path_folder:
            yield from gen_files_path(file_path, path_folder)
        elif os.path.isfile(file_path):
            print(file_path)
        if elem == path_folder:
            return


for item in gen_files_path('SkillBox', ".idea"):
    print(item)
