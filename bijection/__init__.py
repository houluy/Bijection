class ReadOnly():
    def __set__(self, obj, value):
        raise AttributeError('This attribute is read-only')

class Bijection(dict):
    v2k = ReadOnly()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__['v2k'] = {}

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __getitem__(self, key):
        if key in self.v2k:
            return self.v2k.__getitem__(key)
        else:
            return super().__getitem__(key)

    def __setitem__(self, name, value):
        if value in self.v2k:
            if name not in self:
                raise ValueError('Cannot have multiple same keys or values')
        else:
            self.v2k.__setitem__(value, name)
            super().__setitem__(name, value)
