# 2020-06-05
# Сделать функции dec2bin и bin2dec для преобразования десятичного числа в двоичное и наоборот
def bin2dec(bin):
    dec = 0
    pos = 0
    for ch in bin[::-1]:
        dec += int(ch) * (2 ** pos)
        pos += 1
    return dec


def dec2bin(dec):
    bin = ""
    while dec != 0:
        bin = str(dec % 2) + bin
        dec //= 2
    return bin


print("bin2dec: ", bin2dec("101001"))
print("dec2bin: ", dec2bin(30))
