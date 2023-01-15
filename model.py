from pydantic import BaseModel, validator

class searchModel(BaseModel):
    txt: str
