data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum (*args):
    sum = 0

    for i in args:
        if isinstance(i, str):
            sum += (len(i))
#            print(sum)
        if isinstance(i, int):
            sum += i
#            print(sum)
        if isinstance(i, list):
            calculate_structure_sum (*i)
        if isinstance(i, tuple):
            calculate_structure_sum (*i)
        if isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, int):
                    sum += key
                else: sum += len(key)
                if isinstance(value, int):
                    sum += value
                else: sum += len(value)
#                print (sum)
        if isinstance(i, set):
            calculate_structure_sum(*i)

    print(sum)


calculate_structure_sum (data_structure)


