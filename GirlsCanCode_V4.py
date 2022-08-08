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

#For this version, I updated the aesthetics of the entire interface,I also changed the wording of some buttons and questions in order to make the entire quiz more overall professional.

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
#Label which displays users name
pag1_label = Label(page1, text='Name', font=('Arial', 15, 'bold'))

pag1_label.place(x=50, y=100)

 
#Entry box for user to enter their name
pag1_entry = Entry(page1,textvariable = name)

pag1_entry.place(x=170, y=106)

 
#Label which displays users year level
pag1_label2 = Label(page1, text='Year Level', font=('Arial', 15, 'bold'))

pag1_label2.place(x=50, y=150)

 
#Entry box for user to enter their year level
pag1_entry2 = Entry(page1,textvariable = yr_level)

pag1_entry2.place(x=170, y=155)

 
#Displaying the "NEXT" button to continue to the second page (introduction)
pg1_button = Button(page1, text='NEXT', font=('Arial', 13, 'bold'), command=lambda: show_frame(page2))

pg1_button.place(x=170, y=200)

 

 

# ======== Page 2 ===============

 
#creating opening title and text to introduce the user
pag2_label = Label(page2, fg = "#D284AC", text='WELCOME TO', font=('Arial', 30, 'bold'))

pag2_label.grid(row = 0,column=2)

 

 
#adding imagery to make the interface more visually appealing
canvas = Canvas(page2, width = 200, height = 150) 

canvas.grid(row = 1,column=2)

img = ImageTk.PhotoImage(Image.open("gcc_logo1.png"))

canvas.create_image(20, 20, anchor=NW, image=img)

openingtitle = Label(page2, fg = "#9A4794", text = "Girls Can Code!", font = ("Times", "40"))

openingtitle.grid(row = 2, column = 2)

 
#Label for introduction for the second page
opening_sub = Label(page2, fg = "#D284AC", text = "Welcome to the Girls Can Code quiz \nwhere women can come together and \n learn more about eachother.", font = ("Times", "20"))

opening_sub.grid(row = 3, column = 2)

 

login_registers = Label(page2, fg = "#D284AC", text = "This is a product, promoting women \n in computer and prorgramming classes\n we need more young girls to pursue these \n careers and understand just how fun \ncoding can be!", font = ("Times", "20"))

login_registers.grid(row = 4, column = 2)

 

pg2_button = Button(page2, text='START', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))

pg2_button.grid(row = 5, column = 2)

 

#show_frame(page2)

# ======== Page 3 ===========

page3.config(background='#F5BDC7')

##pag3_label = Label(page3, text='WELCOME TO PAGE 3', font=('Arial', 30, 'bold'))

##pag3_label.place(x=50, y=100)

#QUIZ NEEDS TO GO HERE

 

 
#assigning the questions for the quiz under one varible name
q=["Who is this women in the image provided?",

    "Who is this women in the image provided?",

   "Who is this women in the image provided?",

   "Who is this women in the image provided?"]

 
'''assigining the options for the buttons which the user has to select,
creating this in lists so that they are grouped to specific questions'''
options=[

         ['Janet','Charlotte','AdaLoveLace','Briana'],['Josephine','Kate','Melinda','GraceHopper',],

         ['HedyLamarr','Rose','Yvonne','Mary'],['Rina','MargaretHamilton','Adel']

        ]

 
'''assigning the order of the actual answers'''
a=[3,4,1,2]

 

images=["AdaLoveLace.jpg","GraceHopper.jpg","HedyLamarr.jpg","MargaretHamilton.jpg"]

#window.geometry("800x500")

#window.title("Quiz")

 

 
#beginning of class for the individual quiz question
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
        #banner to pop up on every question

        t = Label(page3, text="Girls Can Code", width=50, bg="#AE616F", fg="black", font=("times", 20, "bold"))

        t.place(x=0, y=2)

        qn = Label(page3, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")

        qn.place(x=70, y=100)

        return qn

 
    #creating the selection buttons for the quiz section of the game
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
    #opens image on every frame

       pic=ImageTk.PhotoImage(Image.open(images[qn]))

       label= Label(page3)

       label.place(x=380, y=150)

       label.config(image=pic)

       label.image=pic

                  

    def buttons(self):
        #creates buttons so the users have options to leave or continue throughout every frame

        nbutton = Button(page3, text="Next",command=self.nextbtn, width=10,bg="#A3C79A",fg="white",font=("times",16,"bold"))

        nbutton.place(x=200,y=380)

        quitbutton = Button(page3, text="Quit", command=window.destroy,width=10,bg="#D13B1B",fg="white", font=("times",16,"bold"))

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
        #calculation for final score + display'''

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

 

