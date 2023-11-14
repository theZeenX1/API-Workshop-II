from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.FactsApiModel import ApiBaseModel
from config.db import connection
from fun.facts import fun
import json


app_fact_route = APIRouter()
templates = Jinja2Templates(directory="templates")
app_fact_route.mount("/static", StaticFiles(directory="static"), name="static")


db = connection['API_workshop']
Users = db['Users']
Keys = db['API_keys']


@app_fact_route.get('/facts')
async def apiRoute(query: str, api_key: str):
    user = Keys.find_one(filter={'api_key': api_key})
    if user:
        try:
            tokens_left = user['tokens_left']
            tokens_left -= 1
            if not tokens_left:
                Keys.delete_one({'api_key': api_key})
            else:
                Keys.update_one(filter={'api_key': api_key}, update={'$set': {'tokens_left': tokens_left}})
            response = {
                "fact": fun(query),
                "tokens_left": tokens_left
            }
            response = json.dumps(response)
            response = json.loads(response)
            validated_data = ApiBaseModel.model_validate(response)
            validated_data = validated_data.model_dump()

            return JSONResponse(content=validated_data)
        except ValueError as e:
            return JSONResponse(content={"error": f"Data Validation Failed {e}"})
    else:
        return JSONResponse(content={"error": f"Couldn't find the api_key: {api_key}"}, status_code=404)


