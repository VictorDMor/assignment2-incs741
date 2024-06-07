def rfc_decrypt(ciphertext: str, key: int) -> str:
    if key == 1:
        return ciphertext

    n = len(ciphertext)
    rails = [['' for _ in range(n)] for _ in range(key)]
    direction = 1
    row = 0

    for i in range(n):
        rails[row][i] = '*'
        row += direction
        if row == key - 1 or row == 0:
            direction *= -1

    index = 0
    for i in range(key):
        for j in range(n):
            if rails[i][j] == '*' and index < len(ciphertext):
                rails[i][j] = ciphertext[index]
                index += 1

    plaintext = ''
    row = 0
    direction = 1

    for i in range(n):
        plaintext += rails[row][i]
        row += direction
        if row == key - 1 or row == 0:
            direction *= -1

    return plaintext.replace('*', '')


def repeated_rfc_decrypt(ciphertext: str, key: int, reps: int) -> str:
    for i in range(reps):
        ciphertext = rfc_decrypt(ciphertext, key)
        print(f"Rep {reps-i}: {ciphertext}")
    return ciphertext



# ciphertext = "CTGSEACNT TNEOEEMIIIHRNOH T LARIRPOOYI H RCIEADSUYO EHIUSFRSCR OMNCTO NTEPEEC FTIDPRISCLE DESRE.YL TPT  DFCQ  UCUAN  SE RAEADVAS"
ciphertext = "TAOTINEN KAT I ODIOAEI OHHLSCTE TTETOEL BI IHI GAO   EPSEA TO SS  EEK  ELRCPTSIY EANRPHMCYEK E CREAAIEJURTE  IEASHI MA DRN RH  AUWTA RF EFTFHENTPSF Q   TAILB E TTECAPMSIYIY SRPURNTBL YCL OANAO  E  TVREAOSHOTTNULSRHK"

decrypted_text = repeated_rfc_decrypt(ciphertext, 3, 3)
print(decrypted_text)
