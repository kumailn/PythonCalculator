from tkinter import *
from tkinter import ttk

class Number:
    binar = 0
    decima = 0
    def __init__(self, base, numStr):
        if numStr == "":
            numStr = 0
        if base == 2:
            self.binary = numStr
            #self.decimal = decimal(numStr)
            self.BinaryToDecimal()
        else:
            self.decimal = numStr
            #self.binary = binary(numStr)
            self.DecimalToBinary()

    def GetBinary(self):
        return self.binary
    def GetDecimal(self):
        return self.decimal
    def BinaryToDecimal(self):
        a = str(self.binary)
        t = 0
        cc = len(a) - 1
        for i in a:
            t += int(i) * 2 ** cc
            cc = cc - 1
        self.decimal = t
    def DecimalToBinary(self):
        s = ""
        b = int(self.decimal)
        b1 = int(self.decimal)
        while b != 0:
            b = b // 2
            s = s + str(b1%2)
            b1 = b
        self.binary = (s[::-1])
        

class Calculator:
    num1 = ""
    num2 = ""
    num10bj = None
    num20bj = None
    numberSystem = 10
    operation = ""
    isNum1 = True
   

    digitButtons  = []
    operatorButtons = []
    equalsButton = []
    clearButton = []
    binaryButtons = []
    decimalButtons = []
    
    def __init__(self, master):
        mainframe = ttk.Frame(master, relief=SUNKEN, padding="3 3 12 12")
        mainframe.grid(column=0,row=0,columnspan=7,rowspan=6,sticky="NWES")
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        txt = StringVar()
        viewLabel = Label(mainframe,  text="0")
        viewLabel.grid(column=0, row=3)


        plusButton = ttk.Button(mainframe,text="+", command=lambda : self.RecordOperator("+"))
        plusButton.grid(column=6,row=1,pady=5)
        self.operatorButtons.append(plusButton)

        minusButton = ttk.Button(mainframe,text="-", command=lambda : self.RecordOperator("-"))
        minusButton.grid(column=7,row=1,pady=5)
        self.operatorButtons.append(minusButton)

        multButton = ttk.Button(mainframe,text="*", command=lambda : self.RecordOperator("*"))
        multButton.grid(column=6,row=2,pady=5)
        self.operatorButtons.append(multButton)

        divButton = ttk.Button(mainframe,text="/", command=lambda : self.RecordOperator("//"))
        divButton.grid(column=7,row=2,pady=5)
        self.operatorButtons.append(divButton)


        cButton = ttk.Button(mainframe,text="clear", command=lambda : self.ClearAll(viewLabel))
        cButton.grid(column=5,row=1,pady=5)
        self.clearButton.append(cButton)

        eButton = ttk.Button(mainframe,text="=", command=lambda : self.ComputeResult(viewLabel))
        eButton.grid(column=5,row=2,pady=5)
        self.equalsButton.append(eButton)

        
        nineButton = ttk.Button(mainframe,text="9", command=lambda : self.AppendDigit(9, viewLabel))
        nineButton.grid(column=2,row=2,pady=5)
        self.digitButtons.append(nineButton)
        self.decimalButtons.append(nineButton)



        eightButton = ttk.Button(mainframe,text="8", command=lambda : self.AppendDigit(8, viewLabel))
        eightButton.grid(column=1,row=2,pady=5)
        self.decimalButtons.append(eightButton)
        self.digitButtons.append(eightButton)

        sevenButton = ttk.Button(mainframe,text="7", command=lambda : self.AppendDigit(7, viewLabel))
        sevenButton.grid(column=0,row=2,pady=5)
        self.decimalButtons.append(sevenButton)
        self.digitButtons.append(sevenButton)

        sixButton = ttk.Button(mainframe,text="6", command=lambda : self.AppendDigit(6, viewLabel))
        sixButton.grid(column=2,row=1,pady=5)
        self.decimalButtons.append(sixButton)
        self.digitButtons.append(sixButton)

        fiveButton = ttk.Button(mainframe,text="5", command=lambda : self.AppendDigit(5, viewLabel))
        fiveButton.grid(column=1,row=1,pady=5)
        self.decimalButtons.append(fiveButton)
        self.digitButtons.append(fiveButton)

        fourButton = ttk.Button(mainframe,text="4", command=lambda : self.AppendDigit(4, viewLabel))
        fourButton.grid(column=0,row=1,pady=5)
        self.decimalButtons.append(fourButton)
        self.digitButtons.append(fourButton)

        threeButton = ttk.Button(mainframe,text="3", command=lambda : self.AppendDigit(3, viewLabel))
        threeButton.grid(column=2,row=0,pady=5)
        self.decimalButtons.append(threeButton)
        self.digitButtons.append(threeButton)

        twoButton = ttk.Button(mainframe,text="2", command=lambda : self.AppendDigit(2, viewLabel))
        twoButton.grid(column=1,row=0,pady=5)
        self.decimalButtons.append(twoButton)
        self.digitButtons.append(twoButton)

        oneButton = ttk.Button(mainframe,text="1", command=lambda : self.AppendDigit(1, viewLabel))
        oneButton.grid(column=0,row=0,pady=5)
        self.decimalButtons.append(oneButton)
        self.digitButtons.append(oneButton)
        self.binaryButtons.append(oneButton)

        zeroButton = ttk.Button(mainframe,text="0", command=lambda : self.AppendDigit(0, viewLabel))
        zeroButton.grid(column=2,row=2,pady=5)
        self.decimalButtons.append(zeroButton)
        self.digitButtons.append(zeroButton)
        self.binaryButtons.append(zeroButton)

        #Radio buttons
        rb1 = Radiobutton(mainframe, text="Binary",state=NORMAL, value=2, command=self.rd2)
        rb1.grid(row=0, column=6)
        rb2 = Radiobutton(mainframe, text="Decimal", value=1, command=self.rd1)
        rb2.grid(row=0, column=7)


        self.DisableButtons(( self.equalsButton + self.clearButton + self.operatorButtons))
        
    def AppendDigit(self, digit, viewLabel):
        global numSys
        if numSys == 10:
            if(self.isNum1):
                self.num1 = self.num1 + str(digit)
                viewLabel.config(text=self.num1)
                self.EnableButtons(self.operatorButtons + self.clearButton)
            else:
                self.num2 = self.num2 + str(digit)
                
                viewLabel.config(text=self.num2)
                self.EnableButtons(self.equalsButton)
        else:
            if(self.isNum1):
                self.num1 = self.num1 + str(digit)
                viewLabel.config(text=self.num1)
                self.EnableButtons(self.operatorButtons + self.clearButton + self.binaryButtons)
            else:
                self.num2 = self.num2 + str(digit)
                
                viewLabel.config(text=self.num2)
                self.EnableButtons(self.equalsButton)

        return

    def RecordOperator(self, op):
        self.operation = op
        self.num10bj = Number(self.numberSystem, str(self.num1))
        self.isNum1 = False
        self.DisableButtons(self.operatorButtons)
        return

    def ComputeResult(self, viewLabel):
        self.num20bj = Number(self.numberSystem, str(self.num2))
    
        global numSys
        if numSys == 10:
            if(self.operation=="+"):
                r = str(int(self.num1) + int(self.num2))
                q = ""
            elif(self.operation=="-"):
                r = str(int(self.num1) - int(self.num2))
                q = ""
            elif (self.operation == "="):
                r = str(int(self.num1) - int(self.num2))
                q = ""
            elif (self.operation == "*"):
                r = str(int(self.num1) * int(self.num2))
                q = ""
            elif (self.operation=="//"):
                r = str(int(self.num1) // int(self.num2))
                q = "R" + str(int(self.num1) % int(self.num2))
            viewLabel.config(text=(r+q))
        else:
            
            if(self.operation=="+"):
                r = str(int(decimal(self.num1)) + int(decimal(self.num2)))
                q = ""
            elif(self.operation=="-"):
                r = str(int(decimal(self.num1)) - int(decimal(self.num2)))
                q = ""
            elif (self.operation == "="):
                r = str(int(decimal(self.num1)) - int(decimal(self.num2)))
                q = ""
            elif (self.operation == "*"):
                r = str(int(decimal(self.num1)) * int(decimal(self.num2)))
                q = ""
            elif (self.operation=="//"):
                r = str(int(decimal(self.num1)) // int(decimal(self.num2)))
                q = "R" + str(int(decimal(self.num1)) % int(decimal(self.num2)))
            r2 = binary(int(r))
            q2 = binary(int(str(int(decimal(self.num1)) % int(decimal(self.num2)))))
            r1 = Number(10, r)
            q1 = Number(10, str(int(decimal(self.num1)) % int(decimal(self.num2))))
            if (self.operation=="//"):
                viewLabel.config(text=((r1.binary) + " " + "R" + " " + (q1.binary)))
            else:
                viewLabel.config(text=((r1.binary)))

        self.num1 = r
        self.num2 = ""
        self.num10bj = None
        self.num20bj = None
        self.isNum1 = True

        return

    def AssignSystem(self, base, viewLabel):
        #none
        #functionality of this method is integrated in multiple other methods to achieve same output
        a = 1

    def ClearAll(self, viewLabel):
        self.num1 = ""
        self.num2 = ""
        self.operation = ""
        self.num10bj = None
        self.num20bj = None
        isNum1 = True

        viewLabel.config(text="")
        return

    def EnableButtons(self, bList):
        for i in bList:
            i.config(state=NORMAL)
        return
    def DisableButtons(self, bList):
        for i in bList:
            i.config(state=DISABLED)
        return

    def rd1(self):
        a = 0
        global numSys
        numSys = 10
        self.EnableButtons(self.digitButtons)
    
    def rd2(self):
        global numSys
        numSys = 2
        self.DisableButtons(self.decimalButtons)
        self.EnableButtons(self.binaryButtons)
    

def main():
    master = Tk()
    Calculator(master)
    master.title("Calculator")
    master.mainloop()

#main()

def binary(a):
    s = ""
    b = int(a)
    b1 = int(a)
    while b != 0:
        b = b // 2
        s = s + str(b1%2)
        b1 = b
    return (s[::-1])

def decimal(a):
    a = str(a)
    t = 0
    cc = len(a) - 1
    for i in a:
        t += int(i) * 2 ** cc
        cc = cc - 1
    return t

numSys = 10

