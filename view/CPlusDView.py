from PyQt5.QtWidgets import QMainWindow
from utils.CPlusDObserver import CPlusDObserver
from utils.СplusDMeta import CplusDMeta
from view.form import Ui_MainWindow


class CPlusDView(QMainWindow, CPlusDObserver, metaclass=CplusDMeta):
    def __init__(self, controller, model, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model.add_observer(self)


        self.ui.pushButton_result.clicked.connect(self.controller.sum)

    def model_is_changed(self):
        sum = str(self.model.get_sum())
        self.ui.lineEdit_equels.setText(sum)
