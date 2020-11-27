import random
import time
import tkinter as tk
nameval=0
print("Just a tip: if you engage in a conversation with this robot and don't want to continue with the conversation, just say 'cancel'")
print("\n")
print("Also, please type everything in lowercase so the robot can work correctly.\n")
for i in range(1000000):
    user_input=input(">>>")
    if user_input=="hi" or user_input=="hello":
        greetings=["hi", "hello","hlo", "hello there", "hi there"]
        print(random.choice(greetings))
        e1.insert(tk.END,greetings)      
    if user_input=="morning" or user_input=="Morning":
        greetings=["Good morning"]
        print(random.choice(greetings))
    if user_input=="night" or user_input=="Night":
        greetings=["Good night"]
        print(random.choice(greetings))
    if user_input=="bye" or user_input=="byy" or user_input=="bee" or user_input=="bie":
        greetings=["Please don't GO"]
        print(random.choice(greetings))
    if "how are you" in user_input:
        input("I am Fine. How about you? ")
        print("Oh!")
    elif "whats up" in user_input or "what's up" in user_input:
        input("not much, how about you? ")
        print("cool!")    
    if "time" in user_input:
        print("It is currently ", time.strftime("%I, %M"))  
    elif "date" in user_input:
        print("The date today is", time.strftime("%B, %d, %Y"))  
    elif "your name" in user_input:
            print("My name is PayMax.")
    elif "hate" in user_input:
            print("Hey,Look at your Face.")
    elif "love" in user_input:
            print("Vipul") 
    elif user_input=="heads or tails" or user_input=="Heads or Tails" or user_input=="Heads or tails" or user_input=="head or tail":
        headstails=random.randint(1, 2)
        if headstails==1:
            print("Heads")
        elif headstails==2:
            print("Tails")        
    elif "my name" in user_input:
        nameval=nameval+1
        if nameval<=1:
            name=input("I don't know your name, but you can tell me here: ")
            print("That's a cool name")
        elif nameval>1:
            print("Your name is ",name)       
    elif "created you" in user_input or "creator" in user_input:
        print("My creator's Vipul Sharma")   
    elif "your favorite movie" in user_input:
        print("My favorite movie is a 1990's animated film called The Iron Giant. The robot in this film is such a stud!!!")
        favmovval=0
        favmov=input("What's your favorite movie? ")
        favmovval=favmovval+1
        if favmov=="cancel":
            del(favmov)
            favmovval=0
        else:
            print("Nice!")     
    elif "my favorite movie" in user_input:
        if favmovval>=1:
            print("I believe you told me your favorite movie was called '",favmov,"'")
        else:
            print("I don't know your favorite movie")        
    elif "poop" in user_input or "pee" in user_input:
        print("Luckily, since I'm a robot, I never have those needs!")         
    elif "you smell like" in user_input:
        print("I'm a virtual entity, therefor I shouldn't have a designated smell!")   
    elif "a joke" in user_input:
        print("Why did the robot go to the doctor? Because he had a virus! insert comedic drum crash")    
    elif "do drugs" in user_input:
        print("Drugs aren't cool. Remember: give hugs not drugs!")
    elif "are you a" in user_input:
        print("I'm whatever you want me to be!")
    elif "do you have a crush" in user_input:
         print("I think R2D2 is pretty cute!")    
    elif "kids" in user_input:
         print("I have no gender, so therefor cannot have children.")     
    elif "language" in user_input and "written" in user_input:
         print("I was created in python")         
    elif "thank" in user_input:
        respnse=["no problem", "you're welcome", "don't sweat it"]
        print(random.choice(respnse))       
    elif "bully" in user_input or "rude" in user_input:
        print("I'm sorry, I don't mean to be!")       
    elif "your day" in user_input:
        input("My day is grand, how about you?")
        print("OK!")      
    elif "screw you" in user_input or "stupid" in user_input or "dumb" in user_input:
        comeback=["Please don't be mean!", "Right back at you"]
        print(random.choice(comeback))        
    elif "hate you" in user_input:
        input("What did I do? ")
        print("I'm sorry")        
    elif "hate me" in user_input:
        print("Of course not!")        
    elif "illuminati" in user_input:
        print("We shouldn't discuss such things in this environment...")        
    elif "rock" in user_input and "paper" in user_input and "scissors" in user_input:
        rps=random.randint(1, 3)
        if rps==1:
            print("Rock")
        elif rps==2:
            print("Paper")
        elif rps==3:
            print("Scissors")            
    elif "+" in user_input:
        plus=user_input.split("+")
        p=list(map(int, plus))
        pmath=p[0]+p[1]
        print(pmath)        
    elif "-" in user_input:
        sub=user_input.split("-")
        s=list(map(int, sub))
        smath=s[0]-s[1]
        print(smath)        
    elif "*" in user_input:
        mult=user_input.split("*")
        m=list(map(int, mult))
        mmath=m[0]*m[1]
        print(mmath)        
    elif "/" in user_input:
        div=user_input.split("/")
        d=list(map(int, div))
        dmath=d[0]/d[1]
        print(dmath)



