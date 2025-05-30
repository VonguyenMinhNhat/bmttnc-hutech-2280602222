class PlayfairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        seen = set()
        matrix = []

        for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen and char.isalpha():
                seen.add(char)
                matrix.append(char)
                if len(matrix) == 25:
                    break

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def preprocess_text(self, text):
        text = text.upper().replace("J", "I")
        cleaned = ""

        for c in text:
            if c.isalpha():
                cleaned += c

        i = 0
        pairs = []
        while i < len(cleaned):
            a = cleaned[i]
            b = ""
            if i + 1 < len(cleaned):
                b = cleaned[i + 1]
                if a == b:
                    b = "X"
                    i += 1
                else:
                    i += 2
            else:
                b = "X"
                i += 1
            pairs.append(a + b)

        return pairs

    def playfair_encrypt(self, plain_text, matrix):
        pairs = self.preprocess_text(plain_text)
        encrypted = ""

        for pair in pairs:
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted += matrix[row1][(col1 + 1) % 5]
                encrypted += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted += matrix[(row1 + 1) % 5][col1]
                encrypted += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted += matrix[row1][col2]
                encrypted += matrix[row2][col1]

        return encrypted

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)
            if row1 == row2:
                decrypted += matrix[row1][(col1 - 1) % 5]
                decrypted += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted += matrix[(row1 - 1) % 5][col1]
                decrypted += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted += matrix[row1][col2]
                decrypted += matrix[row2][col1]

        return decrypted
