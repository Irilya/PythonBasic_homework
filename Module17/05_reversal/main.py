original_text = input('Введите строку: ')
original_text_rvr = original_text[::-1]

i = original_text.index('h')
n = original_text_rvr.index('h')
n = - n - 2

print('Развёрнутая последовательность между первым и последним h:', original_text[n:i:-1])


