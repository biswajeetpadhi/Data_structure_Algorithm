from typing import Dict
from collections import OrderedDict


def main():

    key_value: dict[int, int] = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}

    for i in sorted(key_value.keys()):
        print(i, end=" ")
    print()

    for j in sorted(key_value.items()):
        print(j)
    print()

    dic1 = OrderedDict(sorted(key_value.items()))
    print(dic1)
    print(type(dic1))
    print()
    dic2 = {'ravi': '10', 'rajnish': '9',
            'sanjeev': '15', 'yash': '2', 'suraj': '32'}
    dic3 = OrderedDict(sorted(dic2.items()))
    print(dic3)
    print()
    for j in sorted(dic2.items()):
        print(j)
    print()

    country_code = {'India': '0091',
                    'Australia': '0025',
                    'Nepal': '00977'}
    print(country_code.get('India'))


if __name__ == "__main__":
    main()
