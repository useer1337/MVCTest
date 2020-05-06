from abc import ABCMeta, abstractmethod


class CPlusDObserver(metaclass=ABCMeta):
    @abstractmethod
    def model_is_changed(self):
        pass