from fastapi import FastAPI
from web import explorer, creature
import uvicorn

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)