from fastapi import FastAPI
from app.api.endpoints import users, posts

app = FastAPI(title="Testify", version="1.0.0")

# Register Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])

@app.get("/")
def root():
    return {"message": "Welcome to Testify"}