import random
class fruitquiz:
    def __init__(self):
        self.fruits={"apple":"red",
                     "orange":"orange",
                     "watermelon":"green",
                     "banana":"yellow"}
    def quiz(self):
        while(True):
            fruit,color =random.choice(list(self.fruits.items()))
            print("what is the color of{}".format(fruit))
            user=input()
            if(user.lower()==color):
                print("correct answer")
            else:
                print("wroung answer")
            option = int(input("enter 0, if you want to play again otherwise enter 1:"))
            if (option):
                break
print("welcome to fruit quiz")
fq = fruitquiz()
fq.quiz()