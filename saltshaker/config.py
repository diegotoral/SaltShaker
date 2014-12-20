# -*- coding: utf-8 -*-

import os
import yaml

from saltshaker.exceptions import ConfigurationError


def load_config(path):
    if path is None:
        return {}

    if not os.path.isfile(path):
        raise ConfigurationError('Configuration file not found')

    return yaml.load(open(path, 'r'))
