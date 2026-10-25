def format_title(text: str) -> str:
    """Делает заголовок красивым."""
    return text.strip().title()

def format_kopeks(amount: int) -> str:
    """Переводит копейки в рубли."""
    return f"{amount / 100:.2f} руб."