#--------------------------------------------------IMPORT--------------------------------------------------#
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QRegExp,Qt
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlRecord, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets
from pathlib import Path
import sys
import os
from psycopg2 import Error


class QuestWindow(QWidget):
    def __init__(self):
        super(QuestWindow, self).__init__()
        uic.loadUi('ui/Quest.ui', self)
        self.pushButton.clicked.connect(self.click)
    def click(self):
        quest.hide()

        
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/Filter.ui', self)
        self.pushButton_4.clicked.connect(self.getDirectory)
        self.pushButton.clicked.connect(self.filter)
        self.pushButton_2.clicked.connect(self.click)
        self.pushButton_3.clicked.connect(self.exit)
        
    def click(self):
        quest.show()
    def exit(self):
        sys.exit(app.exec_())
    def getDirectory(self):
        dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
        self.lineEdit_2.setText(str(dirlist))
    def filter(self):
        try: 
            a=self.lineEdit.text()
            b=os.listdir(path=self.lineEdit_2.text())
            f2 = open('log/text.txt', 'w')
            f2.write(self.lineEdit_2.text() +":\n")
            for i in b:
                f2.write("Проверка Файла:" +i+"\n")
                if (Path(i).suffix=='.txt'):
                    d=0
                    e=str(i)
                    if e.find(a) != -1 :
                        f2.write("В названии файла "+i+" найдена фраза\n")
                        d=1
                      
                    f = open(i, 'r')
                    if (f.read().find(a) != -1) :
                            f2.write("В содержимом файла файла "+i+" найдена фраза\n")
                            d=1
                    if (d==1):
                        f.close()
                        path = os.path.join(self.lineEdit_2.text(), i)
                        os.remove(path)
                        f2.write("Удаление файла: "+i+"\n")
                    else:
                        f2.write("Фразы не найдено\n")
                        f.close()
            f2.close()
            os.startfile('log\\text.txt')           
        except (Exception, Error) as error:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не удаётся найти указанный путь')
            msg.setWindowTitle("Error")
            msg.exec_()
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quest=QuestWindow()
    main=MainWindow()
    main.show()
    sys.exit(app.exec_())
