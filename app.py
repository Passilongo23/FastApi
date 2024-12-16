from fastapi import FastAPI

app = FastAPI()


@app.get('/Ola')
def Read_root():
    return {'message': 'Olá Mundo'}
