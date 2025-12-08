# A GUI using the PyQt5 package 
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel
from PyQt5.QtGui import QIcon , QFont 
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Graphic User Interface")
        self.setGeometry(700 , 400 , 500 , 500)
        self.setWindowIcon(QIcon("pfp.jpg"))

        label = QLabel("Hello there", self)
        label.setFont(QFont("Arial" ,12))
        label.setGeometry(0,0, 500, 100)
        label.setStyleSheet("color: white;"
                            "background-color:Black;"
                            "Text-decoration: underline;")
       
       # label.setAlignment(Qt.AlignTop) # Vertically top
       # label.setAlignment(Qt.AlignBottom) #Vertically bottom
       # label.setAlignment(Qt.AlignVCenter) #Vertically center

       # label.setAlignment(Qt.AlignRight) #Horizontally right
       # label.setAlignment(Qt.AlignHCenter) # Horizontally center

       # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center & Top
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & bottom
        label.setAlignment(Qt.AlignCenter) # Center & Center


    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()