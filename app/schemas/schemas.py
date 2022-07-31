from typing import Optional, Union, List
from fastapi import Depends
from pydantic import BaseModel, Field ,validator
import re



class Cursola_Input(BaseModel):
    input_text : str = Field(
        ..., 
        min_length=5, 
        max_length=20,
        description="入力文字列"
    )
    max_length : int = Field(
        100, 
        ge=10, 
        le=200, 
        description="生成文字列の最大文字数"
    )
    @validator("input_text")
    def validate_input_text(cls, v:str) -> Union[str, ValueError]:
        if not re.search(r'[0-9a-zA-Zあ-んア-ン一-鿐]', v):
            ValueError("Not japanese")
        return v        


class CustomBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Cursola_Output(CustomBaseModel):
    output_text : str = Field(
        ...,
        max_length=200,
        description="実際の生成文字列"
    )

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    class Config():
        orm_mode = True
