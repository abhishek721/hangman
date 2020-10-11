import random
from time import sleep
word=["python", "program", "applause", "furry"]
picked=random.choice(word)
def parts(tries):
    stages = [     """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """
    ]
    print(stages[tries])

right=["_"]*len(picked)
print("the word contain",len(picked),"letter")
def update():
    for i in right:
        print(i, end=" ")
    print()

def wait():
    for i in range(5):
        print(".", end=" ")
        sleep(.5)
    print()


update()
wrong=[]
parts(len(wrong))

while True:
    print("========================")
    guess=input("enter your choice:")
    if guess in picked:
        index=0
        for i in picked:
            if i==guess:
                right[index]=guess
            index +=1
        update() 


    else:
       
        if guess not in wrong:
                  wrong.append(guess)
                  parts(len(wrong))
        else:
            print("you already guessed")
        print("wrong guesses",wrong)

    if len(wrong)>5:
        print("you loose the game")
        print("i picked:",picked)
        break
        
    if "_" not in right:
        print("you win")
        break
            

				
    
    
