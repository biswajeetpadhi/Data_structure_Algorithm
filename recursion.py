
# recursion
def recu(check: int):
    if check == 1:
        print("base condition")
    else:
        return recu(check-1)



def firstMethod():
    secondMethod()
    print("I am the first Method")


def secondMethod():
    thirdMethod()
    print("I am the second Method")


def thirdMethod():
    fourthMethod()
    print("I am the third Method")


def fourthMethod():
    print("I am the fourth Method")


def pri_num(num: int):
    if num == 5:
        print(5)

    else:
        print(num)
        pri_num(num + 1)


def fibonacci(num: int):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def factorial(num: int):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = power_of_two(n-1)
        return power * 2


def check_power_of_two(num: int):
    while num % 2 == 0:
        num = num / 2

    if num ==1:
        return True
    else:
        return False


def isPowerOfTwo(num: int) -> bool:
    if num ==1:
        return True
    if num > 1:
        return num % 2 == 0 and isPowerOfTwo(num / 2)
    else:
        return False


if __name__ == '__main__':
    print(check_power_of_two(16))
    #print(factorial(4))
    # print(fibonacci(3))
    # recu(5)
    #print(power_of_two(4))
    # firstMethod()
    # pri_num(1)

