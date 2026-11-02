from argon2 import PasswordHasher
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .routers import auth, post, user, vote

pwd_context = PasswordHasher()

# esto es lo que crea las tablas de postgress pero como lo estamos haciendo con alembic lo vamos a dejar comentado
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello world"}
