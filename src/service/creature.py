from model.creature import Creature
import data.creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> Creature:
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def modify(name: str, creature: Creature) -> Creature:
    return data.modify(name, creature)


def delete(name: str):
    return data.delete(name)