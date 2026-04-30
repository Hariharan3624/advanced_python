class reverse:
    def __init__(self,s=""):
        self.s=s
    def get(self):
        return self.s[::-1]
user = input("enter a word to reverse: ")
reverser = reverse(user)
print(f"reversed string:{reverser.get()}")          