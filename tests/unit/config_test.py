# -*- encoding: utf-8 -*-

import unittest

from saltshaker.config import load_config


class TestConfig(unittest.TestCase):
    def test_path_none(self):
        self.assertEqual(load_config(None), {})
