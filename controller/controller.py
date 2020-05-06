from view.CPlusDView import CPlusDView


class Controller:

    def __init__(self, model):
        self.model = model
        self.view = CPlusDView(self,self.model)

        self.view.show()

    def sum(self):
        c = self.view.ui.lineEdit_c.text()
        d = self.view.ui.lineEdit_d.text()

        self.model.set_c(float(c))
        self.model.set_d(float(d))