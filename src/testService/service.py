from fastapi import FastAPI

app = FastAPI()


@app.get("/clasify")
async def root():
    return {"message": "OK"}