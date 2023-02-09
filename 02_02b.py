
from collections import deque


def check_palindrome(word):
    d = deque(word)
    while len(d) > 1:
        if d.pop().lower() != d.popleft().lower():
            return False

    return True


def main():
    # add code here
    word = "Tacocat"

    print(check_palindrome(word))

    return


if __name__ == "__main__":
    main()
