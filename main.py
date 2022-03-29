# -*- coding: utf-8 -*-
"""
Main FastAPI app.
"""
# -*- coding: utf-8 -*-
from typing import List

from fastapi import FastAPI, Query, Request

from description import desc
from helpers import emojis, passwd, random_users
from pydantic_models import Emoji, Password, Person
import json
import subprocess

app = FastAPI(
    title="Something Random...",
    description=desc,
    version="0.0.1",
    docs_url="/",
)


@app.get("/person", response_model=List[Person], tags=["Randomness..."])
async def random_persons(
    num: int = Query(
        5,
        title="Get a random list of people.",
        ge=1,
        le=50,
    )
) -> List[Person]:
    """
    Get a random list of persons.

    The defautl is 5

    """
    persons = random_users.create(iterations=num)
    return persons


@app.get("/password", response_model=Password, tags=["Randomness..."])
async def random_password(
    num: int = Query(
        8,
        title="Length of password.",
        le=64,
    ),
    hashing: bool = Query(
        False,
        title="Return an MD5 hashed password",
    ),
):
    """
    Generate a random password.
    """
    password = passwd(num, hashing)
    return {"password": password}


@app.get("/emoji", response_model=Emoji, tags=["Randomness..."])
async def random_emoji():
    """
    Return a random emoji.
    """
    return {"emoji": emojis()}

@app.post("/abc")
async def runabc(request: Request):

    inputStr = await request.json()
    #jsonInput = inputStr.decode('utf-8')
    jsonInput = json.dumps(inputStr, indent=2)
    print('body:' + jsonInput)
    
    result = subprocess.run(["/workspace/abcmodel"], input=jsonInput, text=True, stdout=subprocess.PIPE)
    output = result.stdout
    print(output)
    json_out = json.loads(output)
    return  json_out

