# abrir arquivo criptografado

import os
import pyaes

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# remover arquivo original

os.remove(file_name)

# definir a chave de encriptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCRT(key)
decrypt_data = aes.decrypt(file_data)

# salvar arquivo criptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()