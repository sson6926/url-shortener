
# Rút gọn link 

Các bước để tự host

B1: ```git clone```

B2: ```pip install -r requirements.txt```

B3: Tạo file .env

```
MONGODB_URL=<ib vung kin>
MONGODB_DATABASE=url_shortener
```

B3: ```uvicorn app.main:app --reload```
