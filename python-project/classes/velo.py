class Velo():
    def  __init__(self,model,id) -> None:
        self.name=model
        self.id=id
        pass

    def __str__(self) -> str:
        return f"fiets [{self.id}]: {self.name}"