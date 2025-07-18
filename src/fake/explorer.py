from model.explorer import Explorer


_explorers = [
    Explorer(name="Claude Hande",  country="FR",  description="Scarce during full moons"),  
    Explorer(name="Noah Weiser",  country="DE",  description="Myopic machete man"),  
]

def get_all() -> list [Explorer]:
    return _explorers


def get_one(name: str) -> Explorer:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer  
    return _explorers


def create(explorer: Explorer) -> Explorer:
    return explorer 


def modify(name:str, explorer: Explorer) -> Explorer:
    return explorer 


def delete(name: str):
    return None

