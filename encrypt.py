def rfc_encrypt(plaintext: str, key: int, reps: int) -> str:
    if key == 1:
        return plaintext
    
    rails = [[] for i in range(key)]
    direction = 1
    current_rail = 0

    for ch in plaintext:
        rails[current_rail].append(ch)
        current_rail += direction
        if current_rail == 0 or current_rail == key-1:
            direction *= -1
    
    ciphertext = ''
    for rail in rails:
        ciphertext += ''.join(rail)
    
    if reps == 1:
        return ciphertext
    return rfc_encrypt(ciphertext, key, reps-1)


print(rfc_encrypt("HELLO WORLD", 3, 1))