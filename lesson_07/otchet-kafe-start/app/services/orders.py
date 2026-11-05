"""Модуль для работы с заказами."""


def revenue_by_waiter(orders: list[dict], top: int = 3) -> list[tuple[str, int]]:
    """Считает выручку по официантам и возвращает топ.

    Args:
        orders: Список заказов.
        top: Количество лучших официантов.

    Returns:
        Список кортежей (имя официанта, сумма).
    """
    totals = {}
    for order in orders:
        waiter = order["waiter"]
        totals[waiter] = totals.get(waiter, 0) + order["amount"]
    return sorted(totals.items(), key=lambda item: item[1], reverse=True)[:top]


def sort_orders_in_place(orders: list[dict]) -> None:
    """Сортирует список заказов по сумме на месте.

    Args:
        orders: Список заказов.
    """
    orders.sort(key=lambda order: order["amount"])