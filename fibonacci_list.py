

from typing_extensions import get_type_hints


def getFibList(number):
    if number == 1:
        return [1]

    elif number == 2:
        return [1, 1]

    else:
        get_previous_fib_list = getFibList(number-1)
        new_last_element = get_previous_fib_list[-1] + get_previous_fib_list[-2]

        # jab hum list mei kuch append karte hai toh, woh list update ho jaati hai
        get_previous_fib_list.append(new_last_element)

        # get_previous_fib_list ab update ho gayi hai, par kyuki ab yeh current list hai, previous nahi\
        # toh confusion avoid karne ke liye hum ek nayi variable mei yeh list daal kar return karenge
        # jisse code padhne wala confuse na ho

        current_fib_list = get_previous_fib_list

        return current_fib_list
getFibList(67,89,0,89,67)
