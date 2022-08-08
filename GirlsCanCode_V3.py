'''
the following are the external libraries that are being imported
these will help me in developing the graphical user interface,
making quiz, using images and writing the score to an external
file such as csv. 

'''
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import csv


window = Tk()

window.geometry("800x600")

window.rowconfigure(0, weight=1)

window.columnconfigure(0, weight=1)

##window.state('zoomed')class Quiz:

 

 
'''creating each frame for the pages which need to open
(there will be three main pages in total)'''

page1 = Frame(window, width=700, height=500)

page2 = Frame(window, width=700, height=500)

page3 = Frame(window, width=700, height=500)

 

for frame in (page1, page2, page3):

    frame.grid(row=0, column=0, sticky='nsew')

 

def show_frame(frame):

    frame.tkraise()

 

show_frame(page1)
name = StringVar()
yr_level = StringVar()
 

# ============= Page 1 =========

#Creating label to display the name

pag1_label = Label(page1, text='Name', font=('Arial', 15, 'bold'))

pag1_label.place(x=50, y=100)

 
#Entry box for user to enter their name
pag1_entry = Entry(page1,textvariable = name)

pag1_entry.place(x=170, y=106)

 
#Creating label to display year level
pag1_label2 = Label(page1, text='Year Level', font=('Arial', 15, 'bold'))

pag1_label2.place(x=50, y=150)

 
#Entry box for user to enter their year level
pag1_entry2 = Entry(page1,textvariable = yr_level)

pag1_entry2.place(x=170, y=155)

 
#Button for user to select to move onto next frame
pg1_button = Button(page1, text='NEXT', font=('Arial', 13, 'bold'), command=lambda: show_frame(page2))

pg1_button.place(x=170, y=200)

 

 

# ======== Page 2 ===========

#Creating label to welcome user

pag2_label = Label(page2, fg = "#D284AC", text='WELCOME TO', font=('Arial', 30, 'bold'))

pag2_label.grid(row = 0,column=1)

 

 
#Addingimagery
canvas = Canvas(page2, width = 200, height = 150) 

canvas.grid(row = 1,column=1)

img = ImageTk.PhotoImage(Image.open("gcc_logo1.png"))

canvas.create_image(20, 20, anchor=NW, image=img)

openingtitle = Label(page2, fg = "#9A4794", text = "Girls Can Code!", font = ("Times", "40"))

openingtitle.grid(row = 2, column = 1)

 
#Introductory sentence
opening_sub = Label(page2, fg = "#D284AC", text = "Welcome to the Girls Can Code quiz \nwhere women can come together and \n learn more about eachother.", font = ("Times", "20"))

opening_sub.grid(row = 3, column = 1)

 

login_registers = Label(page2, fg = "#D284AC", text = "This is a product, promoting women \n in computer and prorgramming classes\n we need more young girls to pursue these \n careers and understand just how fun \ncoding can be!", font = ("Times", "20"))

login_registers.grid(row = 4, column = 1)

 
#Start button for user to select to move onto next page
pg2_button = Button(page2, text='START', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))

pg2_button.grid(row = 5, column = 1)

 

#show_frame(page2)

# ======== Page 3 ===========

page3.config(background='#E1B0DE')

##pag3_label = Label(page3, text='WELCOME TO PAGE 3', font=('Arial', 30, 'bold'))

##pag3_label.place(x=50, y=100)

#QUIZ NEEDS TO GO HERE

 

 
#Setting variables for questions
q=["who is this lady?",

    "Who is this lady?",

   "Who is this lady?",

   "Who is this lady?"]

#options for user to select

options=[

         ['Janet','Charlotte','AdaLoveLace','Briana'],['Josephine','Kate','Melinda','GraceHopper',],

         ['HedyLamarr','Rose','Yvonne','Mary'],['Rina','MargaretHamilton','Adel']

        ]

 
#Actual answers which gives user points
a=[3,4,1,2]

 
#Images shown on each frame
images=["AdaLoveLace.jpg","GraceHopper.jpg","HedyLamarr.jpg","MargaretHamilton.jpg"]

#window.geometry("800x500")

#window.title("Quiz")

 

 

class Quiz:

    def __init__(self):

        self.qn = 0

        self.ques = self.question(self.qn)

        self.images=images

        self.display_image(self.qn)

        self.opt_selected = IntVar()

        self.opts = self.radiobtns()

        self.display_options(self.qn)

        self.buttons()

        self.correct = 0

 

 

    def question(self, qn):
        #Creating banner displayed at the top of the frame
        t = Label(page3, text="Women in Computing", width=50, bg="blue", fg="white", font=("times", 20, "bold"))

        t.place(x=0, y=2)

        qn = Label(page3, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")

        qn.place(x=70, y=100)

        return qn

 

    def radiobtns(self):

        val = 0

        b = []

        yp = 150

        while val < 4:

            btn = Radiobutton(page3, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))

            b.append(btn)

            btn.place(x=100, y=yp)

            val += 1

            yp += 40

        return b

 

    def display_options(self, qn):

        val = 0

        self.opt_selected.set(0)

        self.ques['text'] = q[qn]

        for op in options[qn]:

              self.opts[val]['text'] = op

              val += 1

    def display_image(self, qn):
        #Display for images to show on every frame in the same place

       pic=ImageTk.PhotoImage(Image.open(images[qn]))

       label= Label(page3)

       label.place(x=380, y=150)

       label.config(image=pic)

       label.image=pic

                  

    def buttons(self):
        #creates buttons so the users have options to leave or continue throughout every frame

        nbutton = Button(page3, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))

        nbutton.place(x=200,y=380)

        quitbutton = Button(page3, text="Quit", command=window.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))

        quitbutton.place(x=380,y=380)

 

    def checkans(self, qn):

        if self.opt_selected.get() == a[qn]:

             return True

       

    def nextbtn(self):

        if self.checkans(self.qn):

            self.correct += 1

        self.qn += 1

        if self.qn == len(q):

            self.display_result()

        else:

            self.display_options(self.qn)      

            self.display_image(self.qn)

 

    def display_result(self):
        #calculation for final score + display

        score = int(self.correct / len(q) * 100)

        result = "Score: " + str(score) + "%"

        wc = len(q) - self.correct

        correct = "No. of correct answers: " + str(self.correct)

        wrong = "No. of wrong answers: " + str(wc)

        mb.showinfo("Result", "\n".join([result, correct, wrong]))
        mname = name.get()
        myear = yr_level.get()
        row =  mname+"-"+myear+"-"+str(score)

## -------writing score to file-------------
        
        with open('myscore.txt', 'a') as f:      
            f.write('\n'+(row))
## -------------------------------------
 

 

quiz=Quiz()

#window.mainloop()

