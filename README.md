# API-Workshop-II
API-II ECES Workshop

Today we will see "How to create APIs". The discussion will involve these topics:
- FastAPI: for creating your REST interface in Python
- MongoDB: for creating your backend
- Fetch API: for creating your REST interface in JS
- And finally a final project that includes creating your own chatbot api, using OpenAI

The session is going to be a big one so make sure to pay complete attention and all of the resources will be provided in the whatsapp group. Plus if you need some help in anything do place your doubts in the comments!

Moving on with the slides, here is the to-do list for today: 


## Now moving to section one: "FastAPI" 
#FastAPI

==<Begin by creating a new 3.11 environment in a new dir.>
<Install the following packages for the module:
		 fastapi, uvicorn, pydantic, bson(if objectid is to be used), jinja2>==

>### Alright, so what's an app instance?
Well this instance will help you create your base router for your webpage. It will help you create endpoints and routes to your website easily. Basically an initializer for you APIs.
(Make a basic JSON response:
    `@app.get(/)
    async def homepage():
        return JSONResponse(content={
          "message": "this is a response 😁"
        })`
    `@app.get(/{my_name})
    async def my_name(my_name: str):
        return JSONResponse(content={
          "message": "Say my name",
          "response": my_name,
          "👨🏻‍🍳": "good"
        })`
)

>### What are routes?
Routes are basically fastapi instances for various endpoints. As your website expands in size, we end up introducing a lot of endpoints in our project, to mange all of those, we need to use APIRouters().
These help in making our codes manageable as well as help in cleaning up our project.
To create a new route just import APIRouter

``` 
from fastapi import APIRouter
router = APIRouter()

@router.get(/route/)
async def routePage(a: int, b: int):
    return JSONResponse (content={
        "route-response": str(a+b)
    })
```

To import this router in the main app:
```
app.include_router(router)
```

>### Moving on to templates and static files.
Obviously our webpages won't just have a bunch of json's floating around, we need to add some color to our website and give it some life.

The manipulative part of the webpage (mostly the html files) are called as templates, as this is what is essentially "moving" or changing based on our or external inputs.

To create templates:

First create a basic HTML webpage. Hopefully everyone has basic familiarity with html, css.

HTML:
```
<!DOCTYPE html>
<html>
<head>
<title>Hello, {{ name }}!</title>
</head>
<body>
<h4>Hello, {{ name }}!✌️</h4>
</body>
</html> 
```

``` 
from fastapi import FastAPI, TemplateResponse

app = FastAPI()

@app.get("/")
async def index():
    context = {
        "name": "Rohan"
    }
    return TemplateResponse(template="index.html", context=context) 
```

If the templates are present in some other folder, eg. htmls, you can assign that folder as the location for your templates, eg.

```
htmlTemplates = Jinja2Templates(directory="htmls")
...
return htmlTemplates.TemplateResponse(template="index.html", context=context)
```

To include the static files such as your javascript scripts, CSS files, images, fonts etc., we need to mount those files on our app:

```
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

static_files = StaticFiles(directory="static")

app = FastAPI()

app.mount("/static", static_files, name="static")
```


>### Now moving on to the different types of responses:
We have here the basic response, then JSONResponse, HTMLResponse, StreamResponse, RedirectResponse and FileResponse.
The basic Response has these attributes:
    headers: A dictionary of response headers.
    content_type: The content type of the response body.
    content: The response body.
(Try to show them the headers in the console itself.)
(Next show them the different types of responses mentioned.)

>### Pydantic
Pydantic is an important library as it helps in parsing and validating the request and response data by defining the data structure.

Let's check it out by creating a basic post request:

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI ()

class Item(BaseModel):
    name:str
    price:float = 0.0 # default value, if price isn't set
    type:int

@app.post('/submit/')
async def sumbit_req(data: Item):
    """
    do something
    """
    print(data)
    return JSONResponse (content={
        "message": "data recieved successfully!"
    })

```

>### Finally the last question, wtf am I writing before the functions?
Async are essentially the tasks that are brought outside the main event loop and then brought back again, once the task is completed.
Though unlike traditional asynchronous processes, asyncs in python are managed by a single thread itself by cooperative multitasking and prevent multi threaded issues like synchronisation and locking. Though these details are mostly irrelevant for today's session, we need to focus on the part that's relevant: **ASYNCS AND AWAITS**

``` 
import asyncio
async def delayed_print(message, delay):
    await asyncio.sleep(delay)
    print(message)

async def main():
    print("Regular Line 1")
    print("Regular Line 2")

await delayed_print("Async Line after 1 second", 1)

    print("Regular Line 3")

asyncio.run(main())
  ```


Hopefully now I have covered up all of the basics for the FastAPI package, now let's move on to the next topic of today's discussion:


## Section 2: MongoDB
#MongoDB 

### Setting up your MongoClient
MongoDB can be used locally using MongoDB Compass or by hosting it on a server.
To use MongoDB in python: install pymongo

For online servers, follow the steps mentioned in the MongoDB dashboard to set up your client.
```
from pymongo.mongo_client import MongoClient  
  
