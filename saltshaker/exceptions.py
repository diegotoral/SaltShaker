# -*- coding: utf-8 -*-


class ShakerError(Exception):
    """
    Base class for all SaltShaker exceptions
    """
    pass


class ConfigurationError(ShakerError):
    pass
