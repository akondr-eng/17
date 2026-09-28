__version__ = "1.1.0"

def delivery_cost(weight: int | float, distance: int, express: bool = False)-> float:
    if isinstance(weight, bool) or not isinstance(weight, (int, float)):
        raise TypeError("weight должен иметь тип int или float")
    if isinstance(distance, bool) or not isinstance(distance, int):
        raise TypeError("distance должен иметь тип int")
    if not isinstance(express, bool):
        raise TypeError("express должен иметь тип bool")
    if weight<0.01 or weight>30.01:
        raise ValueError("За диапозоном вес")
    if weight > 1:
        raise ValueError("")

    cost = 200 + weight * 35 + distance * 2

    if express:
        cost += 500

    return round(cost, 2)


def delivery_days(distance: int, express: bool = False)-> int:
    if isinstance(distance, bool) or not isinstance(distance, int):
        raise TypeError("distance должен иметь тип int")
    if not isinstance(express, bool):
        raise TypeError("express должен иметь тип bool")

    
    if  1 <= distance <= 100:
        days = 1
    elif distance <= 500:
        days = 3
    elif distance <= 2000:
        days = 7

    if express:
        days = max(1, days - 1)

    return days

def function_name(parameter: int) -> int:
    """Краткое назначение функции.

    Args:
        parameter: Описание параметра.

    Returns:
        Описание результата.

    Raises:
        TypeError: Когда передан неверный тип.
        ValueError: Когда значение находится вне диапазона.
    """
