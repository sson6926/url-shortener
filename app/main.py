from fastapi import FastAPI
from app.routes.url_shortener import router as url_shortener_router

app = FastAPI()

# Đăng ký router cho URL shortener
app.include_router(url_shortener_router)