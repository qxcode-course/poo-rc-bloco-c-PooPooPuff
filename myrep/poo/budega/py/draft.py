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
    def __init__(self,counters_num:int=0):
        self.__counters:list[Person|None]=[]
        self.queue:list[Person]=[]
        for i in range(counters_num):
            self.__counters.append(None)

    def __str__(self):
        slots=", ".join([str(x) if x else "-----" for x in self.__counters])
        queue=", ".join([str(x) for x in self.queue])
        return f"Caixas: [{slots}]\nEspera: [{queue}]"
    
    def arrive(self,person:Person):
        self.queue.append(person)

def main():
    market=Market(0)
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
        elif args[0]=="arrive":
            market.arrive(str(args[1]))


main()