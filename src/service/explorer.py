from model.explorer import Explorer
import fake.explorer as data


def get_all() -> list[Explorer]:
    return data.get_all()


def get_one(name: str) -> Explorer:
    return data.get_one(name)

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)


def modify(name: str, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)


def delete(name: str):
    return data.delete(name)