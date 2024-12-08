import re
from datetime import datetime


def is_date(value: str) -> bool:
    """
    Проверка формата даты DD.MM.YYYY
    """
    if re.match(r"^\d{2}\.\d{2}\.\d{4}$", value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            pass
    """
    Проверка формата даты YYYY-MM-DD
    """
    if re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            pass
    return False


def is_phone(value: str) -> bool:
    """
    Проверка номера телефона
    """
    return bool(re.match(r"^\+7\d{10}$", value))


def is_email(value: str) -> bool:
    """
    Проверка email
    """
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+", value))


def detect_type(value: str) -> str:
    """
    Определение типа данных
    """
    if is_date(value):
        return "date"
    elif is_phone(value):
        return "phone"
    elif is_email(value):
        return "email"
    else:
        return "text"
