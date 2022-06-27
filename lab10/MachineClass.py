class MachineClass():
    #States
    def __init__(self):
        self.tape = ""

    def getIndex(self, index):
        print("tape = ", self.tape, "index = ", index)
        return self.tape[index]

    def getTape(self):
        return self.tape

    def setTape(self, tape): 
        self.tape = tape

    def read(self, index):
        needed = self.tape[index]
        self.tape = self.tape[0:index] + self.tape[index:]
        return needed
    
    def addTape(self, elem):
        self.tape += elem

    def printTape(self):
        print(f"Tape:\n{self.tape}")