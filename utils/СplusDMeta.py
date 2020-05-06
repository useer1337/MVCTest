from PyQt5 import QtCore
from abc import ABCMeta

pyqtWrapperType = type(QtCore.QObject)


class CplusDMeta(pyqtWrapperType, ABCMeta):
    pass