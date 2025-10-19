def main():
    num = input("数字を入力").split()
    moden = input("どう計算するか")
    if moden == "+":
        print(int(num[0]) + int(num[1]))


if __name__ == "__main__":
    main()