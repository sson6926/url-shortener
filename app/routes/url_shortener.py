from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse
from shortuuid import uuid
from app.models import URL
from app.database import collection

router = APIRouter()

#short_id bi cam
RESERVED_SHORT_IDS = ["shorten", "docs", "redoc"]


@router.post("/shorten")
async def shorten_url(url_data: URL):
    original_url_str = str(url_data.url)
    if url_data.custom_short_id:
        short_id = url_data.custom_short_id
    else:
        short_id = uuid()[:6]

    if short_id in RESERVED_SHORT_IDS:
        raise HTTPException(status_code=400, detail="ID nay bi cam vui long chon ID khac")

    existing_url = collection.find_one({"short_id": short_id})
    if existing_url:
        raise HTTPException(status_code=400, detail="ID nay da duoc su dung")


    new_url = {
        "original_url": original_url_str,
        "short_id": short_id
    }
    collection.insert_one(new_url)

    return {"short_id": short_id}


@router.get("/{short_id}")
async def redirect_to_url(short_id: str):
    url_data = collection.find_one({"short_id": short_id})

    if not url_data:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url_data["original_url"])