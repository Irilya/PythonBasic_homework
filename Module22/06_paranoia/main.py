

def ceiser_cipher(file):

    alfabeta = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_text = []
    orig_text = open(file, 'r', encoding='utf-8')
    print('Содержимое файла text.txt: ')
    print(orig_text.read())
    orig_text.close()
    count = 0
    orig_text = open(file, 'r', encoding='utf-8')
    for line in orig_text:
        count += 1
        for sign in line:
            if sign in alfabeta:
                index = alfabeta.find(sign)
                index += count
                sign = alfabeta[index]
                cipher_text.append(sign)
            else:
                cipher_text.append(sign)
    cipher_text = ''.join(cipher_text)
    orig_text.close()
    cipher = open('cipher_text.txt', 'w', encoding='utf-8')
    cipher.write(str(cipher_text))
    cipher.close()
    cipher = open('cipher_text.txt', 'r', encoding='utf-8')
    print('Содержимое файла cipher_text.txt: ')
    print(cipher.read())
    cipher.close()


ceiser_cipher('text.txt')
