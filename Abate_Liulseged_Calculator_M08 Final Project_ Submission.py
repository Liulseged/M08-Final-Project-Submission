#Import everything from tkinter
from tkinter import *
#set and defind messagebox
from tkinter import messagebox
window = Tk()
#set window.title ("Liulseged's Calculator")
window.title("Liulseged's Calculator")
window.geometry('375x574')
#set window.resizable(width=False, height=False)
window.resizable(width=False, height=False)
#window.configure(background="light blue")
window.configure(background="#ffcbb3")

#set Entry window with background color'#ffcbb3',width=52, borderwidth=20
entry = Entry(window,  bg='#ffcbb3',width=52, borderwidth=20)
#set entry.grid(row=0, column=0, columnspan=3, padx=10, pady=3)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=3)



#def button_press(number): functionality 
def button_press(number):
  current = entry.get()
  entry.delete(0, END)
  entry.insert(0, str(current) + str(number))

#def button_clear functionality 
def button_clear():
    entry.delete(0, END)
    
#def button_add functionality 
def button_add():
    first_number = entry.get()
    global fir_num
    global math
    math = "addition"
    fir_num = int(first_number)
    entry.delete(0, END)
    
#def button_equal functionality 
def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
#showing the result on the second Window
    if math == "addition":
        messagebox.showinfo(0, fir_num + int(second_number))
#showing the result on the second Window        
    if math == "subtraction":
        messagebox.showinfo(0, fir_num - int(second_number))

#showing the result on the second Window
    if math == "multiplication":
        messagebox.showinfo(0, fir_num * int(second_number))
#showing the result on the second Window
    if math == "division":
        messagebox.showinfo(0, fir_num / int(second_number))
  
#def button_subtract functionality 
def button_subtract():
    first_number = entry.get()
    global fir_num
    global math
    math = "subtraction"
    fir_num = int(first_number)
    entry.delete(0, END)


#def button_multiply functionality 
def button_multiply():
    first_number = entry.get()
    global fir_num
    global math
    math = "multiplication"
    fir_num = int(first_number)
    entry.delete(0, END)



#def button_divide functionality 
def button_divide():
    first_number = entry.get()
    global fir_num
    global math
    math = "division"
    fir_num = int(first_number)
    entry.delete(0, END)


