# letters=['a','b','d','e','i','j','o']
# def filter_vowels(letters):
#     vowels=['a','e','i','o','u']
#     return True if letters in vowels else False
# filtered_vowels=filter(filter_vowels,letters)
# vowels=tuple(filtered_vowels)
# print(vowels)


# numbers=[1,2,3,4,5,6,7]
# even_numbers=filter(lambda x:(x%2==0),numbers)
# even=list(even_numbers)
# print(even)


# from tkinter import*
# from tkinter import messagebox
# top=Tk()
# top.geometry("200x100")

# def fun():
#     messagebox.showinfo("hello","red button clicked")

# b1=Button(top,text="red",command=fun,activeforeground="red",activebackground="pink",pady=10)
# b2=Button(top,text="blue",activeforeground="blue",activebackground="pink",pady=10)
# b3=Button(top,text="green",activeforeground="green",activebackground="pink",pady=10)
# b4=Button(top,text="yellow",activeforeground="yellow",activebackground="pink",pady=10)

# b1.pack(side=LEFT)
# b2.pack(side=RIGHT)
# b3.pack(side=TOP)
# b4.pack(side=BOTTOM)
# top.mainloop()


# from tkinter import*
# pane=Tk()
# b1=Button(pane,text="click me")
# b1.pack(fill=Y,expand=True)
# b2=Button(pane,text="click me too")
# b2.pack(fill=X,expand=True)
# pane.mainloop()




# from tkinter import*
# m=Tk()
# m.geometry("500x500")
# b1=Button(m,text="submit")
# b1.place(anchor=NE,relx=1,x=-2,y=2)
# b2=Button(m,text="new")
# b2.place(anchor=CENTER,relx=0.5,rely=0.5)
# m.mainloop()





# from cProfile import label
# from cgitb import text
# from tkinter import*
# w=Tk()
# w.geometry("300x300")
# l1=Label(text="first")
# l2=Label(text="second")
# l3=Label(text="Third")
# l4=Label(text="Fourth")
# l1.grid(row=0,column=0,padx=50)
# l2.grid(row=0,column=1,padx=50)
# l3.grid(row=1,column=0)
# l4.grid(row=1,column=1)
# w.mainloop()


from tkinter import*
import tkinter
root=Tk()
logo=tkinter.PhotoImage(file="ME.png")
w1=Label(root,image=logo).pack(side="right")
msg="welcome to riddhi's world"
w2=Label(root,justify=tkinter.LEFT,padx=10,text=msg).pack(side="left")
root.mainloop()