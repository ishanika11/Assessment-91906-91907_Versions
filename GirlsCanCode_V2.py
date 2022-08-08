from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image

#Setting variables for questions
q=["Who is this women in the image provided?",
    "Who is this women in the image provided?",
   "Who is this women in the image provided?",
   "Who is this women in the image provided?"]

#Answer options displayed on screen

options=[
         ['Janet Jackson','Charlotte Webster','Ada Lovelace','Briana Williamson'],['Josephine','Kate','Melinda','GraceHopper',],
         ['HedyLamarr','Rose','Yvonne','Mary'],['Rina','MargaretHamilton','Adel']
        ]
#Order of the actual answers
a=[3,4,1,2]

images=["AdaLoveLace.jpg","GraceHopper.jpg","HedyLamarr.jpg","MargaretHamilton.jpg"]
root = Tk()
root.geometry("800x500")
root.title("Quiz")


#Setting class for the backend of the quiz
class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
##        self.images=images
        self.display_image(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        #Setting up banner displayed on the screen.
        t = Label(root, text="Girls Can Code", width=50, bg="#FFB6C1", fg="black", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):
        #Creating the selection buttons for the user to select. 
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
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
        #display for images on every frame for actual quiz
        pic=ImageTk.PhotoImage(Image.open(images[qn]))
        label= Label(root)
        label.place(x=380, y=150)
        label.config(image=pic)
        label.image=pic
                   
    def buttons(self):
        #Creating the Next and Quit Buttons for user to select during quiz.
        nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="#A3C79A",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="#D13B1B",fg="white", font=("times",16,"bold"))
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
        #Message box which pops up showing the users score
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))



#Calling function
quiz=Quiz()
