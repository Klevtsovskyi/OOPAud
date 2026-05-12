import abc


class AbstractClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def abstract_method(self):
        pass


class CurrentClass(AbstractClass):

    def abstract_method(self):
        pass


if __name__ == '__main__':
    obj = CurrentClass()

