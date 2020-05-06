import sys

from PyQt5 import QtWidgets

from controller.controller import Controller
from model.CPlusDModel import CPlusDModel


def main():
    app = QtWidgets.QApplication(sys.argv)

    model = CPlusDModel()

    controller = Controller(model)

    app.exec_()


if __name__ == '__main__':
    main()
