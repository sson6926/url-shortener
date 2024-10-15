from fastapi import FastAPI
from app.routes.url_shortener import router as url_shortener_router
from app.routes.homepage import router as homepage
app = FastAPI()

# Đăng ký router cho URL shortener
app.include_router(url_shortener_router)
app.include_router(homepage)