from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app, endpoint="/metrics")

@app.get('/')
def read_root():
    return {'message': 'Hello World!'}