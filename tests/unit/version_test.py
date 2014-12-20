# -*- coding: utf-8 -*-

import unittest

from saltshaker.version import get_version


class TestGetVersion(unittest.TestCase):
    def test_get_the_version(self):
        self.assertIsInstance(get_version(), str)

    def test_version_format(self):
        self.assertRegexpMatches(get_version(), r'(\d+\.){2}(\d+)')
