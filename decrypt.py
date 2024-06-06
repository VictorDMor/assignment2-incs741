def rfc_decrypt(ciphertext: str, key: int, reps: int) -> str:
    if key == 1:
        return ciphertext

    def single_decrypt(text: str, key: int) -> str:
        rail_lengths = [0] * key
        direction = 1
        current_rail = 0

        for ch in text:
            rail_lengths[current_rail] += 1
            current_rail += direction
            if current_rail == 0 or current_rail == key - 1:
                direction *= -1

        rails = [[] for _ in range(key)]
        idx = 0
        for i in range(key):
            for j in range(rail_lengths[i]):
                rails[i].append(text[idx])
                idx += 1

        plaintext = []
        current_rail = 0
        direction = 1
        rail_indices = [0] * key

        for _ in text:
            plaintext.append(rails[current_rail][rail_indices[current_rail]])
            rail_indices[current_rail] += 1
            current_rail += direction
            if current_rail == 0 or current_rail == key - 1:
                direction *= -1

        return ''.join(plaintext)

    plaintext = ciphertext
    for _ in range(reps):
        plaintext = single_decrypt(plaintext, key)

    return plaintext
