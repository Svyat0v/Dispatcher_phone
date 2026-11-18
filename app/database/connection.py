
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Путь к корню проекта
BASE_DIR = Path(__file__).resolve().parents[2]

# Путь к файлу базы данных
DATABASE_PATH = BASE_DIR / "dispatcher.db"

# Строка подключения
DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

# Создаём подключение
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Создаём фабрику сессий
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Базовый класс для моделей
Base = declarative_base()

print(f"Путь к базе данных: {DATABASE_PATH}")