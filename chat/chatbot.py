import pyttsx3
import random
from knowledge import CHATBOT_KNOWLEDGE_BASE

engine = pyttsx3.init()

def speak (text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

while True: 
    ''
    try:    
        print("--------------------------------")
        print("hello, how are you, what is your name, bye, what is a variable, what are data types, what is an integer, what is a string, how to get user input, how to print output, what is an operator, comparison operators, logical operators, what is if else, what is elif, what is a loop, for loop vs while loop, how to stop a loop, what is a list, how to add to a list, what is a dictionary, how to access dictionary, what is a tuple, what is a function, how to define a function, what is a return statement, what is file io, how to open a file, explain try except, what is a value error")
        print("---------------------------------")

        user = input("USER : Entre the question needed for assistance ? \n").lower().strip()
        
        if user in CHATBOT_KNOWLEDGE_BASE:
            responce_list = CHATBOT_KNOWLEDGE_BASE[user]
            responce = random.choice(responce_list)
            print(f"Chatbot: {responce}")
            speak(responce)

        elif user == 'exit' or 'Exit':
            
            a=("""Thank You So Much, Shashank Shukla ji \n Come Back Again Soon.... """)
            print(a)
            speak(a)
            break
        # else:
        #     if user not in CHATBOT_KNOWLEDGE_BASE:
                 
    except ValueError as e:
        print('ValueError: Database is small,Pick right questio? ')