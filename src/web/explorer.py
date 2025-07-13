from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
import service.explorer as service
from error import Duplicate, Missing


router = APIRouter(prefix = '/explorer')

@router.get("")
@router.get("/")
async def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
async def get_one(name) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("")
@router.post("/")
async def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.patch("/")
async def modify(name: str, explorer: Explorer) -> Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.delete("/{name}")
async def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
