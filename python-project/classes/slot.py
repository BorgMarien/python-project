from asyncio.windows_events import NULL
from classes.velo import Velo


class Slot():
    def __init__(self,id) -> None:
        self.id=id
        self.is_empty= True
        self.velo= NULL
        pass

    def add_velo(self,velo):
        if(self.is_empty):
            self.velo= velo
            self.is_empty=False
            return True
        else:
            #print("slot is occupied, try a different slot")
            return False
    def remove_velo(self):
        self.velo=NULL
        self.is_empty=True  
    def __str__(self) -> str:
        if(self.is_empty):
            return "slot [empty]"
        else:
            return f"slot [{self.velo}]"
    


    