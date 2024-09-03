from dotetime import dotetime
from typing import Union
import masks

def mask_account_card(user_card:str) -> str:
 "Функция для маскировки номера карты/счета"
 if "check" in user_card:
  return f"{user_card[:6]}**{user_card[-4:]}{user_card[:-12]}"
 else:
  return f"{user_card[:-12]} {user_card[-12:-10]}** ****{user_card[-4:]}"

print(mask_account_card("Счет 73654108430135874305"))


def get_date(user_date:Union[str]) -> Union[str]:
  "Функция принимающая строку с датой и модифицирующая её в формат 'ДД.ММ.ГГГГ'"
 date_it = datetime.strptime(user_date,"%Y-%m-%dT%H:%M:%S.%f")
 new_date = date_format.strftime("%d.%m.%Y")
    return new_date
  print(get_date(new_date))