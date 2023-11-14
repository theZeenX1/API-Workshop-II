from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from config.db import connection
from models.model import User
from cryptography.fernet import Fernet
import base64

db = connection['API_workshop']
Users = db['Users']
Keys = db['API_keys']


submit_form_route = APIRouter()


@submit_form_route.post('/submit-form', response_model=None)
async def submit_form(data: User):
    user_data = data.model_dump()
    try:
        user_email = user_data['email']
        user = Users.find_one({'email': user_email})
        if not user:
            Users.insert_one(user_data)

        api_data = Keys.find_one({'email': user_email})
        if api_data:
            return JSONResponse(content={"error": f" kAn APIey already exists for the User: {user_email}", "email": user_email}, status_code=403)
        key = Fernet.generate_key()
        api_key = base64.urlsafe_b64encode(key).decode()
        Keys.insert_one({
            'email': user_data['email'],
            'api_key': api_key,
            'tokens_left': 50
            })
        user = Users.find_one({'email': user_data['email']})
        return JSONResponse(content={"success": "User Data Uploaded Successfully", "email": str(user['email'])}, status_code=200)
    except HTTPException as e:
        return JSONResponse(content={"error": f"Validation error: {e.detail}"}, status_code=422)
