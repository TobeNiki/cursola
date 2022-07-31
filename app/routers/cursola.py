
from typing import Any
from fastapi import APIRouter, Depends
import app.schemas.schemas as schema
import app.model as model
from app.auth.oauth2 import  get_current_user


router = APIRouter(
    prefix="/cursola",
    tags=["cursola"]
)


@router.post("/app", response_model=schema.Cursola_Output)
async def cursola(
    cursola_obj: schema.Cursola_Input,
    current_user:str = Depends(get_current_user)
)->schema.Cursola_Output:
    cursola_output_obj = schema.Cursola_Output
    cursola_output_obj.output_text = model.generater.generate(
        cursola_obj.input_text,
        cursola_obj.max_length
    )
    return cursola_output_obj
