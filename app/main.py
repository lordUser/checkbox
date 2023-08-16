from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import  user, auth,invoice,product


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(invoice.router)



@app.get("/")
def root():
    return {"message": "Hello World pushing out",
            "hi":"Hello"}
