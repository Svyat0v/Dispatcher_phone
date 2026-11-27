
from sqlalchemy import inspect, text

from app.database.connection import engine


def add_crew_column():

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    if "orders" not in tables or "crews" not in tables:
        print("Сначала создайте таблицы orders и crews.")
        return

    columns = [
        column["name"]
        for column in inspector.get_columns("orders")
    ]

    if "crew_id" in columns:
        print("Столбец crew_id уже существует.")
        return

    with engine.begin() as connection:
        connection.execute(
            text(
                "ALTER TABLE orders "
                "ADD COLUMN crew_id INTEGER REFERENCES crews(id)"
            )
        )

    print("Столбец crew_id успешно добавлен!")


if __name__ == "__main__":
    add_crew_column()
