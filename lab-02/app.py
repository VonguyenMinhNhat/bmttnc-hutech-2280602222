from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các đối tượng mã hóa
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()

# ==== Trang giao diện người dùng ==== #
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/transposition")
def transposition():
    return render_template('transposition.html')


# ==== Xử lý Caesar Cipher ==== #
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"{text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"{text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"


# ==== Xử lý Vigenere Cipher ==== #
@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
    return f"{text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
    return f"{text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"


# ==== Xử lý Rail Fence Cipher ==== #
@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    num_rails = int(request.form['inputNumRailsPlain'])
    encrypted_text = rail_fence_cipher.rail_fence_encrypt(text, num_rails)
    return f"{text}<br/>Số rail: {num_rails}<br/>Encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    num_rails = int(request.form['inputNumRailsCipher'])
    decrypted_text = rail_fence_cipher.rail_fence_decrypt(text, num_rails)
    return f"{text}<br/>Số rail: {num_rails}<br/>Decrypted text: {decrypted_text}"


# ==== Xử lý Playfair Cipher ==== #
@app.route("/playfair/creatematrix", methods=['POST'])
def playfair_creatematrix():
    key = request.form['inputKeyMatrix']
    matrix = playfair_cipher.create_playfair_matrix(key)
    return render_template('playfair.html', matrix=matrix, matrix_key=key)

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
    return render_template('playfair.html', encrypted=encrypted_text, plain=text, key=key)

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
    return render_template('playfair.html', decrypted=decrypted_text, cipher=text, key=key)


# ==== Xử lý Transposition Cipher ==== #
@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = transposition_cipher.encrypt(text, key)
    return f"{text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = transposition_cipher.decrypt(text, key)
    return f"{text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2222, debug=True)