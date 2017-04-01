# -*- coding: utf-8 -*-

import unittest
from kitti_cropper import check_argv, get_filename_from_path, get_folder_config_files, find_image_file, process_file, KITTIReader, make_class_output_folder, get_file_extension


class TestUtil(unittest.TestCase):

    def test_check_argv(self):
        self.assertEqual(check_argv(["script"]), False)
        self.assertEqual(check_argv(["script", "."]), True)
        self.assertEqual(check_argv(["script", ".", "./samples"]), False)

    def test_get_filename_from_path(self):
        self.assertEqual( get_filename_from_path("samples\\1.txt"), "1")

    def test_get_folder_config_files(self):
        files = get_folder_config_files("samples")

        self.assertEqual(len(files), 4)
        self.assertEqual( get_filename_from_path(files[0]), "1")

    def test_find_image_file(self):
        self.assertEqual(find_image_file("samples", "1"), "samples\\1.jpg")
        self.assertEqual(find_image_file("samples", "999"), None)

    def test_process_file(self):
        self.assertEqual(process_file("samples", "samples\\1.txt"), 14)
        self.assertEqual(process_file("samples", "samples\\999.txt"), 0)

    def test_make_class_output_folder(self):
        self.assertEqual(make_class_output_folder("samples", "car"), "samples\\car")

    def test_get_file_extension(self):
        self.assertEqual( get_file_extension("samples\\1.jpg"), ".jpg")


class TestKITTIReader(unittest.TestCase):
    def setUp(self):
        self.kitti_reader = KITTIReader("samples\\1.txt")

    def test_read_file_content(self):
        content = self.kitti_reader.read_file_content()

        self.assertNotEqual(content, None)
        self.assertNotEqual(content, "")

    def test_get_lines(self):
        content = self.kitti_reader.read_file_content()

        self.assertEqual(len(self.kitti_reader.get_lines(content)), 14)

    def test_make_crop_item(self):
        item = self.kitti_reader.make_crop_item("car 0.00 0 0.0 54.00 235.00 150.00 321.00 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0")

        self.assertEqual(item["name"], "car")
        self.assertEqual(item["x_min"], 54)
        self.assertEqual(item["y_min"], 235)
        self.assertEqual(item["x_max"], 150)
        self.assertEqual(item["y_max"], 321)

    def test_get_items(self):
        items = self.kitti_reader.get_items()

        self.assertEqual(len(items), 14)


if __name__ == '__main__':
    unittest.main()
