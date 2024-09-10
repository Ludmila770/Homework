from typing import Any
my_dict = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def filter_by_state(dictionary_inform: list[dict[str, object]], state_id: str = "EXECUTED") -> list[dict[str, object]]:
    """Функция фильтрующая данные по указаному параметру"""
    list_stat = []
    for i in dictionary_inform:
        if i ['state'] == state_id:
         list_stat.append(i)
    return list_stat



def sort_by_date(dictionary_inform:list[dict[str, Any]],revers:bool = True) ->list[dict[str, Any]]:
    """Функция сортирующая словарь по дате в порядке убывания"""


    sorted_list = sorted(dictionary_inform, key=lambda x: x["date"], reverse=revers)
    return sorted_list

if __name__ == "__main__":
    print(filter_by_state(my_dict))

    print(sort_by_date(my_dict))




