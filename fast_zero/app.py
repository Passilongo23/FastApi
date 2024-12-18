from http import HTTPStatus

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

from fast_zero.Schemas import Message

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def Read_root():
    return {'message': 'Olá Mundo!'}

@app.get('/testehtml', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def Read_root():
    return  """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""