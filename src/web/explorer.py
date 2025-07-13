from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service


router = APIRouter(prefix = '/explorer')


@router.get("/")
async def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
async def get_one(name) -> Explorer:
    return service.get_one(name)


@router.post("/")
async def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)


@router.patch("/")
async def modify(name: str, explorer: Explorer) -> Explorer:
    return service.modify(name, explorer)


@router.delete("/{name}")
async def delete(name: str):
    return service.delete(name)