from numpy import *
from tkinter import *
import matplotlib.pyplot as plt
from mathematicalfunc import *
superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
    "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
    "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
    "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
    "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
    "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
    "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
    "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}

trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))
subscript_map = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
    "7": "₇", "8": "₈", "9": "₉", "a": "ₐ", "b": "♭", "c": "꜀", "d": "ᑯ",
    "e": "ₑ", "f": "բ", "g": "₉", "h": "ₕ", "i": "ᵢ", "j": "ⱼ", "k": "ₖ",
    "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "ₒ", "p": "ₚ", "q": "૧", "r": "ᵣ",
    "s": "ₛ", "t": "ₜ", "u": "ᵤ", "v": "ᵥ", "w": "w", "x": "ₓ", "y": "ᵧ",
    "z": "₂", "A": "ₐ", "B": "₈", "C": "C", "D": "D", "E": "ₑ", "F": "բ",
    "G": "G", "H": "ₕ", "I": "ᵢ", "J": "ⱼ", "K": "ₖ", "L": "ₗ", "M": "ₘ",
    "N": "ₙ", "O": "ₒ", "P": "ₚ", "Q": "Q", "R": "ᵣ", "S": "ₛ", "T": "ₜ",
    "U": "ᵤ", "V": "ᵥ", "W": "w", "X": "ₓ", "Y": "ᵧ", "Z": "Z", "+": "₊",
    "-": "₋", "=": "₌", "(": "₍", ")": "₎"}


sub_trans = str.maketrans(
    ''.join(subscript_map.keys()),
    ''.join(subscript_map.values()))


