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
    
    #def __str__(self):
        
    
#class Theather:
    #def __init__(self,capacity:int):
        #self.__seats:list[]
def main():
    #theather=Theather()
    while True:
        line=input()
        print("$"+line)
        args=line.split(" ")
        
        if args[0]=="end":
            break
        #elif args[0]=="show":
            #print(theather)
main()