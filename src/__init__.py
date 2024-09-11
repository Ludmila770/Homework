def mask_account_card(user_card: str) -> str:
    """Функция для маскировки номера карты/счета"""

    if "check" in user_card:
        return f"{user_card[:6]}**{user_card[-4:]}{user_card[:-12]}"
    else:
        return f"{user_card[:-12]} {user_card[-12:-10]}** ****{user_card[-4:]}"


print(mask_account_card("Счет 73654108430135874305"))


def get_date(date: str) -> str:
    """Функция принимающая строку с датой и модифицирующая её в формат 'ДД.ММ.ГГГГ'"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))

