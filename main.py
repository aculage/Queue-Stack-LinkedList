from tkinter import *
from tkinter import ttk
from linkedlist import *
from cqueue import *
from stack import *

#entry
mainWindow = Tk()
mainWindow.title("Task 1, Navoitsev Denis, IKBO-06-18")
mainWindow.geometry("800x600")
tab = ttk.Notebook(mainWindow)

#task one
tabList = ttk.Frame(tab)
tab.add (tabList, text = "Linear Monodirected List")
tab.pack(expand=1, fill='both')

#input fields
inputFieldL = Entry(tabList, width = 40, font= ("Consolas", 18))
inputFieldL.grid(column =1, row =1)
inputFieldL.focus()

#info fields
labelL = Label(tabList, text='Input int values:', font= ("Consolas", 18))
labelL.grid(column =1, row =0)


#list --init--
loclist = LinkedList()
#input
def listInput():
    try:
        dataIn = inputFieldL.get().split()
        for i in dataIn:
            loclist.Add(i)
        labelL.configure(text ='Succesful input')
    except Exception:
        labelL.configure ('DataType exception occured', 'Check your input')

#output
def listPrint():
    labelL.configure(text = loclist.FormString())

#sumlast
def listSumLast():
    labelL.configure(text = loclist.SumLast())

#clear
def listClear():
    loclist.Clear()
    

#input button
inputButtonL = Button(tabList, text = "Append", font=("Consolas", 18), command = listInput)
inputButtonL.grid(column = 0, row = 2)

#print button
printButtonL = Button(tabList, text = "Print", font=("Consolas", 18), command = listPrint)
printButtonL.grid(column = 0, row = 3)

#sum button
sumButtonL = Button(tabList, text = "Sum", font = ("Consolas", 18), command = listSumLast)
sumButtonL.grid(column = 1, row = 2)

#clear button
clearButtonL = Button(tabList, text = "Clear", font = ("Consolas", 18), command = listClear)
clearButtonL.grid(column = 1, row = 3)




#task two
tabStack = ttk.Frame(tab)
tab.add (tabStack, text = "Stack")
tab.pack (expand=1, fill='both')

#input fields
inputFieldT = Entry(tabStack, width = 40, font= ("Consolas", 18))
inputFieldT.grid(column =1, row =1)
inputFieldT.focus()

#info fields
labelT = Label(tabStack, text='Input int values:', font= ("Consolas", 18))
labelT.grid(column =1, row =0)

#list --init--
locStack = Stack()
#input
def stackInput():
    try:
        dataIn = inputFieldT.get().split()
        for i in dataIn:
            locStack.Push(i)
        labelT.configure(text ='Succesful input')
    except Exception:
        labelT.configure ('DataType exception occured', 'Check your input')

#output
def stackPrint():
    labelT.configure(text = locStack.FormString())

#sumlast
def stackSum():
    labelT.configure(text = locStack.Sum())

#clear
def stackClear():
    locStack.Clear()

#input button
inputButtonS = Button(tabStack, text = "Append", font=("Consolas", 18), command = stackInput )
inputButtonS.grid(column = 0, row = 2)

#print button
printButtomS = Button(tabStack, text = "Print", font=("Consolas", 18), command = stackPrint )
printButtomS.grid(column = 0, row = 3)

#sum button
sumButtonS = Button(tabStack, text = "Sum", font = ("Consolas", 18), command = stackSum )
sumButtonS.grid(column = 1, row = 2)

#clear button
clearButtonS = Button(tabStack, text = "Clear", font = ("Consolas", 18), command = stackClear )
clearButtonS.grid(column = 1, row = 3)




#task three
tabQueue = ttk.Frame(tab)
tab.add (tabQueue, text = "Queue")
tab.pack (expand=1, fill='both')

que = Queue()
#label
labelQ=Label(tabQueue, text ='Press the button',font = ("Consolas", 18))
labelQ.grid(column = 0, row = 0)

def copyQueue ():
    fin = open('text.txt','r')
    arrstr = fin.read().split()
    for i in arrstr :
            que.insert(i)
    txt = ''
    while que.length != 0 :
        txt += que.pop() + ' '
    labelQ.configure(text=txt)

#button
buttonCopy = Button(tabQueue, text = "Copy", font=("Consolas", 18), command = copyQueue)
buttonCopy.grid(column = 0, row = 1)


#finisher loop
mainWindow.mainloop()

 