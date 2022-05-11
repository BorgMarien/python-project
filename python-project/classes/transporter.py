from cmath import log
from classes.user import User

logFile= "logFiles/user_velo.txt"

class Transporter(User):
    def __init__(self, fname, lname, age,responsibleStations) -> None:
        super().__init__(fname, lname, age)
        self.responisbleStations=responsibleStations
        self.velos=[]

    #laat 1 fiets staan in het station en proeberd de andere fietsen te verdelen
    def disperse_Velos(self,Fullstation):
        self.velos = Fullstation.transporter_getter(self)
    
        #hij blijft elk station 1 fiets geven tot hij mistens 1 keer geprobeerd heeft om al zijn feitsen kwijt te geraken
        lookForMoreStations=True
        while (lookForMoreStations and len(self.velos)>0):
            for station in self.responisbleStations:        
                if(station.emptyPlaces>0 and len(self.velos)>0):
                    if(station.add_velo_to_slot(self.velos.pop())):
                        station.log(f"transporter {self.firstName} {self.lastName} gave a velo to station [{station.id}]")
                        added=True
            if(added==False):
              lookForMoreStations=False    
        return True            



    def __str__(self) -> str:
        if(len(self.responisbleStations)>0):
            output= f"transporteur {self.firstName} {self.lastName} [{self.age}] heeft volgende stations als verantwoordelijkheid:\n"
            for station in self.responisbleStations:
                output+=f"station [{station.id}]\n"
        else:
            output= f"transporteur {self.firstName} {self.lastName} [{self.age}] heeft geen verantwoordelijke stations"

        
        return output
                    


def log(message):
       f= open(logFile,"a")
       f.write(f"--------\n{message}\n--------")
