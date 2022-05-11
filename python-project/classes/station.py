from asyncio.windows_events import NULL
import json
import re
from tkinter.messagebox import RETRY
from classes.user import User
from classes.slot import Slot

logFile= "logFiles/station_velo.txt"


class Station():
    def __init__(self,id,type,type_velo,Placement,street,number,addition,district,postalcode,objectCode,usage,slotCount,coordinates) -> None:
        self.id=id
        self.stationType=type
        self.velo_typ= type_velo
        self.placement= Placement
        self.street=street
        self.number=number
        self.addition=addition
        self.district=district
        self.postalcode=postalcode
        self.objectcode= objectCode
        self.isInUse= usage
        self.numberOfSlots=slotCount
        self.coordinates=coordinates
        self.slots= []
        self.add_slots()
        self.emptyPlaces= slotCount
        pass

    
    #vult de slot array op op basis van het aantal vrije slots
    def add_slots(self):
        for x in range(self.numberOfSlots):
            self.slots.append(Slot(x))
            
    #loopt over alle slots in het sattion
    #kijkt vervolgens of er een lege slot is
    #als de fiets nog niet teogevoegd is aan een slot, voegt hij de fiets toe
    def add_velo_to_slot(self,velo):
        veloAdded=False
        if(self.emptyPlaces > 0):
            for slot in self.slots:
                if(veloAdded==False):
                    if( slot.add_velo(velo)):
                        veloAdded=True
                        self.emptyPlaces= self.emptyPlaces-1
                        return True
        else:
            print("no empty places left")
            return False
   
    def transporter_getter(self,transporter):
        if(self.emptyPlaces == self.numberOfSlots):
            print("no velos in this station")
            self.log(f"transporter {transporter.firstName} {transporter.lastName} tried to take velos, but station was too empty")
            return NULL
        else:
            velos=[]
            #zorgt ervoor dat er steeds 1 fiets blijft in het station
           
            for slot in self.slots:
                if(slot.is_empty==False):
                    velos.append(slot.velo)
                    slot.remove_velo()
                    self.emptyPlaces+=1
            
            self.log(f"transporter, {transporter.firstName} {transporter.lastName} took {len(velos)} velos from station [{self.id}]")

            return velos

       
    def log(self,message):
       f= open(logFile,"a")
       f.write(f"--------\n{message}\n--------")


    def __str__(self) -> str:
       return f"station [{self.id}]: {self.stationType}, velo type: {self.velo_typ}, placement: {self.placement},street: {self.street}, number: {self.number}, addition: {self.addition}, district: {self.district}, postalcode: {self.postalcode}, objectCode:{self.objectcode}, in use: {self.isInUse}, slot count: {self.numberOfSlots}, coordinates: {self.coordinates}"

    def __print_slots__(self) ->str:
        output= "slots:\n"
        for slot in self.slots:
            output+= slot.__str__() +"\n"    
        return output
    
  
    
       
            

