from Chapter_5.EX_73.ui.MyMainWindow import Ui_MainWindow
from Chapter_5.EX_73.libs.my_module import quadratic_equa

class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.calculation)
    def calculation(self):
        a=float(self.aParameterLineEdit.text())
        b=float(self.bParameterLineEdit.text())
        c=float(self.cParameterLineEdit.text())
        rs=quadratic_equa(a,b,c)
        self.resultLineEdit.setText(str(rs))

    def show_window(self):
        self.MainWindow.show()