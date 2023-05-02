import os
from os.path import isfile, isdir, join
import zipfile
from loguru import logger

def get_all_sub_dir(dir: str):
    all_sub_dirs = [root for root, dirs, files in os.walk(dir)]
    return all_sub_dirs

def get_files(dir: str):
    files = os.listdir(dir)
    result = []
    for f in files:
        if isfile(join(dir, f)):
            result.append(join(dir, f))
    return result

def filter_smallfiles(files: list, size_in_byte: int):
    result = []
    for f in files:
        if os.path.basename(f) == "smallfile.zip":
            continue
        if os.path.getsize(f) <= size_in_byte:
            result.append(f)
    return result

def create_zipfile(target_dir: str, write_files: list):
    output_file_name = target_dir + "/smallfile.zip"
    with zipfile.ZipFile(output_file_name, "w", zipfile.ZIP_DEFLATED) as zip:
        for file in write_files:
            arcname = os.path.basename(file)
            zip.write(file, arcname=arcname)