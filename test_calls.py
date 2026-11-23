# from app.services.call_service import add_call, get_all_calls


# add_call(
#     phone="+79002257085",
#     call_type="incoming",
#     status="missed"
# )

# calls = get_all_calls()

# for call in calls:
#     print(
#         f"ID: {call.id} | "
#         f"Телефон: {call.phone} | "
#         f"Тип: {call.call_type} | "
#         f"Статус: {call.status} | "
#         f"Дата: {call.created_at}"
#     )

from app.services.call_service import (
    get_all_calls,
    update_call_status
)

calls = get_all_calls()

if calls:
    call = calls[0]

    print(f"Было: {call.status}")

    success = update_call_status(call.id, "answered")

    if success:
        print("Статус успешно изменён!")
else:
    print("История звонков пуста!")