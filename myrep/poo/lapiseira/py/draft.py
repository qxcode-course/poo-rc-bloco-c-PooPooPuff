class Lead:
    def __init__(self,thickness:float,hardness:str,size:int):
        self.__size:int=size
        self.__thickness:float=thickness
        self.__hardness:str=hardness

    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"

    def getthickness(self):
        return self.__thickness
    
    def gethardness(self):
        return self.__hardness
    
    def getsize(self):
        return self.__size
    
    #def desgaste(self):
        #self.__size-=
class Pencil:
    def __init__(self,thickness:float):
        self.__tip:Lead|None=None
        self.__thickness:float=thickness
        self.barrel:list[Lead]=[]

    def __str__(self)->str:
        tip=f"{self.__tip}" if self.__tip else "[]"
        pencilbarrel= "".join([str(x) for x in self.barrel])
        return f"calibre: {self.__thickness}, bico: {tip}, tambor: <{pencilbarrel}>"

    def insert(self,lead:Lead):
        if lead.getthickness()!=self.__thickness:
            print("fail: calibre incompatível")
            return
        else:
            self.barrel.append(lead)

    def pull(self):
        if self.__tip is not None:
            print("fail: ja existe grafite no bico")
            return
        self.__tip=self.barrel[0]
        del self.barrel[0]
        
    def remove(self):
        self.__tip=None

    def write(self):
        if not self.__tip:
            print("fail: nao existe grafite no bico")
            return
        
        hardness=self.__tip.gethardness()
        
        if hardness=="HB":
            desgaste=1
        elif hardness=="2B":
            desgaste=2
        elif hardness=="4B":
            desgaste=4
        elif hardness=="6B":
            desgaste=6
            
        size=self.__tip.getsize()
        
        if size<=10:
            print("fail: tamanho insuficiente")
            return
        if size-desgaste<10:
            print("fail: folha incompleta")
            self._Pencil__tip._Lead__size=10
            return
        #Caralho isso daqui é genial V, adorei a descoberta
        self._Pencil__tip._Lead__size-=desgaste
        
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
            thickness=float(args[1])
            size=int(args[3])
            hardness=args[2]
            lead=Lead(thickness,hardness,size)
            pencil.insert(lead)
        elif args[0]=="pull":
            pencil.pull()
        elif args[0]=="remove":
            pencil.remove()
        elif args[0]=="write":
            pencil.write()
main()