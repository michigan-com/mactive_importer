# -*- coding utf-8 -*-
import unittest
import os
import shutil

from deathnotice_importer.obit import Obit
from .lib import src_dir, dest_dir, get_test_images

class TestObit(unittest.TestCase):
    def tearDown(self):
        # clear out images after every test method
        for fname in os.listdir(dest_dir):
            file_path = os.path.join(dest_dir, fname)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def get_default_args(self):
        return {
            'first_name': 'test name',
            'last_name': 'test last name',
            'ad_number': 1234,
            'publication': 'asdf',
            'text': 'sample text sample text sample text',
            'images': [],
            'siicode': 'idk what this is',
        }

    def check_images(self, obit, images):
        """ Do some basic sanity checks for images """
        self.assertEqual(len(obit.images), len(images), 'obit.images length')
        self.assertEqual(obit.image_str, ';'.join(images), 'images_str does not match')

        for img in obit.images:
            self.assertTrue(img in images, 'Img {} not found in args'.format(img))

    def test_simple_init(self):
        args = self.get_default_args()
        obit = Obit(**args)
        args['text'] = args['text'].encode('utf-8') # Obit() encodes the tests
        for key in args:
            self.assertTrue(hasattr(obit, key),
                    'Attribute {} not found in obit'.format(key))
            self.assertEqual(obit.__getattribute__(key), args[key],
                    'obit != args for attribute {}'.format(key))

        self.assertFalse(obit.inserted, 'obit.inserted != False (default)')
        self.assertFalse(obit.updated, 'obit.UPDATED != False (default)')
        self.assertEqual(obit.image_str, '', 'image_str should be empty')

    def test_images(self):
        args = self.get_default_args()
        args['images'] = ['img1.jpg', 'img2.png']
        obit = Obit(**args)
        self.check_images(obit, args['images'])


    def test_successful_copy(self):
        args = self.get_default_args()
        args['images'] = get_test_images()
        obit = Obit(**args)
        self.check_images(obit, args['images'])

        # Copy and verify image copying
        obit.copy_images(src_dir, dest_dir)
        for img in obit.images:
            if not os.path.exists(os.path.join(dest_dir, img)):
                self.fail('image {} didn\'t copy to {}'.format(img, dest_dir))

    def test_copy_images_dont_exist(self):
        args = self.get_default_args()
        args['images'] = ['asdfasdfasdfasdfasdf.jpg', 'asdfasdfasdf.png',
               'thisisatestname.jpg', 'thisisalsoatest.png']
        obit = Obit(**args)
        self.check_images(obit, args['images'])

        obit.copy_images(src_dir, dest_dir)
        self.assertEqual(len(os.listdir(dest_dir)), 0, 'No images should have been copied to ./data/dest_dir')

    def test_copy_images_inavlid_dest_dir(self):
        args = self.get_default_args()
        args['images'] = get_test_images()[:10]
        obit = Obit(**args)
        self.check_images(obit, args['images'])

        obit.copy_images(src_dir, '/this/destination/doesn\'t exist')
        self.assertEqual(len(os.listdir(dest_dir)), 0, 'No images should have been copied to ./data/dest_dir')

    def test_copy_images_invalid_src_dir(self):
        args = self.get_default_args()
        args['images'] = get_test_images()[:10]
        obit = Obit(**args)
        self.check_images(obit, args['images'])

        obit.copy_images('/this/destination/doesn\'t exist', dest_dir)
        self.assertEqual(len(os.listdir(dest_dir)), 0, 'No images should have been copied to ./data/dest_dir')

