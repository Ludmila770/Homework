from typing import  Any

def filter_by_state(dictionary_inform:list[dict[str, Any]],state_id:str = "EXECUTED") -> list[dict[str,Any]]:
 """Функция фильтрующая данные по указаному параметру"""

 list_stat = []
 for key in dictionary_inform:
     if key.get('state') == state_id:
         list_stat.append(key)
         return list_stat


     print(filter_by_state(dictionary_inform))


def sort_by_date(dictionary_inform:list[dict[str, Any]],revers:bool = True) ->list[dict[str, Any]]:
 """Функция сортирующая словарь по дате"""


 sorted_inform_state = sorted(dictionary_inform, key = lambda dictionary_inform: dictionary_inform["date"], revers = revers)


 return sorted_inform_state


print(sort_by_date(dictionary_inform))