from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.db import connection
from models.ChatbotApiModel import ApiBaseModel
from fun.chatbot import createResponse
import json

app_chat_route = APIRouter()
templates = Jinja2Templates(directory="templates")
app_chat_route.mount("/static", StaticFiles(directory="static"), name="static")

db = connection['API_workshop']
Users = db['Users']
Keys = db['API_keys']


@app_chat_route.get('/chat')
async def chatRoute(api_key: str, prompt: str, role: str | None):
    user_db = Keys.find_one({'api_key': api_key})
    if user_db:
        user = user_db['email']
        user = user.strip()

        try:
            tokens_left = user_db['tokens_left']
            if not tokens_left:
                return JSONResponse(content={"error": f"No tokens left for the api_key: {api_key}"}, status_code=404)
            tokens_left -= 1
            if tokens_left <= 0:
                Keys.delete_one({'api_key': api_key})
            else:
                Keys.update_one(filter={'api_key': api_key}, update={'$set': {'tokens_left': tokens_left}})

            content = createResponse(user=user, prompt=prompt, role=role)
            response = {
                'assistant': content,
                'tokens_left': tokens_left
            }
            response = json.dumps(response)
            response = json.loads(response)
            validated_data = ApiBaseModel.model_validate(response)
            validated_data = validated_data.model_dump()

            return JSONResponse(content=validated_data)
        except Exception as e:
            return JSONResponse(content={'error': f'Could not generate a response. Details: {e}'})
    else:
        return JSONResponse(content={"error": f"Couldn't find the api_key: {api_key}"}, status_code=404)
