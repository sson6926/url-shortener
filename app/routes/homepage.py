from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def homepage():
    return {'msg': 'Day la trang chu, vao /docs de xem'}