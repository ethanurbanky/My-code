from tkinter import*
import webbrowser
from tkinter import Frame, Tk, Button

url = 'file:///Users/ethan.urbanky/Documents/Html/home%20page.html'     
root = Tk()
root.title("Sleep tight")
root.geometry("1075x900")
frame = Frame(root)
frame.pack()

def OpenUrl():
    webbrowser.open_new(url)
    
topframe = Frame(root,bg="teal")
topframe.pack(fill=X)
l6 = Label(topframe,text="Sleep Tight", bg = "teal", fg = "white")
l6.pack(side=LEFT)

aframe = Frame(root,borderwidth = 1.5, relief=RAISED,width=10000)
aframe.place(x=300,y=30)
aframe.pack_propagate(10) 
l3 = Label(aframe,text="When do you want to wake up:\n",fg="#008080")
l3.pack(side = LEFT)
E1 = Entry(aframe)
E1.pack(side=TOP,ipady=19)
E2 = Entry(aframe)
E2.pack(side=TOP,ipady=12)
E3 = Entry(aframe)
E3.pack(side=TOP,ipady=12)



titleheight = 100 # set variable to height of title frame
titleframe = Frame(root,width=200,height=titleheight,bg="black") # top title frame
titleframe.place(x=50,y=300) # fill entire container frame
titleframe.pack_propagate(0) # enforce frame size, do not change to content size
title = Label(titleframe,text="About Us",fg="white",bg="black")
title.config(font=("Arial", 32))
title.pack(ipady=titleheight/2) # set internal padding to place title in centre
contentheight = 150
contentframe = Frame(root,width=200,height=contentheight,bg="#008080")
contentframe.place(x=50,y=400)
contentframe.pack_propagate(0)
content = Label(contentframe,text="Click Explore \n to learn a little \n about the creator \n of the website",bg="#008080")
content.pack(ipady=contentheight/2)

titleheight = 100 # set variable to height of title frame
titleframe = Frame(root,width=200,height=titleheight,bg="black") # top title frame
titleframe.place(x=400,y=300) # fill entire container frame
titleframe.pack_propagate(0) # enforce frame size, do not change to content size
title = Label(titleframe,text="Need Help",fg="white",bg="black")
title.config(font=("Arial", 32))
title.pack(ipady=titleheight/2) # set internal padding to place title in centre
contentheight = 150
contentframe = Frame(root,width=200,height=contentheight,bg="#008080")
contentframe.place(x=400,y=400)
contentframe.pack_propagate(0)
content = Label(contentframe,text="Click Explore \n if you are in need of help",bg="#008080")
content.pack(ipady=contentheight/2)


titleheight = 100 # set variable to height of title frame
titleframe = Frame(root,width=200,height=titleheight,bg="black") # top title frame
titleframe.place(x=750,y=300) # fill entire container frame
titleframe.pack_propagate(0) # enforce frame size, do not change to content size
title = Label(titleframe,text="Why Sleep",fg="white",bg="black")
title.config(font=("Arial", 32))
title.pack(ipady=titleheight/2) # set internal padding to place title in centre
contentheight = 150
contentframe = Frame(root,width=200,height=contentheight,bg="#008080")
contentframe.place(x=750,y=400)
contentframe.pack_propagate(0)
content = Label(contentframe,text="Click Explore \n to learn a little \n about sleep",bg="#008080")
content.pack(ipady=contentheight/2)




#first button


button = Button(frame, text="Explore", command=OpenUrl)

button.pack(ipady=10,ipadx=423)
frame.place(x=49,y=549)
root.mainloop()



