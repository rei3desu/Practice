def main():
    num = [0] * 2
    num[0] = int(input("数字を入力"))
    num[1] = int(input())
    moden = input("どう計算するか")
    if moden == "+":
        print(num[0] + num[1])
    elif moden == "-":
        print(str(num[0]) + "-" + str(num[1]) + "=" + str(num[0] - num[1]))


if __name__ == "__main__":
    main()