#functions
class Graphing():
    def __init__(self):
        self.txtdisplayno=0
        self.strequationlist=list()
        self.equation=[[]]
        self.equationlist=list()
        self.mathfunc=0
        self.position=0
        self.upper=4*pi
        self.lower=-4*pi
        self.lrange=-10
        self.urange=10
        self.process=True
        self.turn=0
        self.present=0
        self.superscript=False
        self.k=False
        self.brack=False
        self.brackin=1
        self.brackout=0
    def test(self,t):
        self.present=t
    def collector(self,L):
        value=''
        for i in L:
            value+=i
        return value
    def decollector(self,s):
        nishant=[]
        for i in s:
            nishant.append(i)
        return nishant
    def backnForth(self,forward=None,backward=None):
        if forward==1:
            if len(self.equation[self.present])>self.position:
                self.position+=1
        if backward==1:
            if self.position>0:
                self.position-=1
    """ superscripts s=02E2,x=02E3a=0363,e=0364,i=0365,o=0366
    """
    def brackcount(self,elemnet):
        for i in elemnet:
            if i=='(':
                self.brackin+=1

            if i==')':
                self.brackout+=1
        if self.brackin==self.brackout:
            return True
        else:
            return False
    def clear(self):
        try:
            a = self.equation[self.present].pop()
            if a=='**2':
                a='\u00B2'
            if a=='**(':
                a='^('
            if a=='sqrt(':
                a='\u221A('
            t=f'end-{len(a)+1}c'
            txtDisplay[self.present].configure(state='normal')
            txtDisplay[self.present].delete(t,END)
            txtDisplay[self.present].configure(state=DISABLED)
        except:
            pass
    def numberEnter(self,element):

        self.equation[self.present].insert(self.position,element)
        self.position+=1
        global txtDisplay
        if element=='**2':
            element='\u00B2'
        elif element=='pi':
            element='\u03C0'
        elif element=='**(':
            element='^('
        elif element=='sqrt(':
            element='\u221A('
        txtDisplay[self.present].config(state=NORMAL)
        txtDisplay[self.present].insert(END,element)
        txtDisplay[self.present].config(state=DISABLED)
    def funcEnter(self,element):
        self.mathfunc.destroy()
        self.numberEnter(element)
    def functions(self):
        self.mathfunc=Tk()
        self.mathfunc.title('Mathematical Functions')
        self.mathfunc.geometry('330x470')
        self.mathfunc.resizable(False,False)
        mainFrame=Frame(self.mathfunc)
        mainFrame.pack(fill='both',expand=1)
        myCanvas=Canvas(mainFrame)
        myCanvas.pack(side=LEFT,fill='both',expand=1)
        scrolllabel = Scrollbar(myCanvas,orient='vertical',command=myCanvas.yview)
        scrolllabel.pack(side=RIGHT,fill='y')
        myCanvas.configure(yscrollcommand=scrolllabel.set)
        myCanvas.bind('<Configure>',lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))
        mfunc=Frame(myCanvas)
        myCanvas.create_window((0,0),window=mfunc, anchor='nw')
        trigLabel=Label(mfunc,text='Trignometric Function',font=('times', 20,'bold'))
        trigLabel.place(x=0,y=0)

        triglist=['sin(','cos(','tan(','csc(','sec(','cot(']
        trigButton=[]
        for i in range(6):
            trigButton.append(Button(mfunc,
                          width=6,
                          height=2,
                          bg='white',
                          fg='black',
                          font=('times', 15, 'bold'),
                          bd=4, text=triglist[i][:-1]))
            trigButton[i]["command"] = lambda x=triglist[i]: self.funcEnter((x))
            l=50
            if i>=3:
                l=10
            trigButton[i].grid(row=int(i//(3)+1),column=i%3,padx=7,pady=(l,10))
        inversetrigLabel=Label(mfunc,text='Inverse Trig Function',font=('times', 20,'bold'))
        inversetrigLabel.place(x=0,y=230)
        invtriglist=['arcsin(','arccos(','arctan(','arccsc(','arcsec(','arccot(']
        invtrigButton=[]
        for i in range(6):
            invtrigButton.append(Button(mfunc,
                          width=6,
                          height=2,
                          bg='white',
                          fg='black',
                          font=('times', 15, 'bold'),
                          bd=4, text=invtriglist[i][:-1]))
            l=80
            if i>=3:
                l=10
            invtrigButton[i]["command"] = lambda x=invtriglist[i]: self.funcEnter((x))
            invtrigButton[i].grid(row=int(i//(3)+4),column=i%3,padx=7,pady=(l,10))

        self.mathfunc.mainloop()
    def delete(self,t):
        txtDisplay[t].destroy()
        txtDisplay[t]=0
        self.equation[t]=''
        close[t].destroy()
        close[t]=0
    def graph(self):
        if self.process==False:
            try:
                plt.clf()
                plt.close(1)
            except:
                pass
        self.process=False
        self.fig=plt.figure()
        self.ax=self.fig.add_subplot(1,1,1)
        self.ax.spines['left'].set_position('center')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['top'].set_color('none')
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')


 
        plt.xlim([self.lower,self.upper])
        plt.ylim([self.lrange,self.urange])
        x=arange(self.lower,self.upper,0.01)
        for graphs in self.equationlist:
            if graphs!='' and graphs!=None:
                fx = graphs
                
                try:
                    eqy=eval(bytes(ord(p) for p in fx))
                    eqy=eqy*x**0
                    L=[]
                    for j in self.strequationlist:
                        if j not in L:
                            L.append(j)
                    try:
                        plt.plot(x,eqy,label=fx)
                    except:
                        pass
                except:
                    pass

        plt.legend(loc='upper right')
        plt.show()
    def graphingEnter(self):
        for j in range(len(self.equation[self.present])-1):
            a = self.equation[self.present][j]
            b=self.equation[self.present][j+1]
            if a.isdigit():
                if b=='(':
                    self.equation[self.present][j]=a+'*'
                elif b in ['arcsin(','arccos(','arctan(','arccsc(','arcsec(','arccot(',
                                        'sin(','cos(','tan(','csc(','sec(','cot(','x']:
                    self.equation[self.present][j]=a+'*'
            if a==')':
                if b.isdigit() or b=='\u03C0':
                    self.equation[self.present][j]=a+'*'
                elif b in ['arcsin(','arccos(','arctan(','arccsc(','arcsec(','arccot(',
                                        'sin(','cos(','tan(','csc(','sec(','cot(','x']:
                    self.equation[self.present][j]=a+'*'
            if a=='x':
                if b in ['arcsin(','arccos(','arctan(','arccsc(','arcsec(','arccot(',
                                        'sin(','cos(','tan(','csc(','sec(','cot(','x']:
                    self.equation[self.present][j]=a+'*'
            if a.isdigit():
                if b=='pi':
                    self.equation[self.present][j]=a+'*'
        '''bin = 0
        sq=0
        for i in len(self.equation[self.present]):
            if self.equation[self.present][i] =='\u221A':
                self.equation[self.present][i]='sqrt('
                sq+=1
            if sq >=1:
                if self.equation[self.present][i]=='(':
                    bin += 1
                if self.equation[self.present][i]==')':
                    if bin>1:
                        bin-=1
                    if bin==1:
                        sq-=1
                        self.equation[self.present].insert(i,')')
'''     
        '''ab = []
        i=0
        while(True):
            if self.equation[self.present][i] =='|':
                self.equation[self.present][i]='abs('
                ab.append(1)
            if len(self.equation[self.present])==i:
                break
            i+=1
            '''
        self.equationlist=[self.collector(i) for i in self.equation]

        self.equation.append([])

        self.present+=1
        self.txtdisplayno+=1
        txtDisplay.append(Text(calc0,
                       font=('times', 15),
                        height=2,width=63,
                       bg='white',relief='sunken',
                       fg='black',
                       bd=1))
        txtDisplay[self.txtdisplayno].grid(row=self.txtdisplayno,column=0,pady=1)
        close.append(Button(calc0,
        text='x',font=('Helvetica', 15,'italic'),bg='white',relief='sunken',
                       fg='black',
                       bd=1,command= lambda x=self.txtdisplayno: self.delete(x)))
        close[self.txtdisplayno].grid(row=self.txtdisplayno,column=1)
        
        txtDisplay[self.txtdisplayno].insert(END,f'{self.txtdisplayno+1}.  ')
        txtDisplay[self.txtdisplayno].bind('<Button-1>', lambda e,i=self.txtdisplayno: graphing.test(i))
        txtDisplay[self.txtdisplayno].configure(state='disabled')
        self.graph()
if __name__=='__main__' :
    graphing=Graphing()
    
    root=Tk()
    root.title("Graphing Calculator")
    
    # sets the background color of the calculator
    # as white9
    root.configure(background = 'white')

    root.geometry("718x393")
    root.resizable(False,True)
    close=[]
    # act as a container for numbers and operators
    calc1=Frame(root)
    calc1.pack(fill='both',expand=1)
    myCanvas=Canvas(calc1)
    myCanvas.pack(side=LEFT,fill='both',expand=1)
    scrolllabel = Scrollbar(myCanvas,orient='vertical',command=myCanvas.yview)
    scrolllabel.pack(side=RIGHT,fill='y')
    myCanvas.configure(yscrollcommand=scrolllabel.set)
    myCanvas.bind('<Configure>',lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))
    calc0=Frame(myCanvas)
    myCanvas.create_window((0,0),window=calc0, anchor='nw')
    txtDisplay=[]
    txtDisplay.append(Text(calc0,
                       font=('times', 15),
                        height=2,width=63,
                       bg='white',relief='sunken',
                       fg='black',
                       bd=1))
    txtDisplay[0].grid(row=0,column=0,pady=1)
    txtDisplay[0].insert(END,f'1.  ')
    txtDisplay[0].bind('<Button-1>', lambda e,i=0: graphing.test(i))
    txtDisplay[0].configure(state='disabled')
    close.append(0)
    #numberkeys
    # store all the numbers in a variable
    calc2=Frame(root)
    calc2.pack()
    calc2.config(height=219,width=300)
    myCanvas1=Canvas(calc2)
    myCanvas1.pack(side=LEFT)
    myCanvas1.config(height=210,width=700)
    calc=Frame(myCanvas1)
    myCanvas1.create_window((0,0),window=calc, anchor='nw')
    calc.config(height=100,width=100)
    # holds the buttons in the calculator,
    numberpad = "789/456*123-0.=+"
    
    # here i will count the rows for placing buttons
    # in grid
    i = 0
    
    # create an empty list to store
    # each button with its particular specifications
    btn = []
    
    # j is in that range to place
    # the button in that particular row
    for j in range(2, 6):
    
            # k is in this range to place the
        # button in that particular column
        
        for k in range(4):
            texchar=numberpad[i]
            if texchar=='*':
                texchar='x'
            btn.append(Button(calc,
                              width=4,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('times', 15, 'bold'),
                              bd=4, text=texchar))
    
            # set buttons in row & column and
            # separate them with a padding of 1 unit
            btn[i].grid(row=j-1, column=k+4, pady=4,padx=(2,2))
    
            # put that number as a symbol on that button
            btn[i]["command"] = lambda x=numberpad[i]: graphing.numberEnter(str(x))
            i += 1

    #______________________________________
    #special key
    pichar='\u03C0'
    sqchar='\u221A'
    spkey=f'xy`~()<>|,{chr(8805)}{chr(8804)}-_{sqchar}{pichar}'
    i=0
    spebtn=[]

    for j in range(2, 6):
    
            # k is in this range to place the
        # button in that particular column
        for k in range(4):
            texchar=spkey[i]
            if texchar=='|':
                texchar='|a|'
            elif texchar=='`':
                texchar='a\u00B2'
            elif texchar=='~':
                texchar='a\u1D47'
            elif texchar=='-':
                texchar='ABC'
            elif texchar=='_':
                texchar='rand'
            spebtn.append(Button(calc,
                              width=4,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('times', 15, 'italic'),
                              bd=4, text=texchar))
    
            # set buttons in row & column and
            # separate them with a padding of 1 unit
            if k!=3:
                spebtn[i].grid(row=j-1, column=k, pady=2,padx=(2,2))
            else:
                spebtn[i].grid(row=j-1, column=k, pady=2,padx=(2,20))

            # put that number as a symbol on that button
            if i==2:
                spebtn[i]["command"] = lambda x='**2': graphing.numberEnter((x))
            elif i==3:
                spebtn[i]["command"] = lambda x='**(': graphing.numberEnter((x))
            elif texchar==pichar:
                spebtn[i]["command"] = lambda x='pi': graphing.numberEnter((x))
            elif texchar=='rand':
                spebtn[i]["command"] = lambda x='random(': graphing.numberEnter((x))
            elif texchar =='\u221A':
                spebtn[i]["command"] = lambda x='\u221A(': graphing.numberEnter(('sqrt('))
            else:
                spebtn[i]["command"] = lambda x=spkey[i]: graphing.numberEnter(str(x))
            i += 1
    
    #_______________________
    #functioning buttons
    funcbtn=[]
    funcbtn.append(Button(calc,
                              width=5,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('times', 15, 'bold'),
                              bd=4,text='func'))
    funcbtn[0]['command']=lambda: graphing.functions()
    funcbtn[0].grid(row=1, column=9, pady=2,padx=(80,0))
    funcbtn.append(Button(calc,
                              width=3,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('times', 15, 'bold'),
                              bd=4,text='\u2190'))
    funcbtn[1]['command']=lambda: graphing.backnForth(backward=1)
    funcbtn[1].place(x=581,y=54)
    funcbtn.append(Button(calc,
                              width=3,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('times', 15, 'bold'),
                              bd=4,text='\u2192'))
    funcbtn[2]['command']=lambda: graphing.backnForth(forward=1)
    funcbtn[2].place(x=633,y=54)
    funcbtn.append(Button(calc,
                              width=5,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('times', 15, 'bold'),
                              bd=4,text='AC'))
    funcbtn[3]['command']=lambda: graphing.clear()
    funcbtn[3].grid(row=3, column=9, pady=2,padx=(80,0))
    
    funcbtn.append(Button(calc,
                              width=5,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('times', 15, 'bold'),
                              bd=4,text='Enter'))
    funcbtn[4]['command']=lambda: graphing.graphingEnter()
    funcbtn[4].grid(row=4, column=9, pady=2,padx=(80,0))
    i=0
    #________________________
    root.mainloop()