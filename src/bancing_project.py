from typing import Union


def mask_account_card(card_namber: str) -> str:
    if "счет" in card_namber:
        return f"{card_namber[:6]}**{card_namber[-4:]}"
    else:
        return f"{card_namber[:-12]}{card_namber[-12:-10]}** ****{card_namber[-4:]}"
        print(mask_account_card())

        def get_date(user_date: Union[str], team=None) -> str:
            """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ"""
            date_format = team.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
            new_date = date_format.strftime("%d.%m.%Y")
            return new_date

        print(get_date(new_date))
