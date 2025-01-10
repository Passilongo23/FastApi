from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from sqlalchemy import  create_engine, select
from sqlalchemy.orm import Session

from fast_zero import User
from fast_zero.Schemas import Message, UserDB, UserList, UserPublic, UserSchema
from fast_zero.settings import Settings
app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def Read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    engine = create_engine(Settings().DATABASE_URL)
    with Session (engine) as session:
        db_user = session.scalar(
            select(User).where(User.username == user)
        )
        if db_user:
            return 'Usuario já existente'

@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User Not Found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User Not Found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}
