from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):  # Sửa 'seft' thành 'self'
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:  # Sửa 'seft' thành 'self'
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:  # Thêm kiểm tra ký tự có trong bảng chữ cái
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter)
            else:
                encrypted_text.append(letter)  # Giữ nguyên ký tự không nằm trong alphabet
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:  # Sửa 'seft' thành 'self'
        return self.encrypt_text(text, -key)  # Tối ưu bằng cách tái sử dụng encrypt_text