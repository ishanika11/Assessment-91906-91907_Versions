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
 

#***********************************************PAGE 1********************************************************

class UsersInfo:

    def __init__(self):

#The header/instructions for user to follow

        self.welcome = Label(page1, fg = "#54748D", text='PLEASE ENTER YOUR DETAILS', font=('Arial', 20, 'bold'))

        self.welcome.place(x=20, y=25)
        
#Adding an image to the opening page
        img = ImageTk.PhotoImage(Image.open("imagetest1.png"))

        label= Label(page1)

        label.place(x=320, y=270)

        label.config(image=img)

        label.image=img
 

#Label which displays users name

        self.name = Label(page1, text='Name', font=('Arial', 15, 'bold'))

        self.name.place(x=225, y=100)


#Entry box for user to enter their name

        self.ent_name = Entry(page1,textvariable = name)

        self.ent_name.place(x=350, y=106)



#Label which displays users year level

        self.year = Label(page1, text='Year Level', font=('Arial', 15, 'bold'))

        self.year.place(x=225, y=150)

 

#Entry box for user to enter their year level

        self.ent_year = Entry(page1)

        self.ent_year.place(x=350, y=155)

 

#The text (warning message) which pops up to validate the users input

        self.warning_name = Label(page1, text="", font=('Arial', 12))

        self.warning_name.place(x=260, y=250)


        self.warning_year = Label(page1, text="", font=('Arial', 12, ))

        self.warning_year.place(x=260, y=230)

 

#Displaying the "NEXT" button to continue to the second page (introduction)

        self.buttons()
 
    def buttons(self):

        pg1_button = Button(page1, text='NEXT', command= self.Check_Entry, font=('Arial', 13, 'bold'))
        pg1_button.place(x=350, y=200)


#This function checks for the validity of the user's input in the NAME section:

    def check_nameValue(self):

        self.warning_name.config(text="")


        while len(self.ent_name.get()) >= 1:

            if all(name.isalpha() or name.isspace() for name in self.ent_name.get()):

                self.warning_name.config(text="")
                return True
                break


#Validates that no numerical or other values have been inputted (considers any errors made and let's the user retry)

            else:

                self.warning_name.config(text="Invalid input. Please enter alphabetical values", fg='red')

                self.ent_name.delete(0,END)


                return False

                break
        else:

            len(self.ent_name.get()) < 1

            self.warning_name.config(text="Try Again! Please enter your name", fg='blue')
 #This will imply that if one box has something entered and the other does not, the box will become empty again
            return False
       

#This function checks for the validity of the user's input in the "YEAR_LEVEL" section:     

    def check_yearValue(self):

        self.warning_year.config(text="")

        try:

            while len(self.ent_year.get()) >= 1:
#Setting up the range for the year level values

                if int(self.ent_year.get()) >= 8 and int(self.ent_year.get())<= 13:

                    self.warning_year.config(text="")

                    return True

#Will make sure any user using the quiz is for the designated years 8-13

                else:

                    self.warning_year.config(text="Apologies, you must be between years 8-13 to continue", fg="red")

                    self.ent_year.delete(0,END)

                    return False
            else:

                len(self.ent_year.get()) < 1

                self.warning_year.config(text="Please enter your year level", fg='blue')

                return False

#If the age inputted by the user is not between 12 - 18, the error message will show up, and the entry box will go blank


        except ValueError:

            self.warning_year.config(text="Invalid Year Group. Please enter numerical value.", fg="red", )

            self.ent_year.delete(0,END)

            return False

#IF the age inputted is not a numerical value, the error message will show up and the entry box will go blank.


    def Check_Entry(self):


        validate_name = self.check_nameValue()
        validate_year = self.check_yearValue()

 

        if validate_name == True and validate_year == True:

           show_frame(page2)

           self.ent_name.delete(0, END)

           self.ent_year.delete(0,END)


           
#The first flower border
    img2 = ImageTk.PhotoImage(Image.open("flower2.png"))

    label= Label(page1)

    label.place(x=500, y=0)

    label.config(image=img2)

    label.image=img2
#The second flower border

    img3 = ImageTk.PhotoImage(Image.open("flower1.png"))

    label= Label(page1)

    label.place(x=0, y=320)

    label.config(image=img3)

    label.image=img3
 

#Calling the checking functions, and placing them under one single function, to be called in the "Enter" button.


page1 = UsersInfo()


#***********************************************PAGE 2********************************************************
 
#creating opening title and text to introduce the user
pag2_label = Label(page2, fg = "#D284AC", text='WELCOME TO', font=('Arial', 30, 'bold'))

pag2_label.place(x=250, y=25)

 

#adding imagery to make the interface more visually appealing

