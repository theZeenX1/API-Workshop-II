from fastapi import APIRouter
from fastapi import Request
from config.db import connection
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

user_route = APIRouter()

templates = Jinja2Templates(directory="templates")

db = connection['API_workshop']
Users = db['Users']
Keys = db['API_keys']


@user_route.get('/user/{user_id}', response_class=HTMLResponse)
async def userpage(request:Request, user_id:str):
    user_data = Users.find_one({'email': user_id})
    api_key = "No keys left😓"
    tokens_left = "-"

    key = Keys.find_one({'email': user_id})
    if key:
        tokens_left = key['tokens_left']
        api_key = key['api_key']
    return templates.TemplateResponse("user.html",
                                      {"request": request ,"title": "API-Workshop User",
                                       "fname": user_data['fname'], "lname": user_data['lname'],
                                       "api_key": api_key, 'tokens': tokens_left})
