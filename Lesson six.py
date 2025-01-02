from tkinter import Tk, Button

root = Tk()
root.title('Python Tkinter With Mohammed')
root.config(background='#262626')
root.geometry('450x250')

def a():
    print('hello world')


b = Button(root,
       text='Click',
       bg='Blue',
       command=a,
       activebackground='black',
       activeforeground='whitesmoke',
       border=0)
b.pack()

root.mainloop()