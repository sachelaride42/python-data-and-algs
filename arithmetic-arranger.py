algarisms = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def arithmetic_arranger(problems, show_answers=False):
    operations = []
    sizes = []
    results = []
    counter_operation = 0
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        operation = problem.split(' ')
        if len(operation[0]) > 4 or len(operation[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not (operation[1] == '+' or operation[1] == '-'):
            return "Error: Operator must be '+' or '-'."
        if (not operation[0].isdigit()) or not (operation[2].isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(operation[0]) == len(operation[2]):
            sizes.append([len(operation[0]), 0])
        elif len(operation[0]) > len(operation[2]):
            sizes.append([len(operation[0]), 0])
        else:
            sizes.append([len(operation[2]), 2])

        if operation[1] == '+':
            res = str(int(operation[0]) + int(operation[2]))
        else:
            res = str(int(operation[0]) - int(operation[2]))

        results.append(res)
        operations.append(operation)
        # print(operation)

    arrangement1 = ''
    arrangement2 = ''
    arrangement3 = ''
    arrangement4 = ''

    for op in operations:
        indice = operations.index(op)
        if len(op[0]) == len(op[2]):
            arrangement1 += f"{' ' * 2}{op[0]}"
            arrangement2 += f"{op[1]} {op[2]}"
            arrangement3 += f"{'-' * (len(op[0]) + 2)}"
            arrangement4 += f"{' ' * (len(op[0]) + 2 - len(results[indice]))}{results[indice]}"
        elif len(op[0]) > len(op[2]):
            d = len(op[0]) - len(op[2])
            if d >= 2:
                arrangement1 += f"  {op[0]}"
                arrangement2 += f"{op[1]}{' ' * (d - 1 + 2)}{op[2]}"
                arrangement3 += f"{'-' * (len(op[0]) + 2)}"
            else:
                arrangement1 += f"  {op[0]}"
                arrangement2 += f"{op[1]}{' ' * (d - 1 + 2)}{op[2]}"
                arrangement3 += f"{'-' * (len(op[0]) + 2)}"

            arrangement4 += f"{' ' * (len(op[0]) + 2 - len(results[indice]))}{results[indice]}"
        else:
            d = len(op[2]) - len(op[0])
            arrangement1 += f"{' ' * (2 + d)}{op[0]}"
            arrangement2 += f"{op[1]} {op[2]}"
            arrangement3 += f"{'-' * (len(op[2]) + 2)}"
            arrangement4 += f"{' ' * (len(op[2]) + 2 - len(results[indice]))}{results[indice]}"

        if indice < (len(operations) - 1):
            arrangement1 += ' ' * 4
            arrangement2 += ' ' * 4
            arrangement3 += ' ' * 4
            arrangement4 += ' ' * 4

    if show_answers:
        arrangement = f"{arrangement1}\n{arrangement2}\n{arrangement3}\n{arrangement4}"
    else:
        arrangement = f"{arrangement1}\n{arrangement2}\n{arrangement3}"

    print(arrangement)
    return arrangement


# print(f'\n{arithmetic_arranger(["32 + 698",])}')

arithmetic_arranger(["322 + 698", "3801 - 2", "45 + 43", "123 + 49"])
