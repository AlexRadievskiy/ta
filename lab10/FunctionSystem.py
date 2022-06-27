from MachineClass import MachineClass

class FunctionSystem:
    def __init__(self):
        self.machine = MachineClass()
        self.result = ""

    def inputX(self):
        x = input("Input an x(in binary)-> ")
        return x.strip()

    def inputY(self):
        y = input("Input an y(in binary)-> ")
        return y.strip()

    def compareXandY(self):
        x0 = None
        y0 = None

        for i in range(0, len(self.machine.getTape())):
            self.machine.printTape()
            print("i = ", i)
            if len(self.machine.getTape()) == 1: 
                break
            if i == 0:
                x0 = self.machine.read(0)
                y0 = None
            if self.machine.getTape()[i] == " ":
                y0 = self.machine.read(i + 1)
            if y0 != None:
                i = -1
                if x0 != y0:
                    if x0 > y0:
                        return "reject"
                    else:
                        return "accept"
        return "accept"

    def multiply(self):
        x0 = None
        y0 = None
        multiplies = []
        tmp = ""

        for i in range(len(self.machine.getTape()) - 1, self.machine.getTape().index(" "), -1):
            y0 = self.machine.getIndex(i)
            for j in range(self.machine.getTape().index(" ") - 1, -1, -1):
                x0 = self.machine.getIndex(j)
                if x0 == "1" and y0 == "1":
                    tmp += "1"
                else: 
                    tmp += "0"

            for k in range(1, len(self.machine.getTape()) - i + 2):
                tmp += "0"
            for k in range(1, i - self.machine.getTape().index(" ")):
                self.result = "0" + self.result
            multiplies.append(tmp)
            tmp = ""

        print("multiplies:")
        for s in multiplies:
            print(s)

        self.result = multiplies[0]
        for j in range(1, len(multiplies) + 1):
            inMind = None
            for i in range(len(multiplies[j]) - 1, -1, -1):
                if self.result[i] == "1" and multiplies[j][i] == "1":
                    if inMind != None:
                        result_list = list(self.result)
                        result_list[i] = "1"
                        self.result = "".join(result_list)
                    else: 
                        result_list = list(self.result)
                        result_list[i] = "0"
                        self.result = "".join(result_list)
                        inMind = "1"
                if self.result[i] == "0" and multiplies[j][i] == "0":
                    if inMind != None:
                        result_list = list(self.result)
                        result_list[i] = "1"
                        self.result = "".join(result_list)
                        inMind = None
                    else:  
                        result_list = list(self.result)
                        result_list[i] = "0"
                        self.result = "".join(result_list)
                else: 
                    if inMind != None:
                        result_list = list(self.result)
                        result_list[i] = "0"
                        self.result = "".join(result_list)
                    else: 
                        result_list = list(self.result)
                        result_list[i] = "1"
                        self.result = "".join(result_list)
            
            if inMind != None:
                self.result = inMind + self.result
        
        return self.result
    
    def plusXY(self):
        x0 = None
        y0 = None

        self.result = ""
        inMind = None
        for i in range(0, len(self.machine.getTape())):
            if len(self.machine.getTape()) == 1:
                break
            if self.machine.getIndex(i) == " ":
                i -= 1
                x0 = self.machine.read(i)
            if len(self.machine.getTape()) - 1 == i:
                y0 = self.machine.read(i)
                i = -1
                plus = None

                if x0 == "1" and y0 == "1":
                    if inMind != None: 
                        plus = "1"
                    else: 
                        plus = "0"
                        inMind = "1"
                    inMind = "1"
                
                elif x0 == "0" and y0 == "0":
                    if inMind != None:
                        plus = "1"
                        inMind = None
                    else: 
                        plus = "0"
                    
                else: 
                    if inMind != None:
                        plus = "0"
                    else: 
                        plus = "1"
                    
                self.result = plus + self.result
        
        if inMind != None:
            self.result = inMind + self.result
        return self.result
    
    def main(self):
        x = self.inputX()
        y = self.inputY()

        if len(x) < len(y):
            difference = len(y) - len(x)
            for i in range(0, difference):
                x_list = list(x)
                x_list[0] = "0"
                x = "".join(x_list)
            
        if len(x) > len(y):
            difference = len(x) - len(y)
            for i in range(0, difference):
                y = "0" + y

        self.machine.addTape(str(x))
        self.machine.addTape(" ")
        self.machine.addTape(str(y))

        if self.compareXandY() == ("accept"):
            print("x <= y. Multiplying has begun...")
            self.machine.printTape()
            self.machine.setTape("")
            self.machine.addTape(str(x))
            self.machine.addTape(" ")
            self.machine.addTape(str(y))
            self.machine.addTape(" " + self.multiply())
            self.machine.printTape()
        else: 
            print("x > y. Adding has begun...")
            self.machine.setTape("")
            self.machine.addTape(str(x))
            self.machine.addTape(" ")
            self.machine.addTape(str(y))
            addition = self.plusXY()
            self.machine.setTape("")
            self.machine.addTape(str(x))
            self.machine.addTape(" ")
            self.machine.addTape(str(y))
            self.machine.addTape(" " + addition + "1")
            self.machine.printTape()