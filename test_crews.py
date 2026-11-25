from app.services.crew_service import add_crew, get_all_crews


crew_id = add_crew(
    name="Бригада № 1",
    leader="Иванов Иван",
    phone="+79001234567"
)

print("Создана бригада:", crew_id)

for crew in get_all_crews():
    print(crew.id, crew.name, crew.leader, crew.status)