canvas = Canvas(page2, width = 200, height = 150) 

canvas.place(x=280, y=80)

img = ImageTk.PhotoImage(Image.open("gcc_logo1.png"))

canvas.create_image(20, 20, anchor=NW, image=img)


openingtitle = Label(page2, fg = "#9A4794", text = "Girls Can Code!", font = ("Times", "40"))

openingtitle.place(x=215, y=230)


#Label for introduction for the second page

opening_sub = Label(page2, fg = "#D284AC", text = "Welcome to the Girls Can Code quiz \nwhere women can come together and \n learn more about eachother.", font = ("Times", "20"))

opening_sub.place(x=185, y=300)

 

login_registers = Label(page2, fg = "#D284AC", text = "This is a product, promoting women \n in computer and prorgramming classes\n we need more young girls to pursue these \n careers and understand just how fun \ncoding can be!", font = ("Times", "20"))

login_registers.place(x=160, y=395)


'''creating a button for the user to click which links into the third page: this is the beginning of the actual quiz'''
pg2_button = Button(page2, text='START', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))

pg2_button.place(x=355, y=560)

 

#***********************************************PAGE 3********************************************************
page3.config(background='#F5BDC7')


##pag3_label = Label(page3, text='WELCOME TO PAGE 3', font=('Arial', 30, 'bold'))

##pag3_label.place(x=50, y=100)


 
#assigning the questions for the quiz under one varible name'

q=["The first computer programmer, who is she?",

    "An american female computer scientist, who is she?",

   "Popular film actress in the 1960's, who is she?",

   "One of the first computer software programmers, who is she?",
   
   "Who’s the former president and CEO of eBay and HP enterprises?",
   
   "She was the first female engineer hired at Google and was the CEO of Yahoo. \nWho is she?",

   "GENERAL QUESTION:What is a correct syntax to output Hello World in Python?",

   "Who was the first ever home computer user?",

   "Who was the women which inspired GUI (graphical user interface)?",

   "Who was the first ever women to earn a computer science PhD?",

   "GENERAL QUESTION: Select the following answer which indicates a comment",

   "Who is commonly reffered to as The pioneer in Information Science?",

   "Who is the director of user experience at google?",

   "Who is the CEO of Oracle?",

   "Finally as of 2022, what is the percentage of women in tech?"
   ]

 
'''assigining the options for the buttons which the user has to select,
creating this in lists so that they are grouped to specific questions'''
options=[

         ['Janet Jackson','Charlotte Webster','Ada LoveLace','Briana Lockwood'],['Josephine Taylor','Kate Shaw','Melinda Grace','Grace Hopper',],

         ['Hedy Lamarr','Rose Quartz','Yvonne Williams','Mary Kate'],['Rina Hemlock','Margaret Hamilton','Adel Sherlock'],

         ['Sandra Learner', 'Tarah Wheeler', 'Sheryl Sandberg', 'Meg Whitman'], ['Marissa Mayor', 'Jessica Burns', 'Sasha Banks','Sarah J. Mass'],

         ['print("Hello World")', 'p("Hello World")', 'echo("Hello World")', 'echo"Hello World"'], ["Bella Swan", "Radia Pearlman", "Katherine Johnson", "Mary Wilkes"],

         ['Annie Easley', 'Karen Jones', 'Adele Goldberg', 'Elizabeth Feinler'], ['Miah Walters', 'Mary Keller', 'Kendall Keller', 'Mary Anne'],

         ['* This is a comment', '# This is a comment', '// This is a comment', '- This is a comment'], ['Karen Jones', 'Macy Williams', 'Lorelle Scott', 'Kamala Khan'],

         ['Lacy Carter', 'Sarah Goldberg', 'Amarah Sandra', 'Elizabeth Churchill'],['Safra Catz', 'Sofia Collins', 'Renesme Yassir', 'Cora Minaj'],

         ['35.6%', '45.6%','26.7%','14.2%']

        ]

 
'''assigning the order of the actual answers'''
a=[3,4,1,2,4,1,1,4,3,2,2,1,4,1,3]

 
'''adding imagery to each frame which associates with the questions asked (some are hints for the users'''
images=["AdaLoveLace.jpg","GraceHopper.jpg","HedyLamarr.jpg","MargaretHamilton.jpg","eBay.jpg","illustration.jpg", "codepic.jpg",
        "marywilkes.jpg","guiimage.jpg", "wit.jpg", "comment.jpg", "illu2.jpg", "google.jpg", "STEM.jpg","older.jpg"]

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
    
#saving users information and scores to an exterior text file'''
        with open('myscore.txt', 'a') as f:      
            f.write('\n'+(row))
## -------------------------------------
 

 

quiz=Quiz()

#window.mainloop()

 

