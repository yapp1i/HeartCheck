from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
<<<<<<< HEAD


from instr import *
from second_win import *
     
=======
 
 
from instr import *
from second_win import *
 
>>>>>>> 7f482ddf057fcf3804b27b5cc22db0604ae11b54
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
<<<<<<< HEAD


=======
 
 
>>>>>>> 7f482ddf057fcf3804b27b5cc22db0604ae11b54
    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
<<<<<<< HEAD


=======
 
 
>>>>>>> 7f482ddf057fcf3804b27b5cc22db0604ae11b54
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)
<<<<<<< HEAD
    
    def next_click(self):
        self.tw = TestWin()
        self.hide()


    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

=======
 
    def next_click(self):
        self.tw = TestWin()
        self.hide()
 
 
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
 
>>>>>>> 7f482ddf057fcf3804b27b5cc22db0604ae11b54
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
<<<<<<< HEAD


app = QApplication([])
mw = MainWin()
app.exec_()
=======
 
 
app = QApplication([])
mw = MainWin()
app.exec_()
>>>>>>> 7f482ddf057fcf3804b27b5cc22db0604ae11b54
