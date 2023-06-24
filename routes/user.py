from fastapi import APIRouter, Response, status
from uuid import uuid1
from config.db import database
from models.index import userModal
from schemas.index import user, userInput, userUpdateInput
from sqlalchemy import text
userRouter = APIRouter()


async def getUserByEmailFunction(email):
    query = userModal.select().where(userModal.c.email == email)
    res = await database.fetch_all(query)
    return res


async def getUserByIdFunction(id):
    query = userModal.select().where(userModal.c.id == id)
    res = await database.fetch_all(query)
    return res


@userRouter.post("/newUser", response_model=None)
async def newUser(request: userInput, response: Response):

    existingUser = await getUserByEmailFunction(request.email)
    if len(existingUser) > 0:
        return {"msg": "user already exists", "status": 202}
    userId = str(uuid1())
    query = userModal.insert().values(
        id=userId,
        name=request.name,
        email=request.email,
        password=request.password,
        is_verified=True,
        pet_age=request.pet_age,
        pet_bread=request.pet_bread
    )
    await database.execute(query)
    return {"status": 201, "msg": "user created", "data": {"id": userId, **request.dict()}}


@userRouter.get('/getUserByEmail', response_model=None)
async def getUserByEmail(userEmail: str):
    existingUser = await getUserByEmailFunction(userEmail)
    if len(existingUser) > 0:
        return {"msg": "user already exists", "status": 202}
    return {"msg": "user not found", "status": 204}


@userRouter.get('/getUserByEmailAndPassword', response_model=None)
async def getUserByEmailAndPassword(userEmail: str, password: str):
    query = text(
        f'''
        SELECT * FROM users WHERE email='{userEmail}' AND password='{password}'
        '''
    )
    existingUser = await database.fetch_all(query)
    if len(existingUser) > 0:
        return {"msg": "user exists", "status": 200, "data": existingUser}
    return {"msg": "user not found", "status": 204}


@userRouter.put("/updateUser", response_model=None)
async def updateUser(userId: str, userInput: userUpdateInput, response: Response):
    existingUser = await getUserByIdFunction(userId)
    if len(existingUser) > 0:
        query = userModal.update().values(
            name=userInput.name
        )
        await database.execute(query)
        return {"msg": "user updated successfully", "status": 200}
    return {"msg": "user not found", "status": 204}
