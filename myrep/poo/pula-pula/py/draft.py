class Kids:
    def __init__(self, name:str,age:int):
        self.__name=name
        self.__age=age
        
    def __str__(self):
        return f"{self.__name}:{self.__age}"
    
    def getage(self):
        return self.__age
    
    def getname(self):
        return self.__name

class Trampoline:
    def __init__(self):
        self.__waiting:list[Kids]=[]
        self.__playing:list[Kids]=[]
        
    def __str__(self):
        waiting=", ".join([str(x) for x in self.__waiting[::-1]])
        playing=", ".join([str(x) for x in self.__playing])
        return f"[{waiting}] => [{playing}]"
    
    def arrive(self,kids:Kids):
        self.__waiting.append(kids)
        
    def enter(self):
        kids=self.__waiting[0]
        self.__playing.append(kids)
        del self.__waiting[0]
    
def main():
    trampoline=Trampoline()
    while True:
        line=input()
        print("$"+line)
        args=line.split(" ")
        
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(trampoline)
        elif args[0]=="arrive":
            name:str=str(args[1])
            age:int=int(args[2])
            trampoline.arrive(Kids(name,age))
        elif args[0]=="enter":
            trampoline.enter()
main()