from PyQt5 import uic
from PyQt6.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QPushButton,QWidget,QSizePolicy,QGraphicsPixmapItem,QLabel
import random
import config
import configparser
from PyQt5 import QtCore, QtWidgets, QtGui
import threading
from threading import Thread



class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.page = uic.loadUi('Lf_or_DthVOL31.ui', self)
        self.pushButton_4.hide()
        self.pushButton_3.hide()
        self.pushButton.clicked.connect(self.Start_Game)
        self.pushButton_2.clicked.connect(self.Check_Anwser)
        self.label_3.hide()
        self.textBrowser.show()
        self.textBrowser_3.show()

        
    
       
    
 #Starts the game
 
    def Start_Game(self):
     self.label_4.setText("")
     config = configparser.RawConfigParser()
     global questioned_event_right_anwser, questioned_event_exp, questioned_event_Why_correct
     question_types = ["avalanche","speeding","Skydiving","Crnt-Underwtr","Polar-Bear","Earthquake","Choking","Tornado","Bulls","Flood","Dog_Horde","Icy_Roads","Elephant_Seal","Meteor","Crowd_Control","German_Shepherd","Shark","Anaconda"]
     config.read('Disasters.ini', encoding="utf8")
     questioned_event = random.choice(question_types)
     questioned_event_dict = dict(config.items(questioned_event.upper()))
     questioned_event_exp = list(questioned_event_dict.items())[0][1]
     questioned_event_opt_A = list(questioned_event_dict.items())[1][1]
     questioned_event_opt_B = list(questioned_event_dict.items())[2][1]
     questioned_event_opt_C = list(questioned_event_dict.items())[3][1]
     questioned_event_Why_correct = list(questioned_event_dict.items())[4][1]
     questioned_event_photo_src = list(questioned_event_dict.items())[5][1]
     questioned_event_right_anwser = list(questioned_event_dict.items())[6][1]
     self.label.show()
     self.Anwser_A.show()
     self.Anwser_B.show()
     self.Anwser_C.show()
     self.label_4.show()
     self.pushButton_2.show()
     self.textBrowser.show()
     self.textBrowser_3.show()
           


     self.stackedWidget.setCurrentWidget(self.page_5)
     self.textBrowser.setText(questioned_event_exp)
     self.Anwser_A.setText(questioned_event_opt_A)
     self.Anwser_B.setText(questioned_event_opt_B)
     self.Anwser_C.setText(questioned_event_opt_C)
     self.label_3.hide()
     self.pushButton_3.hide()
     self.pushButton_4.hide()
     
     self.label.setPixmap(QtGui.QPixmap(questioned_event_photo_src))
     self.label.setScaledContents(True)


    def Go_Home(self):
        self.label_4.setText("")
        self.stackedWidget.setCurrentWidget(self.page_1)

        

     

    def Check_Anwser(self):

        if questioned_event_right_anwser == "Anwser_A" and self.Anwser_A.isChecked() == True:
            self.End_Game("YOU CHOSE OPTION C WHICH IS CORRECT")

        elif questioned_event_right_anwser == "Anwser_B" and self.Anwser_B.isChecked() == True :
            self.End_Game("YOU CHOSE OPTION B WHICH IS CORRECT")
            

        elif questioned_event_right_anwser == "Anwser_C" and self.Anwser_C.isChecked() == True:
            self.End_Game("YOU CHOSE OPTION C WHICH IS CORRECT")
        else:
            self.End_Game("YOU CHOSE WRONG")



    
    def End_Game(self, you_chose):
         self.textBrowser.hide()
         self.label_4.setText(you_chose)
         self.textBrowser_3.setText(questioned_event_Why_correct)
         self.label.hide()
         self.Anwser_A.hide()
         self.Anwser_B.hide()
         self.Anwser_C.hide()
         self.pushButton_2.hide()

         self.label_3.show()
         self.pushButton_3.show()
         self.pushButton_4.show()
         self.pushButton_3.clicked.connect(self.Start_Game)       
         self.pushButton_4.clicked.connect(self.Go_Home)


        
         
        
        


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


