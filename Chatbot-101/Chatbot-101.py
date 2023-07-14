# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:56:56 2023
Chatbot Application
"""
#Importing librabries
from tkinter import *
import nltk
from nltk.chat.util import Chat, reflections

# Initialize the Tkinter GUI
root = Tk()
root.title("Chatbot")

# Function to send the user's message and generate bot's response
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    user = e.get().lower()

    # Define the chatbot responses based on user input
    if user == "hello":
        txt.insert(END, "\n" + "Bot -> Hi")
    elif user == "hi" or user == "hii" or user == "hiiii":
        txt.insert(END, "\n" + "Bot -> Hello")
    elif e.get() == "how are you":
        txt.insert(END, "\n" + "Bot -> Fine! And you?")
    elif user == "fine" or user == "i am good" or user == "i am doing good":
        txt.insert(END, "\n" + "Bot -> Great! How can I help you?")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand.")
    e.delete(0, END)

# Create the chat window
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)

# Create the message input field
e = Entry(root, width=100)
e.grid(row=1, column=0)

# Create the send button
send = Button(root, text="Send", command=send).grid(row=1, column=1)

# Start the main event loop
root.mainloop()

# Reflections for chatbot responses
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by MasterYou. You can call me crazy!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you?"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that. How can I help you?"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program. Seriously, you are asking me this?"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse"]
    ],
    [
        r"(.*) created ?",
        ["Nitesh created me using Python's NLTK library", "Top secret ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        ["Indore, Madhya Pradesh"]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot here in %1", "Too cold here in %1", "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company. I have heard about it, but they are in huge loss these days."]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn, it's raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy"]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football"]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messi", "Ronaldo", "Rooney"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Analytics Vidhya has many great articles with step-by-step explanations along with code. You can explore them."]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
]

# Function to initiate the conversation with the chatbot
def chat():
    print("Hi! I am a chatbot created by MasterYou for your service")
    chat = Chat(pairs, reflections)
    chat.converse()

# Initiate the conversation
if __name__ == "__main__":
    chat()
