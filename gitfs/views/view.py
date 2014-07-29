import os
from abc import ABCMeta, abstractmethod


class View(object):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        self.args = args

        for attr in kwargs:
            setattr(self, attr, kwargs[attr])

    def _full_path(self, root, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(root, partial)

        return path