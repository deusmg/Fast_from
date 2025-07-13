from fastapi import APIRouter
from model.creature import Creature
import service.creature as service


router = APIRouter(prefix = '/creature')


@router.get("/")
async def get_all() -> list[Creature]:
    return service.get_all()


@router.get("/{name}")
async def get_one(name: str) -> Creature| None:
    return service.get_one(name)


@router.post("/")
async def create(creature: Creature) -> Creature:
    return service.create(creature)


@router.patch("/{name}")
async def modify(name:str, creature: Creature) -> Creature:
    return service.modify(name, creature)


@router.put("/")
async def replace(explorer: Creature) -> Creature:
    return service.replace(explorer)


@router.delete("/{name}")
async def delete(name: str):
    return service.delete(name)