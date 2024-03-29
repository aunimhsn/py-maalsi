
def get_max(numbers:list[float]) -> float:
    if len(numbers) == 0:
        raise Exception('Empty list')
    
    result = numbers[0]

    for number in numbers:
        if number > result:
            result = number

    return result


def get_max(numbers:list[float]) -> float:
    filtered = [number for i, number in numbers if numbers[i-1] > 5]