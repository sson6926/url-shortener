from pydantic import BaseModel, HttpUrl

#du lieu post
class URL(BaseModel):
    url: HttpUrl
    custom_short_id: str = None