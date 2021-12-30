from tkinter import *
root=Tk()
class Test:
	def timer(self):
		self.count=0
		self.start=True
		def run1():
			if(self.start):
				if(self.count<10):
					self.count=self.count+1
					self.para.config(text=self.count)
					self.master.after(1000,run1)
				else:
					self.count=False
					self.start=0
		run1()
	def btnfun1(self):
		if(self.paratext2.get()=="Number"):
			self.paratext2.set("String")
		else:
			self.paratext2.set("Number")

	def btnfun2(self):
		if(self.btntext2.get()=="Start"):
			self.btntext2.set("Stop")
			self.timer()
		else:
			self.start=False
			self.btntext2.set("Start")
	def __init__(self,master):
		self.master=master
		self.master.resizable(False,False)
		self.master.geometry("600x550+100+20")
		self.div=Frame(self.master,width=580,height=530,bd=5,relief="groove",bg="#0c2c33")
		self.div.place(x=0,y=0)
		self.count=0
		self.start=True
		self.btn=Button(self.div,text="Click",width=20)
		self.btn.place(x=20,y=20)
		self.btn.config(command=self.btnfun1)
		self.para=Label(self.div,text="Timer")
		self.para.place(x=10,y=100)
		self.paratext2=StringVar()
		self.para2=Label(self.div,textvariable=self.paratext2)
		self.para2.place(x=20,y=130)
		self.paratext2.set("Number")
		self.btntext2=StringVar()
		self.btn2=Button(self.div,width=20,textvariable=self.btntext2)
		self.btn2.place(x=20,y=170)
		self.btn2.config(command=self.btnfun2)
		self.btntext2.set("Start")
test=Test(root)
root.mainloop()