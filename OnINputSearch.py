import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sqlite3
class OnINputSearch(QMainWindow):
	def getData(self):
		connection=sqlite3.connect("D:\\python\\Python_projects\\Student_management\\Data\\newregistration.db")
		cursor=connection.cursor()
		readData=connection.execute("select * from newregistration")
		data=readData.fetchall()
		connection.close()
		return data
	def eventFilter(self,source,event):
		if source==self.input and event.type()==QEvent.Type.KeyPress:
			if(event.key()==Qt.Key.Key_Backspace):
				if(len(self.name)!=0):
					self.list=list(self.name)
					self.list[len(self.name)-1]=""
					self.name=""
					for i in self.list:
						self.name+=i
			else:
				try:
					data=self.getData()
					char="%c" % (event.key())
					self.name=self.name+event.text()
					temp=""
					list_1=[]
					for i in range(len(data)):
						temp=""
						tempList=list(data[i][1])
						if(len(tempList)>=len(self.name)):
							for j in range(len(self.name)):
								temp+=tempList[j]
							if(self.name==temp):
								list_1.append(data[i][1])
					self.listbox.clear()
					for i in range(len(list_1)):
						self.listbox.insertItem(i,list_1[i])
				except:
					pass
		return super().eventFilter(source,event)
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
		self.input.installEventFilter(self)
		self.show()
App=QApplication(sys.argv)
onINputSearch=OnINputSearch()
sys.exit(App.exec())