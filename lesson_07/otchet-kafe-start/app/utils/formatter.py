"""Модуль для форматирования текста и чисел."""


def format_title(text: str) -> str:
    """Форматирует заголовок, делая первую букву заглавной.

    Args:
        text: Исходная строка.

    Returns:
        Отформатированная строка.
    """
    return text.strip().title()


def format_kopeks(amount: int) -> str:
    """Форматирует сумму в копейках в рубли.

    Args:
        amount: Сумма в копейках.

    Returns:
        Строка с суммой в рублях.
    """
    return f"{amount / 100:.2f} руб."