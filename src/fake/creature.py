from model.creature import Creature


_creatures = [  
    Creature(name="Yeti",  aka="Abominable Snowman",  country="CN",  area="Himalayas",  description="Hirsute Himalayan"),  
    Creature(name="Bigfoot",  description="Yeti's Cousin Eddie",  country="US",  area="*",  aka="Sasquatch"),  
    ] 


def get_all() -> list[Creature]:
    return _creatures 


def get_one(name: str) -> Creature:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature  
        return _creature

def create(creature: Creature) -> Creature:
    return creature 


def modify(name: str, creature: Creature) -> Creature:
    return creature 


def delete(name: str):
    return None