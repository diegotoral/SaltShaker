# -*- coding: utf-8 -*-

import os
import unittest
from testfixtures import TempDirectory

from saltshaker.config import load_config
from saltshaker.exceptions import ConfigurationError


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = TempDirectory()

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_load_config_for_path_none(self):
        self.assertEqual(load_config(None), {})

    def test_load_config_for_invalid_path(self):
        self.assertRaises(ConfigurationError, load_config, '/some/path')

    def test_load_config_for_valid_path(self):
        path = self._write_config_file('.shaker.yml', '')
        self.assertEqual(load_config(path), None)

    def test_load_config_with_sources(self):
        path = self._write_config_file('.shaker.yml', b'sources:')
        self.assertEqual(load_config(path), { 'sources': None })

    def _write_config_file(self, filename, filecontent):
        self.tmp_dir.write(filename, filecontent)
        return os.path.join(self.tmp_dir.path, filename)
