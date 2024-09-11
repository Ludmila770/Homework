from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает её маску"""
    return f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


print(get_mask_card_number("карта 7000792289606361"))


def get_mask_account(account_number: str) -> str | None:
    """Возвращает замаскированный номер счета"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"{"*"*2}{account_number[-4:]}"
    else:
        return None


print(get_mask_account("счет 73654108430135874305"))

