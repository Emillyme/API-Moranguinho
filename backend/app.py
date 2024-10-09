from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/get_data')
async def get_data():
    return {'body': 'Rendereizar esse texto'}

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
