from fastapi import FastAPI

# Нужен для разворачивания БД, 
# т.к. в нем хранится информация 
# о структуре всех таблиц
from .config.db import Base 

# Движок для подключения к БД
from .config.db import engine

# Подключаем роутеры
from .routers import works


app = FastAPI(
    title = "College Portfolio API",
    docs_url = "/documentation",
    redoc_url = None
)

# Создаем в базе данных таблицы по моделям.
# Если таблицы уже есть, то ничего не произойдет.
Base.metadata.create_all(bind=engine)

# Добавляем подключенный роутер в объект app
app.include_router(works.router)