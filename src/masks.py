from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает её маску"""
    return f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


print(get_mask_card_number("карта 7000792289606361"))


def get_mask_account(account: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    return f"** {account[-4:]}"


print(get_mask_account("счет 73654108430135874305"))
