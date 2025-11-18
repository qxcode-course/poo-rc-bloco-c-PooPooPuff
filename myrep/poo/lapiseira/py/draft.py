class Lead:
    def __init__(self,size:float,thickness:int,hardness:str):
        self.__size:float=size
        self.__thickness:int=thickness
        self.__hardness:str=hardness

    def getthickness(self):
        return self.__thickness
    
class Pencil:
    def __init__(self,thickness:float):
        self.__tip:Lead|None=None
        self.__thickness:float=thickness
        self.barrel:list[Lead]=[]

    def __str__(self)->str:
        tip=f"[{self.__tip}]" if self.__tip else "[]"
        pencilbarrel= "".join([str(x) for x in self.barrel])
        return f"calibre: {self.__thickness}, bico: {tip}, tambor: <{pencilbarrel}>"

    def insert(self,lead:Lead):
        if lead.getthickness()!=self.__thickness:
            print("fail: calibre incompatível")
            return
        else:
            self.barrel.append(lead)

def main():
    pencil=Pencil(0)
    while True:
        line=input()
        print('$'+line)
        args=line.split(" ")
        
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(pencil)
        elif args[0]=="init":
            pencil=Pencil(float(args[1]))
        elif args[0]=="insert":
            size=float(args[1])
            thickness=int(args[3])
            hardness=args[2]
            lead=Lead(size,thickness,hardness)
            pencil.insert(lead)
main()