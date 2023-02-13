from tkinter import *

root = Tk()
expression ="z"
def setexpression(num):
    global expression
    expression = expression + str(num)
    value.set(expression)

def calculator():
    try:
        global expression
        answer =str(eval(expression))
        value.set(answer)
    except:
        value.set("Enter correct expression")
        expression = ""

def AC():
    global expression
    expression = ""
    value.set(expression)
root.geometry("430x495")

large_font =("TimesNewRonam 15")
value =StringVar(value="Enter expression")

Entry(root,textvariable=value,font=large_font).grid(row=0,column=0,columnspan=4,ipadx=70)
Button(root,text="+",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("+")).grid(row=1,column=0)
Button(root,text="-",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("-")).grid(row=2,column=0)
Button(root,text="x",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("*")).grid(row=3,column=0)
Button(root,text="/",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("/")).grid(row=4,column=0)
Button(root,text="1",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("1")).grid(row=1,column=1)
Button(root,text="2",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("2")).grid(row=1,column=2)
Button(root,text="3",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("3")).grid(row=1,column=3)
Button(root,text="4",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("4")).grid(row=2,column=1)
Button(root,text="5",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("5")).grid(row=2,column=2)
Button(root,text="6",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("6")).grid(row=2,column=3)
Button(root,text="7",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("7")).grid(row=3,column=1)
Button(root,text="8",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("8")).grid(row=3,column=2)
Button(root,text="9",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("9")).grid(row=3,column=3)
Button(root,text="0",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression("0")).grid(row=4,column=2)
Button(root,text=".",fg="Black",bg="silver",height=4,width=8, command=lambda :setexpression(".")).grid(row=4,column=1)
Button(root,text="=",fg="White",bg="orange",height=4,width=8, command=calculator).grid(row=4,column=3)
Button(root,text="AC",fg="Black",bg="orange",height=4,width=8, command=AC).grid(row=5,column=2)
root.mainloop()