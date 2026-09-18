def nto1(n: int):

    if n == 0:
        return

    nto1(n - 1)
    print(n)


# nto1(15)

arr = [80, 2, 7]
n = len(arr) - 1


def arrSum(arr: list[int], n: int) -> int:
    if n == 0:
        return arr[0]

    return arr[n] + arrSum(arr, n - 1)


# print(arrSum(arr, n))

strx = "Geeks for Geeks yM"
n = len(strx) - 1


def revString(strx: str, n: int) -> str:
    if n == 0:
        return strx[0]

    return strx[n] + revString(strx, n - 1)


# print(revString(strx, n))


num = 1234567


def sumDigit(num):

    if num < 10:
        return num

    lastdigit = num % 10
    return lastdigit + sumDigit(num // 10)


# print(sumDigit(num))

string = "abxyba"
l = 0
r = len(string) - 1


def palindromeCheck(string, l, r):
    if l >= r:
        return True

    if string[l] != string[r]:
        return False

    return palindromeCheck(string, l + 1, r - 1)


print(palindromeCheck(string, l, r))


def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(int(n / 10))


def reverse(s):
    if s == s[0]:
        return s[0]
    return s[-1] + reverse(s[:-1])


def max_recursive(nums: list[int]):
    if len(nums) == 1:
        return nums[0]
    curr = nums.pop(0)

    restmax = max_recursive(nums)

    if curr > restmax:
        return curr
    else:
        return restmax


def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
