from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from security.token_verify import verify_token
from fastapi.middleware.cors import CORSMiddleware
from routes.index import userRouter, categoryRouter, subCategoryRouter, productRouter, searchRouter, breadsRouter, addressRouter, orderRouter
from config.db import database, metadata, engine


metadata.create_all(bind=engine)
app = FastAPI()


# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def root(token: str = Depends(verify_token)):
    return {"message": "Bearer token verified!"}


app.include_router(userRouter, dependencies=[Depends(verify_token)])
app.include_router(categoryRouter, dependencies=[Depends(verify_token)])
app.include_router(subCategoryRouter, dependencies=[Depends(verify_token)])
app.include_router(productRouter, dependencies=[Depends(verify_token)])
app.include_router(searchRouter, dependencies=[Depends(verify_token)])
app.include_router(breadsRouter, dependencies=[Depends(verify_token)])
app.include_router(addressRouter, dependencies=[Depends(verify_token)])
app.include_router(orderRouter, dependencies=[Depends(verify_token)])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
