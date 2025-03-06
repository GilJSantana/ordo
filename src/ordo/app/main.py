from fastapi import FastAPI

app = FastAPI(title='Ordo API', version='0.0.1')

@app.get('/')
def read_root():
    return {'message': 'Ordo API em contrução!'}