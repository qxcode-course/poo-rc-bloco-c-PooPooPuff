class Lead:
    def __init__(self,size:float):
        self.__size:float=0
        self.__thickness:int
        
class Pencil:
    def __init__(self,thickness:int):
        self.__tip:Lead|None=None
        self.__thickness:int=thickness

    def __str__(self)->str:
        return f"calibre: {self.__size}"

    def haslead(self)->bool:
        if self.__tip is None:
            print("fail: nao existe grafite")
            return
        else:
            return self.__tip 
        
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
            
main()