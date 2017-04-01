# -*- coding: utf-8 -*-
import sys
from os import listdir, makedirs
from os.path import isfile, isdir, join, dirname, splitext
import ntpath
from PIL import Image


class KITTIReader:
    def __init__(self, path):
        self.path = path

    def read_file_content(self):
        file = open(self.path, 'r')
        content = file.read()
        file.close()

        return content

    def get_lines(self, content):
        return content.split('\n')

    def make_crop_item(self, line):
        item = {}

        parts = line.split(' ')

        item["name"] = parts[0]
        item["x_min"] = int(float(parts[4]))
        item["y_min"] = int(float(parts[5]))
        item["x_max"] = int(float(parts[6]))
        item["y_max"] = int(float(parts[7]))

        return item

    def get_items(self):
        content = self.read_file_content()

        items = []
        lines = self.get_lines(content)
        for line in lines:
            item = self.make_crop_item(line)
            items.append(item)

        return items

def make_class_output_folder(current_dir, class_name):
    class_dir_path = join(current_dir, class_name)

    if not isdir(class_dir_path):
        makedirs(class_dir_path)

    return class_dir_path


def get_file_extension(path):
    _, ext = splitext(path)
    return ext


def crop(item, image_path, output_dir, name):
    sourceImg = Image.open(image_path)
    croppedImg = sourceImg.crop((item["x_min"], item["y_min"], item["x_max"], item["y_max"]))

    ext = get_file_extension(image_path)
    croppedImg.save(join(output_dir, name + ext))
    pass


def find_image_file(dir, base_name):
    image_extesion_order = ["jpg", "jpeg", "png"]

    for ext in image_extesion_order:
        path = join(dir, base_name + "." + ext)
        if isfile(path):
            return path
    return None


def process_file(dir, config_file):
    base_name = get_filename_from_path(config_file)

    image_path = find_image_file(dir, base_name)

    if not image_path:
        return 0

    kitti_reader = KITTIReader(config_file)
    items = kitti_reader.get_items()

    idx = 1
    for item in items:
        # crop
        output_dir = make_class_output_folder(dir, item["name"])
        filename = base_name + "-" + str(idx)
        crop(item, image_path, output_dir, filename)

        idx += 1

    return len(items)


def get_filename_from_path(path):
    basepath = ntpath.basename(path)
    return basepath[:-4]


def get_folder_config_files(folder):
    return [join(folder, f) for f in listdir(folder) if isfile(join(folder, f)) and splitext(f)[1].lower() == ".txt"]


def check_argv(argv):
    return len(argv) == 2


def main():
    if not check_argv(sys.argv):
        print "Wrong arguments. You should specify single folder with images and kitti *.txt files"
        exit(1)

    processed_file_count = 0
    path = sys.argv[1]

    config_files = get_folder_config_files(path)

    for file in config_files:
        processed_file_count += process_file(path, file)

    print "Finished. {0} Files are created".format(processed_file_count)

if __name__ == "__main__":
    main()