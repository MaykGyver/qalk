from PySide6 import QtCore, QtWidgets
import sys

class Qalk(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle('Qalk')
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    _ = Qalk()
    app.exec()
if __name__=='__main__': main()
