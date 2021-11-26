from tkinter import *
import math
class trignometry:
        root=Tk()
        root.title("Trignometry solver.")
        global Answer_bar
        Answer_bar=Entry(root,width=60,borderwidth=10)
        Answer_bar.grid(row=0,column=0,columnspan=3)
        global Input_bar
        Input_bar=Entry(root,width=40,borderwidth=7)
        Input_bar.grid(row=3,column=0,columnspan=3)
        Input_bar.insert(0,"Enter your value here.")
        #Functions
        def sin():
            global strs
            strs="Sin"
        def cos():
            global strs
            strs="Cos"
        def tan():
            global strs
            strs="Tan"
        def cosec():
            global strs
            strs="Cosec"
        def sec():
            global strs
            strs="Sec"
        def cot():
            global strs
            strs="Cot"
        def calculate():
        
            if(strs=="Sin"):
                n=math.sin(math.radians(int(Input_bar.get())))
                Answer_bar.insert(0,(n))
            elif(strs=="Cos"):
                n=math.cos(math.radians(int(Input_bar.get())))
                Answer_bar.insert(0,(n))
            elif(strs=="Tan"):
                n=math.tan(math.radians(int(Input_bar.get())))
                Answer_bar.insert(0,(n))
            elif(strs=="Cosec"):
                n=1/(math.sin(math.radians(int(Input_bar.get()))))
                Answer_bar.insert(0,(n))
            elif(strs=="Sec"):
               n=1/(math.cos(math.radians(int(Input_bar.get()))))
               Answer_bar.insert(0,(n))
            elif(strs=="Cot"):
                n=1/(math.tan(math.radians(int(Input_bar.get()))))
                Answer_bar.insert(0,(n))

            
        def clear():
            Answer_bar.delete(0,END)
            Input_bar.delete(0,END)




        # Button Assignment
        sin=Button(root,text="Sin",padx=57,pady=5,command=sin).grid(row=1,column=0)
        cos=Button(root,text="Cos",padx=50,pady=5,command=cos).grid(row=1,column=1)
        tan=Button(root,text="Tan",padx=50,pady=5,command=tan).grid(row=1,column=2)
        cosec=Button(root,text="Cosec",padx=50,pady=5,command=cosec).grid(row=2,column=0)
        sec=Button(root,text="Sec",padx=50,pady=5,command=sec).grid(row=2,column=1)
        cot=Button(root,text="Cot",padx=50,pady=5,command=cot).grid(row=2,column=2)
        go=Button(root,text="Go!",padx=60,pady=3,command=calculate).grid(row=4,column=0,columnspan=3)
        refresh=Button(root,text="Clear",padx=60,pady=3,command=clear).grid(row=5,column=0,columnspan=3)
        

        
        
        
        
        
        
        root.mainloop()

        