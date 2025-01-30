class string: 
    def getString(self):
        self.entity = input("Enter something : ")
    def printString(self):
        print(self.entity + '\n')

word = string()
word.getString()
word.printString()
