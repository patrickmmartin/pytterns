# TODO(PMM) - using __metaclass__ could provide quite an elegant solution

class Registry:
    __registry = {}

    # TODO(PMM) define some operations

    def clear(self):
        self.__registry = {}

    # turns out metaclass is done differently in 2 vs. 3
    def add(self, key, func, args):
        self.__registry[key] = (func, args)

    def get(self, key):
        classdef  = self.__registry.get(key, None)
        if not classdef is None:
            return classdef[0](*classdef[1])
        else:
            return None


#type('X', (object,), dict(a=1))

