from collections import deque


def main():
    # add code here
    orders = deque(maxlen=5)
    orders.append("ENT001")
    orders.append("SAL002")
    orders.append("SAL002")
    orders.append("DES004")
    orders.append("ENT002")
    orders.append("DES005")
    print(orders)
    return


if __name__ == "__main__":
    main()
