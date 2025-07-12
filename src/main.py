from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def top():
    return "Top here!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)