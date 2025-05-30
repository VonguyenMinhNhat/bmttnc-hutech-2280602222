class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text

        rails = ['' for _ in range(num_rails)]
        rail_index = 0
        direction = 1

        for char in plain_text:
            rails[rail_index] += char
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return ''.join(rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text

        # Xác định vị trí từng ký tự
        rail_pattern = [0] * len(cipher_text)
        rail_index = 0
        direction = 1

        for i in range(len(cipher_text)):
            rail_pattern[i] = rail_index
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Đếm số ký tự ở mỗi rail
        rail_counts = [rail_pattern.count(i) for i in range(num_rails)]

        # Tách cipher_text thành từng rail
        rails = []
        start = 0
        for count in rail_counts:
            rails.append(list(cipher_text[start:start + count]))
            start += count

        # Duyệt theo pattern để lấy từng ký tự đúng vị trí
        result = ''
        for i in range(len(cipher_text)):
            rail = rail_pattern[i]
            result += rails[rail].pop(0)

        return result
