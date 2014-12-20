# -*- coding: utf-8 -*-

import os
import unittest
from testfixtures import TempDirectory

from saltshaker.config import load_config
from saltshaker.exceptions import ConfigurationError


class TestConfig(unittest.TestCase):
    def test_load_config_for_path_none(self):
        self.assertEqual(load_config(None), {})

    def test_load_config_for_invalid_path(self):
        self.assertRaises(ConfigurationError, load_config, '/some/path')

    def test_load_config_for_valid_path(self):
        with TempDirectory() as d:
            d.write('.shaker.yml', b'')
            path = os.path.join(d.path, '.shaker.yml')
            self.assertEqual(load_config(path), {})
