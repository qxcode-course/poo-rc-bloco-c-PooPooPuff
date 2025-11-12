class Person:
    def __init__(self,name:str):
        self.__name=name

    def getname(self):
        return self.__name

    def setname(self,name:str)->None:
        self.__name=name

    def __str__(self):
        return f"{Person.getname}"

class Market:
    def __init__(self,counters_num:int):
        self.__counters:list[Person|None]=[]
        self.queue:list[Person]=[]

    def __str__(self):
        slot=", "
        queue=", "
        return f"Caixas: "

def main():
    market=Market("")
    while True:
        line=input()
        print("$"+line)
        args=line.split()

        if args[0]=="end":
            break
        elif args[0]=="show":
            print(market)
        elif args[0]=="init":
            market=Market(int(args[1])) 

main()