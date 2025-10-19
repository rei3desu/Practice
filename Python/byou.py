def main():
    # 各数字の7セグメントのビット表現 (abcdefg)
    seg = [
        0b1111110,  # 0
        0b0110000,  # 1
        0b1101101,  # 2
        0b1111001,  # 3
        0b0110011,  # 4
        0b1011011,  # 5
        0b1011111,  # 6
        0b1110000,  # 7
        0b1111111,  # 8
        0b1111011,  # 9
    ]

    h, m = map(int, input().split(":"))
    K = int(input())

    def display(hour, minute):
        return [hour // 10, hour % 10, minute // 10, minute % 10]

    def diff(a, b):
        total = 0
        for i in range(4):
            # XORで変わったセグメントを検出し、1の数をカウント
            total += bin(seg[a[i]] ^ seg[b[i]]).count("1")
        return total

    def next_time(h, m):
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
        return h, m

    current = display(h, m)

    while True:
        nh, nm = next_time(h, m)
        nxt = display(nh, nm)
        cost = diff(current, nxt)

        if K - cost < 0:
            break
        K -= cost
        h, m = nh, nm
        current = nxt

    print(f"{h:02d}:{m:02d}")


if __name__ == "__main__":
    main()
