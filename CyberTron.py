from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

#voice of the bot
engine=pp.init()

voices=engine.getProperty('voices')
print(voices)

engine.setProperty("voice", voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

#This is the Bot's Name
bot=ChatBot("CyberTron")

#These are the conversations
convo=["hi",
       "hello",
       "good morning",
       "Good Morning!, What is your name?",
       "harshal",
       "Oh! hey! Krishna told me about you, you're his best friend right?",
       "yes",
       "Nice to meet you",
       "thankyou",
       "My pleasure",
       "what is your age?",
       "I'm Immortal, I don't have an age",
       "Krishna",
       "Greetings, My master Krishna ",
       "goodnight",
       "Good Night!, sweet dreams",
       "who created you?",
       "Krishna Created me",
       "what is your name?",
       "My Name is CyberTron",
       "how are you?",
       "I'm always happy, just like krishna Programmed me, And how are you?",
       "I'm fine",
       "Good, By the way, You can talk to me whenever you want, I love talking",
       "ok",
       "kay",
       "where do you live?",
       "I live in electricity ",
       "bye",
       "Okay bye, see you!, Take care and stay safe",
       "cybertron say hello to my sir and class friends",
       "Hello! Krishna's sir, Krishna told me that you taught him python very well, Thank you from him sir!, and hello to his class friends",
       "cybertron who is vishwaraj?",
       "Vishwaraj is Krishna's brother, and he will be the greatest footballer",
       "cybertron who is aryan?",
       "Aryan is Krishna's brother, and he is a pro in free fire",
       "cybertron who is kuki?",
       "Kuki is Krishna's sister, and she will a great doctor one day",
       "cybertron who is archana?",
       "Archana Aunty is Krishna's Mom, And Krishna told me that his mom is the best person",
       "cybertron who is rahul?",
       "Rahul Uncle is Krishna's father, and Krishna told me that his father is the best person",
       "cybertron who is tittu?",
       "Tittu is Krishna's brother, and Krishna told me that tittu is the boss of gaming",
       "cybertron who is atul",
       "Atul uncle is Krishna's Uncle, and Krishna told me that his uncle is the best",
       "cybertron who is sandhya?",
       "Sandhya aunty is Krishna's Aunt, and Krishna told me that his aunt is the best",
       "cybertron who is tanu?",
       "Tanu is Krishna's sister",
       "cybertron who is ayush?",
       "Ayush is Krishna's neighbourhood friend",
       "cybertron who is soham?",
       "Soham is Krishna's Best friend",
       "cybertron who is harshal?",
       "Harshal is Krishna's Best friend, And Krishna told me that Harshal is a yz",
       "cybertron who is kedar?",
       "Kedar is Krishna's Best friend",
       ]

#Training The Bot
trainer = ListTrainer(bot)
trainer.train(convo)

#Gui
main = Tk()
main.geometry("500x650")
main.title("CyberTron")
img = PhotoImage(file="1.png")
photoL=Label(main, image=img )
photoL.pack(pady=5)

def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"You : " + query)
    msgs.insert(END, "CyberTron : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

#the Messaging Area
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20, bg="light blue", yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

#User Input Field
textF=Entry(main,font=("Verdana",20), bg="Light blue")
textF.pack(fill=X, pady=10)
btn=Button(main,text="Ask the bot", font=("Verdana",20), command=ask_from_bot, bg="Light blue")
btn.pack()

def enter(event):
    btn.invoke()
main.bind("<Return>", enter)

main.mainloop()