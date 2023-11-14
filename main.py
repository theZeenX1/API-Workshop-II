from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.db import connection
from Routes.apiFacts import app_fact_route
from Routes.apiChatbot import app_chat_route
from Routes.userPage import user_route
from Routes.submitFrom import submit_form_route

# import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")

db = connection['API_workshop']
Users = db['Users']
Keys = db['API_keys']


@app.get('/', response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "API-Workshop HomePage"})


app.include_router(app_fact_route)
app.include_router(app_chat_route)
app.include_router(user_route)
app.include_router(submit_form_route)

