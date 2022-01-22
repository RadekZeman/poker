# srdce_1
# kule_2
# krize_3
# piky_4


if __name__ == '__main__':
    karta1 = [12, 2]
    karta2 = [11, 3]
    if karta1[0] == karta2[0] and karta1[0] > 7:    # dvojice
        print(f"call")
    elif karta1[1] == karta2[1] and karta1[0]+karta2[0] > 19:  # barva
        print(f"call")
    elif karta1[0]+karta2[0] > 21:  # vysoke karty
        print(f"call")
    elif karta1[0] == 14 or karta2[0] == 14 or karta1[0] == 13 or karta2[0] == 13:  # kral nebo eso
        print(f"call")
    else:
        print(f"fold")
