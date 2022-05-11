from asyncio.windows_events import NULL
from classes.velo import Velo

logFile= "logFiles/user_velo.txt"

class User():
    def __init__(self,fname,lname,age) -> None:
        self.firstName=fname
        self.lastName= lname
        self.age= age
        self.velo= NULL
        pass

    def get_velo(self,velo):
        if (self.velo==NULL):
            self.velo=velo
            self.log(f"{self.firstName} {self.lastName} took this velo: {self.velo}")

        else:
            print("you can only have 1 velo at a time")

    def remove_velo(self):
        self.velo=NULL
        self.log(f"{self.firstName} {self.lastName} gave his velo back")

    #loopt alle slots af om te kijken of er een fiets is 
    #als er een fiets is , wordt deze toegewezen aan de user en wordt de de fiets verwijderd van het slot
    #retunrt true indien er een fiets ontleent is
    #returnt false indien er geen fiets ontleent kon worden
    def get_velo_from_station(self,station):
        veloTaken=False
        for slot in station.slots:
            if(veloTaken==False):
                if(slot.is_empty == False):
                    self.get_velo(slot.velo)
                    slot.remove_velo()
                    station.log(f"{self.firstName} {self.lastName} took a velo from station [{station.id}]")
                    veloTaken=True
                    station.emptyPlaces= station.emptyPlaces+1
                    return True
        print("geen fiets gevonden")
        return False


    def give_velo_to_station(self,station):
        if(self.velo==NULL):
            print("this user has no velo to give")
            return False
        if(station.emptyPlaces<=0):
            print("no empty places left")
            return False

        if(self.velo != NULL and station.emptyPlaces>0):
            station.add_velo_to_slot(self.velo)
            self.remove_velo()
            station.log(f"{self.firstName} {self.lastName} gave velo to sation [{station.id}]")
            return True


    def __str__(self) -> str:
        if(self.velo==NULL):
            return f"{self.firstName} {self.lastName} [{self.age}] has no velo"
        else:
             return f"{self.firstName} {self.lastName} [{self.age}] has {self.velo}"

    def log(self,message):
       f= open(logFile,"a")
       f.write(f"--------\n{message}\n--------")

    
