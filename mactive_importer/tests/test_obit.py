# -*- coding utf-8 -*-
import unittest
import os
import shutil

from ..deathnotices.obit import Obit

class TestObit(unittest.TestCase):
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
