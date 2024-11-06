Dlya sozdaniya odnogo universal'nogo klassa dlya CRUD operatsiy, kotoryy mozhno ispol'zovat' dlya lyuboy modeli, mozhno sozdat' obobshchennyy klass `CRUDBase`, kotoromu budut nasledovat' vse ostal'nye modeli.

Vot kak eto mozhno realizovat':

### 1. Sozdayom obshchiy CRUD klass (`crud_base.py`)

Eto bazovyy klass, kotoryy prinimayet v sebe model' i primenyaet CRUD operatsii ko vsem tablitcam avtomaticheski.

```python
# app/crud_base.py
from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic
from pydantic import BaseModel
from sqlalchemy.ext.declarative import as_declarative, declared_attr

# Type variables
ModelType = TypeVar("ModelType")  # Modeli iz SQLAlchemy
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)  # Skhemy dlya sozdaniya
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)  # Skhemy dlya obnovleniya

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """ CRUDBase s opredeleniyem osnovnoy modeli """
        self.model = model

    def get(self, db: Session, id: int) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 10) -> list[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.dict())  # Preobrazovanie skhemy v model'
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType | dict
    ) -> ModelType:
        obj_data = db_obj.__dict__
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: int) -> ModelType | None:
        obj = db.query(self.model).get(id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj
```

### 2. Nasledovanie CRUD dlya kazhdoy modeli

Teper' mozhno sozdat' CRUD dlya lyuboy modeli nasleduya `CRUDBase`. Naprimer, sozdayom CRUD dlya modeli `User`:

```python
# app/crud_user.py
from app.crud_base import CRUDBase
from app.models import User
from app.schemas import UserCreate, UserUpdate

user_crud = CRUDBase[User, UserCreate, UserUpdate](User)
```

### 3. Izmeneniya v osnovnom fayle `main.py`

V osnovnom fayle `main.py` mozhem ispol'zovat' universal'nyy `user_crud` dlya vseh CRUD operatsiy:

```python
# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas
from .database import SessionLocal, engine
from .crud_user import user_crud
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Zavisimos't' dlya sessii BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create(db=db, obj_in=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = user_crud.get_multi(db, skip=skip, limit=limit)
    return users
```

### 4. Sozdaniye CRUD dlya drugikh modeley

Dlya lyuboy novoy modeli (naprimer, `Product`) prosto sozdayom fayl `crud_product.py` i nasleduem `CRUDBase`, kak bylo sdelano s `User`:

```python
# app/crud_product.py
from app.crud_base import CRUDBase
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate

product_crud = CRUDBase[Product, ProductCreate, ProductUpdate](Product)
```

Eto resheniye pozvolyaet legko dobavlyat' novye CRUD operatsii dlya lyubykh modeley bez povtoryayushchegosya koda.

Вот полная структура и пример проекта на FastAPI с использованием универсального класса для CRUD операций. В этом проекте создадим две модели: `User` и `Product`. Универсальный класс `CRUDBase` будет использоваться для CRUD операций с каждой из моделей.

### 1. Структура проекта

```bash
my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py                # Основной файл для запуска FastAPI
│   ├── crud_base.py           # Универсальный класс CRUDBase
│   ├── crud_user.py           # CRUD операции для модели User
│   ├── crud_product.py        # CRUD операции для модели Product
│   ├── models.py              # Определения моделей SQLAlchemy
│   ├── schemas.py             # Pydantic схемы для моделей
│   └── database.py            # Настройки базы данных
└── requirements.txt
```

### 2. Настройка базы данных (`database.py`)

Здесь создадим подключение к базе данных и объект сессии:

```python
# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Локальная SQLite база данных

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

### 3. Определение моделей (`models.py`)

Создадим модели `User` и `Product` с помощью SQLAlchemy.

```python
# app/models.py
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
```

### 4. Pydantic схемы для моделей (`schemas.py`)

Схемы Pydantic нужны для валидации данных, поступающих в API.

```python
# app/schemas.py
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
```

### 5. Универсальный класс CRUD (`crud_base.py`)

Этот класс обрабатывает основные операции для любой модели, которая будет ему передана.

```python
# app/crud_base.py
from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic
from pydantic import BaseModel

# Определяем типы
ModelType = TypeVar("ModelType")  # Модель SQLAlchemy
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)  # Pydantic схема для создания
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)  # Pydantic схема для обновления

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 10) -> list[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType | dict) -> ModelType:
        obj_data = db_obj.__dict__
        update_data = obj_in.dict(exclude_unset=True) if isinstance(obj_in, BaseModel) else obj_in
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: int) -> ModelType | None:
        obj = db.query(self.model).get(id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj
```

### 6. CRUD операции для моделей (`crud_user.py` и `crud_product.py`)

Теперь создаем экземпляры CRUD для каждой модели.

```python
# app/crud_user.py
from app.crud_base import CRUDBase
from app.models import User
from app.schemas import UserCreate, UserUpdate

user_crud = CRUDBase[User, UserCreate, UserUpdate](User)
```

```python
# app/crud_product.py
from app.crud_base import CRUDBase
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate

product_crud = CRUDBase[Product, ProductCreate, ProductUpdate](Product)
```

### 7. Основной файл FastAPI (`main.py`)

Здесь настраиваем основные маршруты для каждой модели.

```python
# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas
from .database import SessionLocal, engine
from .crud_user import user_crud
from .crud_product import product_crud
from .models import Base

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Зависимость для работы с сессией базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршруты для модели User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create(db=db, obj_in=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_crud.get_multi(db, skip=skip, limit=limit)

# Маршруты для модели Product
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create(db=db, obj_in=product)

@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_crud.get(db, id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return product_crud.get_multi(db, skip=skip, limit=limit)
```

### 8. Установка зависимостей и запуск приложения

Добавьте зависимости в `requirements.txt`:

```text
fastapi
sqlalchemy
pydantic
uvicorn
```

Запустите приложение:

```bash
uvicorn app.main:app --reload
```

Теперь API готово!