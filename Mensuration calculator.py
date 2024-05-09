import tkinter as tk
from tkinter import messagebox as m
def check ():
    x=n1.get ()
    y=0
    area=0
    y=n2.get ()
    if(x==1):
        #RECTANGLE
        if(y==1):
            l=side1.get ()
            b=side2.get ()
            if(l!=""and b!=""):
                area=float(l)*float(b)
                result="Area of rectangle is "+str(area)
                m.showinfo("Result",result)
            else:
                m.showerror("Result","Enter both length and breadth")

        #SQAURE
        if(y==2):
            l=side1.get ()
            if(l!=""):
                area=float(l)*float(l)
                result="Area of square is "+str(area)
                m.showinfo("Result",result)
            else:
                m.showerror("Result","Enter side")
            
                    
        #TRIANGLE
        if(y==3):
            h=side1.get ()
            b=side2.get ()
            if(h!=""and b!=""):
                area=0.5*float(h)*float(b)
                result="Area of triangle is "+str(area)
                m.showinfo("result",result)
            else:
                m.showerror("Result","Enter both height and base")
            
                    
        

        #CIRCLE
        if (y==4):
            r=side1.get ()
            if(r!=""):
                area=float(r)*float(r)*3.14
                result="Area of circle is"+str(area)
                m.showinfo("result",result)
            else:
                m.showerror("Result","Enter  radius")

    

    #CUBIOD   
    elif( y==5):
        l=side1.get ()
        b=side2.get ()
        h=side3.get ()
        if(l!=""and b!="" and h!=""):
            area=float(l)*float(b)*float(h)
            result="Volume of cubiod is "+str(area)
            m.showinfo("Result",result)
        else:
            m.showerror("Result","Enter length, breadth and height ")

    #CUBE
    if( y==6):
        l=side1.get ()
        if(l!=""):
            area=float(l)*float(l)*float(l)
            result="Volume of cube is "+str(area)
            m.showinfo("Result",result)
        else:
            m.showerror("Result","Enter side")
        
    #CYLINDER
    if( y==7):
        r=side1.get ()
        h=side2.get ()
        if(r!="" and h!=""):
            area=3.14*float(h)*float(r)*float(r)
            result="Volume of cylinder is "+str(area)
            m.showinfo("Result",result)
        else:
            m.showerror("Result","Enter both radius and height")
                

    #SPHERE         
    if( y==8):
        r=side1.get ()
        if(r!=""):
            area=4/3*3.14*float(r)*float(r)*float(r)
            result="Volume of sphere is "+str(area)
            m.showinfo("Result",result)
        else:
            m.showerror("Result"," Enter radius")
            
    else:
        m.showerror("result","Select correct option")
        

from tkinter import messagebox as m
page1=tk.Tk()
page1.geometry("400x450")
page1.title=("MENSURATION CALCULATOR")
page1.configure(bg="light blue")
lbl1=tk.Label(page1,text="MENSURATION CALCULATOR",bg="light blue",fg="blue",font=("bold",20)).place(x=260,y=0)
n1=tk.IntVar ()
n3=tk.IntVar()
rb1=tk.Radiobutton(page1,text=" AREA",bg="light blue",fg="green",font=("bold",20),variable=n1,value=1).place(x=200,y=100)
rb2=tk.Radiobutton(page1,text="VOLUME",bg="light blue",fg="green",font=("bold",20),variable=n1,value=2).place(x=600,y=100)
n2=tk.IntVar ()
rb1=tk.Radiobutton(page1,text="Rectangle",bg="light blue",fg="dark green",font=("bold",12),variable=n2 ,value=1).place(x=200,y=140)
rb2=tk.Radiobutton(page1,text="Square",bg="light blue",fg="dark green",font=("bold",12),variable=n2,value=2).place(x=200,y=170)
rb3=tk.Radiobutton(page1,text="Triangle",bg="light blue",fg="dark green",font=("bold",12),variable=n2,value=3).place(x=200,y=200)
rb4=tk.Radiobutton(page1,text="Circle",bg="light blue",fg="dark green",font=("bold",12),variable=n2,value=4).place(x=200,y=230)

n3=tk.IntVar()
rb1=tk.Radiobutton(page1,text="Cuboid",bg="light blue",fg="dark green",font=("bold",12),variable=n2,value=5).place(x=600,y=140)
rb2=tk.Radiobutton(page1,text="Cube",bg="light blue",fg="dark green",font=("bold",12),variable=n2,value=6).place(x=600,y=170)
rb3=tk.Radiobutton(page1,text="Cylinder",bg="light blue",fg="dark green",font=("bold",12),variable=n2,value=7).place(x=600,y=200)
rb4=tk.Radiobutton(page1,text="Sphere",bg="light blue",fg="dark green",font=("bold",12),variable=n2,value=8).place(x=600,y=230)




side1=tk.StringVar()
side2=tk.StringVar()
side3=tk.StringVar()
txt1=tk.Entry(page1,width=10,textvariable=side1).place(x=900,y=111)
txt2=tk.Entry(page1,width=10,textvariable=side2).place(x=900,y=150)
txt3=tk.Entry(page1,width=10,textvariable=side3).place(x=900,y=189)

btn1=tk.Button(page1,text="check",command=check).place(x=400,y=300)
page1.mainloop()