uri = "mongodb+srv://<username>:<password>@<uri>"  
  
# Create a new client and connect to the server  
client = MongoClient(uri)  
  
# Send a ping to confirm a successful connection  
try:  
    client.admin.command('ping')  
    print("Pinged your deployment. You successfully connected to MongoDB!")  
except Exception as e:  
    print(e)
```

If MongoDB Compass is installed:
```
from pymongo.mongo_client import MongoClient

client = MongoClient()
```

>### CRUD operations in MongoDB
#### Create:
```
collection = client['TestCollection']
db = collection['Users']

user = {
    "fname" = "Rohan"
    "lname" = "Gunjal"
    "roll_no" = "A49"
}

users = [
{
    "fname" = "John"
    "lname" = "Doe"
    "roll_no" = "7"
},
{
    "fname" = "abc"
    "lname" = "xyz"
    "roll_no" = "xxx"
}
]

db.insert_one(user)
db.insert_many(users)
```

#### Read:
```
abc = db.find_one(filter={
	"fname": "abc"
})

a47 = db.find_one(filter={
	"roll_no": "A47"
})

all_users = db.find(filter={}) # returns a list
```

#### Update:
```
db.update_one(filter={
	"roll_no": "xxx"
}, update = {
	"$set": {
		"roll_no": "A75"
	}
})
```

#### Delete:
```
db.delete_one(filter={
	"fname": "Rohan"
})
```


## Section 3: FetchAPI
#FetchAPI

Moving on to the first question:
### What are Promises?
Promises are asynchronous processes that provide a method to handle processes that require some time to execute. These maybe something like a big algorithm that requires something like 10^8 steps or file/data transferring or recieving.
Each promise has 2 main parts:
- Resolve
- Reject

The resolve part is the one that essentially returns "true" or status codes in the 200 range.
The reject part is the one responsible for dealing with the "false" or invalid states.

Now to simulate a big process, we can define a `setTimeout()` function for 1 sec and the create a promise for that.

```
const fun = (value) => setTimeout(() => value > 0.5, 1000);
```

The promise can then be constructed by:
```
const promise= new Promise((resolve, reject) => {
    const value = fun(Math.random());
    if(fun(value)) {
        resolve(`${value} is greater than 0.5`);
    }
    else {
        reject(`${value} is lesser than or equal to 0.5`);
    }
})
```
As you can see the promise has 2 states essentially, the result and the error.
Now let's look at how you resolve the promise:

```
promise
  .then((result)=>{
    console.log("Fulfilled: ", result);
  })
  .catch((error)=>{
    console.log("Error: ", error);
  })
```
Moving on to fetch APIs, let's check out Reqres.in API:

```
const response = fetch('https://reqres.in/api/users/1', {
    method: 'GET'
})

response
    .then((res)=>{
        if(res.ok) {
            console.log('Response ok.');
            return res.json();
        } else {
            console.log('Response invalid');
            return;
        }
     })
     .then((data)=>{
         console.log(data);
     })
     .catch((error)=>{
         console.log('Error: ', error);
     })
```

Moving on to the next method of parsing promises:

### ASYNC / AWAIT:
For async / await, we use try and catch blocks. The try block tries to get the response, where as the catch block catches the error, so that it won't stop our application.

```
const getUser = async () => {
    try {
        const response = await fetch ('https://reqres.in/api/users/1', {
        method: 'GET'
        })
        if(!response.ok) {
            console.log('Error: Response Invalid');
            return;
        }
        const data = await response.json();
        console.log('Data: ', data);
        return data;
    } catch (error) {
        console.log('Error: ', error);
    }
}

document.querySelector('.btn').addEventListner('click', getUser)
```

### GET, POST, PUT and DELETE using fetch API:

#### GET: 
```
const getFun = async () => {
    try {
        const response = await fetch ('https://jsonplaceholder.typicode.com/posts/42', {
        method: 'GET'
        });
        if(!response.ok) {
            console.log('Error: ', response.status);
            return;
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.log('Error: ', error);
    }
}
```

#### POST: 
```

const postFun = async () => {
    try {
        const response = await fetch ('https://jsonplaceholder.typicode.com/posts/', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(data)
        });
        if(!response.ok) {
            console.log('Error: ', response.status);
            return;
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.log('Error: ', error);
    }
}
```

#### PUT: 
```

const putFun = async () => {
    try {
        const response = await fetch ('https://jsonplaceholder.typicode.com/posts/42', {
        method: 'PUT',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(data)
        });
        if(!response.ok) {
            console.log('Error: ', response.status);
            return;
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.log('Error: ', error);
    }
}
```

#### DELETE: 
```

const deleteFun = async () => {
    try {
        const response = await fetch ('https://jsonplaceholder.typicode.com/posts/42', {
            method: 'DELETE',
        });
        if(response.status !== 204) {
            console.log('Error: ', response.status);
            return;
        }
        console.log('Delete operation Successful.');
    } catch (error) {
        console.log('Error: ', error);
    }
}
```

Hopefully, I have covered everything up, so now we can finally discuss the project!
