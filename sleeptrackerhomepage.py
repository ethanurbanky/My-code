from tkinter import*
from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox

  
root = Tk()
root.title("Sleep tight")
root.geometry("1075x900")


titleheight = 100 # set variable to height of title frame
titleframe = Frame(root,width=200,height=titleheight,bg="black") # top title frame
titleframe.place(x=0,y=0) # fill entire container frame
titleframe.pack_propagate(0) # enforce frame size, do not change to content size
title = Label(titleframe,text="Fun Fact",fg="white",bg="black")
title.config(font=("Arial", 32))
title.pack(ipady=titleheight/2) # set internal padding to place title in centre
contentheight = 150
contentframe = Frame(root,width=200,height=contentheight,bg="#008080")
contentframe.place(x=0,y=100)
contentframe.pack_propagate(0)
content = Label(contentframe,text="Today, 75% of us \n dream in coulor. \n but before coulor T.V's \n just 15% of us \n did",bg="#008080")
content.pack(ipady=contentheight/2)



titleheight = 100 # set variable to height of title frame
titleframe = Frame(root,width=200,height=titleheight,bg="black") # top title frame
titleframe.place(x=900,y=0) # fill entire container frame
titleframe.pack_propagate(0) # enforce frame size, do not change to content size
title = Label(titleframe,text="Fun Fact",fg="white",bg="black")
title.config(font=("Arial", 32))
title.pack(ipady=titleheight/2) # set internal padding to place title in centre
contentheight = 150
contentframe = Frame(root,width=200,height=contentheight,bg="#008080")
contentframe.place(x=900,y=100)
contentframe.pack_propagate(0)
content = Label(contentframe,text="Only 21% of \n Americans get \n the recommended \n seven to eight hours \n sleep each night.",bg="#008080")
content.pack(ipady=contentheight/2)

topframe = Frame(root,bg="teal")
topframe.pack(fill=X)
l6 = Label(topframe,text="Sleep Tracker", bg = "teal", fg = "white")
l6.pack(side=LEFT)
can1 = Canvas(topframe,height="20",bg="#b50909",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill="white")


aframe = Frame(root,borderwidth = 1.5, relief=RAISED,width=10000)
aframe.place(x=350,y=700)
aframe.pack_propagate(10) 
l3 = Label(aframe,text="When do you want to wake up:\n",fg="#008080")
l3.pack(side = LEFT)
E1 = Entry(aframe)
E1.pack(side=TOP,ipady=19)


counter = -1
running = False
def counter_label(label): 
	def count(): 
		if running: 
			global counter 

			# To manage the intial delay. 
			if counter==-1:			 
				display="Starting..."
			else: 
				display=str(counter) 

			label['text']=display # Or label.config(text=display) 

			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			label.after(1000, count) 
			counter += 1

	# Triggering the start of the counter. 
	count()	 

# start function of the stopwatch 
def Start(label): 
	global running 
	running=True
	counter_label(label) 
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# Stop function of the stopwatch 
def Stop(): 
	global running 
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

# Reset function of the stopwatch 
def Reset(label): 
	global counter 
	counter=-1

	# If rest is pressed after pressing stop. 
	if running==False:	 
		reset['state']='disabled'
		label['text']='Good Morning'

	# If reset is pressed while the stopwatch is running. 
	else:			 
		label['text']='Starting...'



# Fixing the window size. 

label =Label(root, text="Good Morning", fg="black", font="Verdana 30 bold") 
label.place(x=500,y=250) 
start = Button(root, text='Start', width=15, command=lambda:Start(label)) 
stop = Button(root, text='Stop', width=15, state='disabled', command=Stop) 
reset =Button(root, text='Reset', width=15, state='disabled', command=lambda:Reset(label)) 
start.place(x=500,y=300) 
stop.place(x=500,y=320) 
reset.place(x=500,y=340) 
root.mainloop()



root = Tk()
root.title("Alarm clock")
def SubmitButton():
  AlarmTime= entry1.get()
  Message1()
  #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
  CurrentTime = time.strftime("%H:%M")
  print("the alarm time is: {}".format(AlarmTime))
  #label2.config(text="")
  while AlarmTime != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
    CurrentTime = time.strftime("%H:%M")
    time.sleep(1)
  if AlarmTime == CurrentTime:
     print("now Alarm Musing Playing")
     os.system("start alarm-music.mp3")
     label2.config(text = "Alarm music playing.....")
     messagebox.showinfo(title= 'Alarm Message', message= "{}".format(entry2.get()))
def Message1():
    AlarmTimeLable= entry1.get()
    label2.config(text="the Alarm time is Counting...")
    #label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable))     
frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height = 100, width = 100)

label1= ttk.Label(frame1,text = "Enter the Alarm time :")
label1.pack()


entry1 = ttk.Entry(frame1, width = 30)
entry1.pack()
entry1.insert(3,"example - 13:15")

labelAlarmMessage= ttk.Label(frame1, text="Alarm Message:")
labelAlarmMessage.pack()

entry2= ttk.Entry(frame1, width=30)
entry2.pack()

button1= ttk.Button(frame1, text= "submit", command=SubmitButton)
button1.pack()
#this Label2 will show the Last Alarm Time
label2= ttk.Label(frame1)
label2.pack()

    
#label2.config(text="hello")

root.mainloop()




