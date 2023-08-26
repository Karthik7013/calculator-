from tkinter import *
from PIL import Image,ImageTk

class Cal:

	def pro(self):
		pro = Frame(root,bg = 'black')
		pro.place(x = 0,y = 0)


	def reset(self):
		self.b.config(state = 'normal')
		self.b.delete(0,END)
		self.value = ''
		self.result = '0'
		self.b.insert(END,'0')

	def clear(self):
		self.b.delete(len(self.b.get())-1,'end')
		self.value = self.b.get()

	def btn_clk(self,num):
		self.value += num
		self.b.delete(0,END)
		self.b.insert('0',self.value)

	def eql(self):

  		try:
  			if self.b.get() == 0.0:
  				self.b.insert(END,0)
  			else:
	  			self.result = eval(self.b.get())
	  			if self.result == 0.0:
	  				self.b.delete(0,END)
	  				self.b.insert('0','0')
	  				self.value = str(f'{self.result:.2f}')
	  				self.value = str('{0:.2f}'.format(self.result))
	  			else:
	  				self.b.delete(0,END)
	  				self.b.insert(END,round(self.result,2))
	  				self.value = str(self.result)
  		except Exception as e:
  			self.b.delete(0,END)
  			self.b.insert('0','ERROR !\t      ')
  			self.b.config(state = 'disabled')

	def __init__(self,root):
		self.root = root
		self.root.title('Calculator')
		self.root.iconbitmap(r'calculator.ico')
		self.root.wm_geometry('318x495')
		self.root.config(bg = 'snow')
		self.root.wm_maxsize(318,495)
		self.root.wm_minsize(318,495)
		self.result = '0'
		self.value = ''

# Entry box ----------------------------------

		self.b = Entry(root,font = ('rockwell',25,''), justify = 'right', width = 15,bd = 0, bg = 'snow')
		self.b.grid(row = 0,column = 0,columnspan = 4, padx = 10,pady = 20, ipady = 10, ipadx = 10)
		self.b.insert('0',self.result)
		self.b.focus()

# images loding ..........

		self.img0 = ImageTk.PhotoImage(Image.open("0.png"))
		self.img1 = ImageTk.PhotoImage(Image.open("1.png"))
		self.img2 = ImageTk.PhotoImage(Image.open("2.png"))
		self.img3 = ImageTk.PhotoImage(Image.open("3.png"))
		self.img4 = ImageTk.PhotoImage(Image.open("4.png"))
		self.img5 = ImageTk.PhotoImage(Image.open("5.png"))
		self.img6 = ImageTk.PhotoImage(Image.open("6.png"))
		self.img7 = ImageTk.PhotoImage(Image.open("7.png"))
		self.img8 = ImageTk.PhotoImage(Image.open("8.png"))
		self.img9 = ImageTk.PhotoImage(Image.open("9.png"))
		self.mul = ImageTk.PhotoImage(Image.open("mul.png"))
		self.min = ImageTk.PhotoImage(Image.open("min.png"))
		self.plus = ImageTk.PhotoImage(Image.open("plus.png"))
		self.div = ImageTk.PhotoImage(Image.open("div.png"))
		self.eq = ImageTk.PhotoImage(Image.open("eql.png"))
		self.dec = ImageTk.PhotoImage(Image.open("dec.png"))
		self.cls = ImageTk.PhotoImage(Image.open("cls.png"))
		self.bs = ImageTk.PhotoImage(Image.open("backspace.png"))
		self.swi = ImageTk.PhotoImage(Image.open("alter.png"))

