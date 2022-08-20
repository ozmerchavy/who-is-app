from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os.path

app = FastAPI()


def read(filename):
    if not os.path.isfile(filename):
        return "FILE DOES NOT EXIST"
    with open(filename, 'r') as f:
        res = f.read()
    return res


@app.get("/who-is-online")
async def api():
    return read(f'{os.path.dirname(__file__)}/../logs/who-is-online.txt')


@app.get("/delta-history")
async def api():
    return read(f'{os.path.dirname(__file__)}/../logs/delta-history.txt')


app.mount("/", StaticFiles(directory=f"{os.path.dirname(__file__)}/../client", html=True), name="client")


def start_server():
    uvicorn.run("server:app", port=5001, reload=True, access_log=False)

if __name__ == '__main__':
    start_server()