from tkinter import *
from PIL import Image,ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")
root.geometry("900x250")

# Pictures
img = Image.open("rock-user.png")
img = img.resize((120,120))
img2 = Image.open("paper-user.png")
img2 = img2.resize((120,120))
img3 = Image.open("scissor-user.png")
img3 = img3.resize((120,120))
img4 = Image.open("rock.png")
img4 = img4.resize((120,120))
img5 = Image.open("paper.png")
img5 = img5.resize((120,120))
img6 = Image.open("scissor.png")
img6 = img6.resize((120,120))

rock_img = ImageTk.PhotoImage(img)
paper_img = ImageTk.PhotoImage(img2)
scissor_img = ImageTk.PhotoImage(img3)
rock_img_comp = ImageTk.PhotoImage(img4)
paper_img_comp = ImageTk.PhotoImage(img5)
scissor_img_comp = ImageTk.PhotoImage(img6)

# Insert picture
user_label = Label(root, image=scissor_img,bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

# Scores
playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

# Indicators
user_indicator = Label(root,font=50,text="USER")
comp_indicator = Label(root,font=50,text="COMPUTER")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

# Message
msg = Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

# Update message
def updateMessage(x):
    msg['text'] = x

# Update user score
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

# Update computer score
def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)

# Check winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("Its a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You losse")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    else:
        pass

# Update choices
choices = ["rock","paper","scissor"]
def updateChoice(x):

# For computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

# For user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)

# Buttons
rock = Button(root,width=20,height=2,text="ROCK",fg="#00008B",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",fg="#00008B",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",fg="#00008B",command=lambda:updateChoice("scissor")).grid(row=2,column=3)


root.mainloop()