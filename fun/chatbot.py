import openai
from config.db import connection

db = connection['ChatBot_History']

with open('openai_api_key.txt', 'r') as f:
    openai.api_key = f.read()

MODEL = "gpt-3.5-turbo"


def generate_request(user: str) -> list:
    collection = db[user]
    documents = collection.find({})
    prompt = []
    for document in documents:
        prompt.append({
            'role': document['role'],
            'content': document['content']
        })
    if len(prompt) > 30:
        prompt = prompt[-30:]
    return prompt


def createResponse(user: str, prompt: str, role: str | None = 'user') -> str:
    collection = db[user]
    if not role:
        role = 'user'

    user_prompt = {
        'role': role,
        'content': prompt
    }

    request = generate_request(user)
    request.append(user_prompt)
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=request,
        temperature=0
    )

    content = response["choices"][0]["message"]["content"]
    collection.insert_one(user_prompt)
    collection.insert_one({
        'role': 'assistant',
        'content': content
    })
    return content
