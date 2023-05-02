import os
from os.path import isfile, isdir, join
import zipfile
from loguru import logger

# target_dir = "H:\\testing\\sub2"
target_dir = "/Users/williamleung/Documents/play_myself/testing"
small_file_size = 50 * 1024 * 1024
mypath = target_dir


def get_all_dir(path):
    my_dirs = [root for root, dirs, files in os.walk(target_dir)]
    return my_dirs


def get_file(dir):
    files = os.listdir(dir)
    result = []
    for f in files:
        if isfile(join(dir, f)): 
            result.append(join(dir, f))
    return result


def filter_size(files: list, size_in_byte: int):
    result = []
    for f in files:
        if os.path.basename(f) == "smallfile.zip":
            continue
        if os.path.getsize(f) <= size_in_byte:
            result.append(f)
    return result


def zip_files(dir: str, files: list):
    output_file_name = dir + "/smallfile.zip"
    with zipfile.ZipFile(output_file_name, "w", zipfile.ZIP_DEFLATED) as zip:
        for file in files:
            arcname = os.path.basename(file)
            zip.write(file, arcname=arcname)


def main():
    # my_dirs = get_all_dir(target_dir)
    # target_dirs = get_file("H:\\testing\\sub2")
    # result = filter_size(target_dirs, 1024 * 1024)
    # print(result)
    # zip_files("H:\\testing\\sub2", files=result)

    all_dirs = get_all_dir(target_dir)
    for dir in all_dirs:
        all_files = get_file(dir)
        small_files = filter_size(all_files, small_file_size)
        logger.info(small_files)
        zip_files(dir, files=small_files)


if __name__ == "__main__":
    main()
