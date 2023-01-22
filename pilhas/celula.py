class Celula:
    def __init__(self, dado):
        self.dado = dado
        self.proxima = None 
    
    def __repr__(self) -> str:
        return f'{self.dado}'