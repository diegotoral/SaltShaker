# -*- coding: utf-8 -*-

import os

from saltshaker.exceptions import ConfigurationError


def load_config(path):
    if path is None:
        return {}
    if not os.path.isfile(path):
        raise ConfigurationError('Configuration file not found')

    return {}
