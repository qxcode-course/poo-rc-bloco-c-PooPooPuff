class Client:
    def __init__(self,id:str,phone:int):
        self.__id:str=id
        self.__phone:int=phone
        
    def getid(self):
        return self.__id
    
    def getphone(self):
        return self.__phone
    
    def setid(self,id:str):
        self.__id=id
    
    def setphone(self,phone:int):
        self.__phone=phone
    
    def __str__(self):
        return f"{self.__id}:{self.__phone}"
    
class Theather:
    def __init__(self,capacity:int):
        self.__seats:list[Client|None]=[None]*capacity
        
    def __str__(self):
        return "["+" ".join([str(x) if x else "-" for x in self.__seats])+"]"
    
def main():
    theather=Theather(0)
    while True:
        line=input()
        print("$"+line)
        args=line.split(" ")
        
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(theather)
        elif args[0]=="init":
            capacity=int(args[1])
            theather=Theather(capacity)
main()