# create buttons ----------------------

		self.clr_b = Button(self.root, image = self.cls,command = self.reset, bd = 0,activebackground = 'white')
		self.sq_b = Button(self.root,image = self.bs,command = self.clear, bd = 0,activebackground = 'white')
		self.mul_b = Button(self.root, image = self.mul,command = lambda: self.btn_clk('*'),bg = 'white', bd = 0,activebackground = 'white')
		self.div_b = Button(self.root, image = self.div, command = lambda: self.btn_clk('/'),bg = 'white', bd = 0,activebackground = 'white')

		self.b7 = Button(self.root, text = '7', image = self.img7,command = lambda: self.btn_clk('7'),bg = 'white', bd = 0,activebackground = 'white')
		self.b8 = Button(self.root, text = '8', image = self.img8,command = lambda: self.btn_clk('8'),bg = 'white', bd = 0,activebackground = 'white')
		self.b9 = Button(self.root, text = '9', image = self.img9,command = lambda: self.btn_clk('9'),bg = 'white', bd = 0,activebackground = 'white')
		self.sub_b = Button(self.root, image = self.min, command = lambda: self.btn_clk('-'),bg = 'white', bd = 0,activebackground = 'white')

		self.b4 = Button(self.root, text = '4', image = self.img4,command = lambda: self.btn_clk('4'),bg = 'white', bd = 0,activebackground = 'white')
		self.b5 = Button(self.root, text = '5', image = self.img5,command = lambda: self.btn_clk('5'),bg = 'white', bd = 0,activebackground = 'white')
		self.b6 = Button(self.root, text = '6', image = self.img6,command = lambda: self.btn_clk('6'),bg = 'white', bd = 0,activebackground = 'white')
		self.plus_b = Button(self.root,image = self.plus, command = lambda: self.btn_clk('+'),bg = 'white', bd = 0,activebackground = 'white')
		
		self.b1 = Button(self.root, text = '1', image = self.img1,command = lambda: self.btn_clk('1'),bg = 'white', bd = 0,activebackground = 'white')
		self.b2 = Button(self.root, text = '2', image = self.img2,command = lambda: self.btn_clk('2'),bg = 'white', bd = 0,activebackground = 'white')
		self.b3 = Button(self.root, text = '3', image = self.img3,command = lambda: self.btn_clk('3'),bg = 'white', bd = 0,activebackground = 'white')
		self.eq_b = Button(self.root, text = '=',image = self.eq, command = self.eql,bg = '#2196F3', bd = 0,activebackground = 'white', height = 140)

		self.switch = Button(self.root,text = 'switch',image = self.swi,command = self.pro,bg = 'snow',bd = 0,activebackground = 'white')
		self.b0 = Button(self.root, text = '0', image = self.img0,command = lambda: self.btn_clk('0'),bg = 'white', bd = 0,activebackground = 'white')
		self.dec_b = Button(self.root, text = '.',image = self.dec, command = lambda: self.btn_clk('.'),bg = 'white', bd = 0,activebackground = 'white')

# showing buttons -------------------------------------

		self.clr_b.grid(row = 2, column = 0, pady = (13,5), padx = (13,5))
		self.sq_b.grid(row = 2, column = 1,pady = (13,5),padx = 5)
		self.mul_b.grid(row = 2,column = 2,pady = (13,5), padx = 5)
		self.div_b.grid(row = 2,column = 3,pady = (13,5),padx = (5,10))

		self.b7.grid(row = 3, column = 0,padx = (10,5),pady = 5)
		self.b8.grid(row = 3, column = 1,padx = 5,pady = 5)
		self.b9.grid(row = 3, column = 2,padx = 5,pady = 5)
		self.sub_b.grid(row = 3, column = 3,padx = 5,pady = 5)

		self.b4.grid(row = 4, column = 0,padx = (10,5),pady = 5)
		self.b5.grid(row = 4, column = 1,padx = 5,pady = 5)
		self.b6.grid(row = 4, column = 2,padx = 5,pady = 5)
		self.plus_b.grid(row = 4, column = 3,padx = 5,pady = 5)

		self.b1.grid(row = 5, column = 0,pady = (5,10),padx = (10,5))
		self.b2.grid(row = 5, column = 1,pady =5,padx = 5)
		self.b3.grid(row = 5, column = 2,pady = 5,padx = 5)
		self.eq_b.grid(row = 5,column = 3,rowspan = 5,padx = (5,10))

		self.b0.grid(row = 6, column = 1,pady = 5,padx = 5)
		self.dec_b.grid(row = 6, column = 2,pady = 5,padx = 5)
		self.switch.grid(row = 6,column = 0,pady = 5,padx = (10,5))

		self.root.mainloop()# ---------   mainloop   ------------- 

if __name__ == '__main__':
	root = Tk()
	startApp = Cal(root)