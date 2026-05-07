class c:
    def __init__(self):
        self.rmap = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    def tr(self,num):
        "computes and returns the roman numeral for a give integer"
        roman_numeral = ""
        for value,symbol in self.rmap:
            while num >= value:
                roman_numeral += symbol
                num-= value
        return roman_numeral
if __name__ == "__main__":
    converter = c()

    try:
        userinput = int(input("enter an interger to convert to roman: "))
        if userinput > 0:
            result = converter.tr(userinput)
            print(f"the roman numeral for {userinput} is: {result}")
        else:
            print("please enter a positive intege greater than 0 ")

    except ValueError:
        print("invalid input")