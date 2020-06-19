# 2020-06-19
# Шифр Виженера


def Vigenere_cipher(input, password):
    input_codes = [ord(i) for i in input]
    password_codes = [ord(i) for i in password]
    output_chars = []

    for b in range(len(input_codes)):
        output_chars.append(input_codes[b] ^ password_codes[b % len(password_codes)])

    for i in range(len(output_chars)):
        output_chars[i] = chr(output_chars[i])

    output = "".join(output_chars)

    return output


a = Vigenere_cipher("Tree. Apple, ball", "asd")
a = Vigenere_cipher(a, "asd")
print(a)
