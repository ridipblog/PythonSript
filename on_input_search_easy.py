import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sqlite3
class on_input_search_easy(QMainWindow):
	def getData(self):
		connection=sqlite3.connect("D:\\python\\Python_projects\\Student_management\\Data\\newregistration.db")
		cursor=connection.cursor()
		readData=connection.execute("select * from newregistration")
		data=readData.fetchall()
		connection.close()
		return data
		return super().eventFilter(source,event)
	def on_input_search(self,text):
		data=self.getData()
		temp=""
		list_1=[]
		for i in range(len(data)):
			temp=""
			tempList=list(data[i][1])
			if(len(tempList)>=len(text)):
				for j in range(len(text)):
					temp+=tempList[j]
				if(text==temp):
					list_1.append(data[i][1])
		self.listbox.clear()
		for i in range(len(list_1)):
			self.listbox.insertItem(i,list_1[i])
	def __init__(self):
		self.name=""
		super().__init__()
		self.setFixedSize(400,400)
		self.input=QLineEdit(self)
		self.input.setGeometry(10,130,100,20)
		self.input_1=QLineEdit(self)
		self.input_1.setGeometry(10,150,100,20)
		self.listbox=QListWidget(self)
		self.listbox.setGeometry(10,10,300,100)
		# self.input.installEventFilter(self)
		self.input.textChanged.connect(self.on_input_search)
		self.show()
App=QApplication(sys.argv)
onINputSearch=on_input_search_easy()
sys.exit(App.exec())