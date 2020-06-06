# 2020-06-06
# Аналогично предыдущей задачи сделать dec2hex и hex2dec


def hex2dec(hex):
    dec = 0
    pos = 0
    for ch in hex[::-1]:
        d = ord(ch) - 48
        if d > 9:
            d -= 7
        dec += d * 16 ** pos
        pos += 1
    return dec


def dec2hex(dec):
    hex = ""
    hex_str = "0123456789ABCDEF"
    while dec != 0:
        r = dec % 16
        dec //= 16
        hex = hex_str[r] + hex
    return hex


print(hex2dec("FF"))
print(dec2hex(255))
