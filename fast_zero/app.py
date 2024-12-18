from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.Schemas import Message, UserDB, UserPublic, UserSchema, UserList

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def Read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get('/users', response_model=UserList)
def read_users():
    return {'users': database}