#Define each buttons     
#Define button 1 and set button 1 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_1 = Button(window, text="1", font=('arial',10, "bold") ,fg='white',borderwidth = 5, bg='#e67300', padx=50, pady=25, command=lambda: button_press(1))
#Define button 2 and set button 2 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_2 = Button(window, text="2",  font=('arial',10, "bold") ,fg='white', borderwidth = 5, bg='#e67300', padx=50, pady=25, command=lambda: button_press(2))
#Define button 3 and set button 3 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_3 = Button(window, text="3", font=('arial',10, "bold") , fg='white', borderwidth = 5, bg='#e67300', padx=50, pady=25, command=lambda: button_press(3))
#Define button 4 and set button 4 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_4 = Button(window, text="4",  font=('arial',10, "bold"),fg='white',borderwidth = 5, bg='#e67300', padx=50, pady=25, command=lambda: button_press(4))
#Define button 5 and set button 5 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_5 = Button(window, text="5", font=('arial',10, "bold"), fg='white', borderwidth = 5,bg='#e67300', padx=50, pady=25, command=lambda: button_press(5))
#Define button 6 and set button 6 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_6 = Button(window, text="6",  font=('arial',10, "bold"),fg='white', borderwidth = 5,bg='#e67300', padx=50, pady=25, command=lambda: button_press(6))
#Define button 7 and set button 7 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_7 = Button(window, text="7", font=('arial',10, "bold"), fg='white',borderwidth = 5, bg='#e67300', padx=50, pady=25, command=lambda: button_press(7))
#Define button 8 and set button 8 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_8 = Button(window, text="8", font=('arial',10, "bold"), fg='white',borderwidth = 5, bg='#e67300', padx=50, pady=25, command=lambda: button_press(8))
#Define button 9 and set button 9 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_9 = Button(window, text="9", font=('arial',10, "bold"), fg='white',borderwidth = 5, bg='#e67300', padx=50, pady=25, command=lambda: button_press(9))
#Define button 0 and set button 0 with font=('arial',10, "bold") ,fg='white',borderwidth = 5, background color ='#e67300', padx=50, pady=25
button_0 = Button(window, text="0",  font=('arial',10, "bold"),fg='white',borderwidth = 5, bg='#e67300', padx=50, pady=25, command=lambda: button_press(0))
#Define button "Clear" with font=('arial',10, "bold"),fg='white',borderwidth = 5, background color ='green', padx=50, pady=25
button_Clear = Button(window, text="C", font=('arial',10, "bold"),fg='white',borderwidth = 5, bg='green', padx=50, pady=25, command=button_clear)
#Define button "Subtract" with font=('time new roman',11,"bold"), fg='white',borderwidth = 5, background=color '#3399ff', padx=50, pady=25
button_subtract = Button(window, text="-",font=('time new roman',11,"bold"), fg='white',borderwidth = 5, bg='#3399ff', padx=50, pady=25, command=button_subtract)
#Define button "add" with font=('arial',10, "bold"),fg='white',borderwidth = 5, background color ='brown', padx=50, pady=25
button_add = Button(window, text="+", font=('arial',10, "bold"),fg='white',borderwidth = 5, bg='brown', padx=50, pady=25, command=button_add)
#Define button "devide" with font=('arial',10, "bold"), fg='white',borderwidth = 5, bg='red', padx=51, pady=25
button_divide = Button(window, text="/",font=('arial',10, "bold"), fg='white',borderwidth = 5, bg='red', padx=51, pady=25, command=button_divide)
#Define button "devide" with font=('arial',10, "bold"), fg='white',borderwidth = 5, bg='red', padx=51, pady=25
button_multiply = Button(window, text="*",font=('arial',10, "bold"),fg='white',borderwidth = 5, bg='#25488e', padx=50, pady=25, command=button_multiply)
#Define button "equal" with fg='white',borderwidth = 10, bg='#b33900', padx=169, pady=27
button_equal = Button(window, text="=", fg='white',borderwidth = 10, bg='#b33900', padx=169, pady=27, command=button_equal)


#creating and display each buttons in the correct row and column
#place button 1 in row 1 and column 0
button_1.grid(row=1, column=0),
#place button 2 in row 1 and column 1
button_2.grid(row=1, column=1),
#place button 3 in row 1 and column 2
button_3.grid(row=1, column=2)
#place button 4 in row 2 and column 0
button_4.grid(row=2, column=0)

#place button 5 in row 2 and column 1
button_5.grid(row=2,column=1),
#place button 6 in row 2 and column 2
button_6.grid(row=2, column=2)
#place button 7 in row 3 and column 0
button_7.grid(row=3, column=0),
#place button 8 in row 3 and column 1
button_8.grid(row=3, column=1),

#place button 9 in row 3 and column 2
button_9.grid(row=3, column=2)
#place button 0 in row 4 and column 2
button_0.grid(row=4, column=2),
#place button "add" in row 4 and column 1
button_add.grid(row=4, column=1),
#place button "substract" in row 5 and column 0
button_subtract.grid(row=5, column=0)

#place button "divide" in row 5 and column 1
button_divide.grid(row=5, column=1)
#place button "multiply" in row 4 and column 0
button_multiply.grid(row=4,column=0)
#place button "clear" in row 5 and column 2
button_Clear.grid(row=5, column=2)
#place button "equal" in row 6 and column 0 columnspan 3
button_equal.grid(row=6, column=0, columnspan=3)

#Display the GUI
window.mainloop()


