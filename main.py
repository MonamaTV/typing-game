from fastapi import FastAPI
app = FastAPI()

from users.user_auth import router

app.include_router(router)

@app.get("/")
def get_some_results():
    return "Results"