from test_crud import (
    add_client,
    get_all_clients,
    # get_client_by_phone,
    # get_client_by_name,
    # update_client_phone,
    # delete_client,
)
#1
add_client(
	full_name="Пётр Иван Васильевич",
	phone="79055403913",
	address="улица Маршала Будёного 6А",
	comment="Лопнула Скважина",
	email="test@gmail.com"
)

#2
# clients = get_all_clients()
#
# for client in clients:
#     print(f"ID: {client.id}")
#     print(f"ФИО: {client.full_name}")
#     print(f"Телефон: {client.phone}")
#     print(f"Адрес: {client.address}")
#     print(f"Email: {client.email}")
#     print("-" * 30)

#3
# client = get_client_by_phone("+79001234567")
#
# if client:
#     print("Клиент найден!")
#     print(f"ФИО: {client.full_name}")
#     print(f"Телефон: {client.phone}")
#     print(f"Адрес: {client.address}")
#     print("-" * 30)
# else:
#     print("Клиент не найден!")
#     print("-" * 30)
# #4
# client = get_client_by_name("Пётр Иван Васильевич")
#
# if client:
#     print("клиент найден")
#     print(f"ФИО: {client.full_name}")
#     print("-" * 30)
# else:
#     print("Клиент не найден!")
#     print("-" * 30)
# #5
# client = update_client_phone("+79013473579", 1)
#
# if client:
#     print(f"Номер клиента успешно обновлен")
#     print("-" * 30)
# else:
#     print("Неизвестная операция.")
#     print("-" * 30)
# #6
# client = delete_client(1)
#
# if not client:
#     print("Клиент был удален!")
#     print("-" * 30)
# else:
#     print("Неизвестная операция")
#     print("-" * 30)
