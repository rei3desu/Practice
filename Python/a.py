# laptopにて

def main():
    import sys

    # 7セグメントの各桁のパターン（a,b,c,d,e,f,gの順、1:点灯、0:消灯）
    seg = {
        '0': "1111110",
        '1': "0110000",
        '2': "1101101",
        '3': "1111001",
        '4': "0110011",
        '5': "1011011",
        '6': "1011111",
        '7': "1110000",
        '8': "1111111",
        '9': "1111011"
    }
    
    # 2つの数字のセグメント変化コストを計算
    def digit_cost(old, new):
        old_pat = seg[old]
        new_pat = seg[new]
        cost = 0
        for i in range(7):
            if old_pat[i] != new_pat[i]:
                cost += 1
        return cost

    # 現在の表示の文字列 (HHMM: 0埋め4桁)
    def time_to_str(h, m):
        return f"{h:02d}{m:02d}"

    # 2つの時刻表示間の遷移コストを計算
    def transition_cost(old_h, old_m, new_h, new_m):
        old_str = time_to_str(old_h, old_m)
        new_str = time_to_str(new_h, new_m)
        cost = 0
        for i in range(4):
            cost += digit_cost(old_str[i], new_str[i])
        return cost

    # 次の時刻への更新
    def next_time(h, m):
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
        return h, m

    # 入力を取得
    # 入力例: "12:34" (HH:MM) と K （電力量）
    line = sys.stdin.readline().strip()
    if not line:
        return
    hh_str, mm_str = line.split(":")
    curr_h = int(hh_str)
    curr_m = int(mm_str)
    K_line = sys.stdin.readline().strip()
    if not K_line:
        return
    K = int(K_line)
    
    # まずは 1440 分（1日の全遷移）サイクルにおける消費電力を計算
    cycle_cost = 0
    t_h, t_m = curr_h, curr_m
    for _ in range(1440):
        nh, nm = next_time(t_h, t_m)
        c = transition_cost(t_h, t_m, nh, nm)
        cycle_cost += c
        t_h, t_m = nh, nm

    # 1日サイクル分をまとめて消耗できる場合は短縮
    if cycle_cost > 0:
        cycles = K // cycle_cost
        K %= cycle_cost
        # 時刻はサイクル後と同じなので変更不要

    # 残りの電力で1分ずつ進める
    while True:
        nh, nm = next_time(curr_h, curr_m)
        cost = transition_cost(curr_h, curr_m, nh, nm)
        if K >= cost:
            K -= cost
            curr_h, curr_m = nh, nm
        else:
            break

    # 最終的な時刻を HH:MM 形式で出力
    print(f"{curr_h:02d}:{curr_m:02d}")

if __name__ == "__main__":
    main()