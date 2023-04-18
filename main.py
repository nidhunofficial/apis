# -*- coding: utf-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import builtins

app = FastAPI()


origins = [

    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class model_input(BaseModel):
    Code : str  
          

@app.post('/code_prediction')
def code_predd(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    code = input_dictionary['Code']
    
    code.replace("/r", "")
    from guesslang import Guess

    guess = Guess()
    
    language = guess.language_name(code)
    
    return language
    
