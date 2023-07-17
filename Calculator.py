from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup
import sys


Ui_MainWindow, QtBaseClass = uic.loadUiType(r"ENTER YOUR FILEPATH HERE")


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.button_group = QButtonGroup()
        
        self.button_group.addButton(self.ui.zerobutton)
        self.button_group.addButton(self.ui.onebutton)
        self.button_group.addButton(self.ui.twobutton)
        self.button_group.addButton(self.ui.threebutton)
        self.button_group.addButton(self.ui.fourbutton)
        self.button_group.addButton(self.ui.fivebutton)
        self.button_group.addButton(self.ui.sixbutton)
        self.button_group.addButton(self.ui.sevenbutton)
        self.button_group.addButton(self.ui.eightbutton)
        self.button_group.addButton(self.ui.ninebutton)

        self.button_group.addButton(self.ui.timesbutton)
        self.button_group.addButton(self.ui.dividebutton)
        self.button_group.addButton(self.ui.minusbutton)
        self.button_group.addButton(self.ui.plusbutton)
        self.button_group.addButton(self.ui.leftbracket)
        self.button_group.addButton(self.ui.rightbracket)
        self.button_group.addButton(self.ui.floatbutton)
        self.button_group.addButton(self.ui.powerbutton)

        self.button_group.buttonClicked.connect(self.type_on_screen)


        self.ui.equalbutton.clicked.connect(self.calculate)

        self.ui.clearbutton.clicked.connect(self.clear)

        self.displaystring = ""
        self.calcstring = ""

    def type_on_screen(self, button):
        value_to_add = button.text()
        
        if value_to_add in ["X", "÷", "-","+"]:
            self.displaystring = self.displaystring + " " + value_to_add + " "
        else:
            self.displaystring += value_to_add

        if value_to_add == "X":
            self.calcstring = self.calcstring + "*"
        elif value_to_add == "÷":
            self.calcstring += "/"
        elif value_to_add == "^":
            self.calcstring += "**"
        else:
            self.calcstring += value_to_add
            
        self.display_on_screen(self.displaystring)

    def display_on_screen(self, display_string):
        self.ui.calcscreen.setText(str(display_string))

    def calculate(self, screenstring):
        
        try:
            result = str(eval(self.calcstring))
        except:
            result = "Please enter a valid calculation"
        
        self.display_on_screen(result)
        self.displaystring = ""
        self.calcstring = ""

    def clear(self):
        self.displaystring = ""
        self.calcstring = ""
        self.display_on_screen(self.displaystring)
        


        
if __name__ == "__main__":
    calculator_app = QApplication(sys.argv)
    calculatorwindow = Calculator()
    calculatorwindow.show()
    calculator_app.exec_()



