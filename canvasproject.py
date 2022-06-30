from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()

root.title("ShapeScape")
root.geometry("500x500")

colorlabel=Label(root,text="Enter color here:")
colorlabel.place(relx=0.5,rely=0.8,anchor=CENTER)

colorinput=Entry(root)
colorinput.place(relx=0.5,rely=0.9,anchor=CENTER)


colorinput.insert(0,"black")


canvas=Canvas(root,width=480,height=300,bg="white",highlightbackground="grey")
canvas.pack()



direction=""

oldx=50
oldy=50
newx=50
newy=50

def right_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+5
    direction= "right"
    draw(direction, oldx, oldy, newx, newy)
    
def left_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx-5
    direction= "left"
    draw(direction, oldx, oldy, newx, newy)
    
def up_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy-5
    direction= "up"
    draw(direction, oldx, oldy, newx, newy)
    
    
def down_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy+5
    direction= "down"
    draw(direction, oldx, oldy, newx, newy)
    
def draw(direction,oldx,oldy,newx,newy):
    fill_color=colorinput.get()
    if(direction=="right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color) 
        
def SquareDraw(direction,newx,newy):
    newx=
    newy=20
    square=canvas.create_rectangle(newx,newy,50,50,fill=colorinput.get()) 
    if(direction=="right"):
        right_line=canvas.create_rectangle(newx,newy,50,50,fill=colorinput.get()) 
    if(direction=="left"):
        left_line=canvas.create_rectangle(newx,newy,50,50,fill=colorinput.get()) 
    if(direction=="up"):
        up_line=canvas.create_rectangle(newx,newy,50,50,fill=colorinput.get()) 
   
        
Shape=Button(root,text="Square",command=SquareDraw)
Shape.place(relx=0.7,rely=0.9,anchor=CENTER)

    if(direction=="right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color) 
        

    
canvas.pack()    
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)

root.mainloop()