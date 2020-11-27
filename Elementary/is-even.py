# https://py.checkio.org/en/mission/is-even/

'''
Check if the given number is even or not. Your function should return True if the number is even,
and False if the number is odd.
'''

def is_even(num: int) -> bool:
    # your code here
    return num % 2 == 0


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
