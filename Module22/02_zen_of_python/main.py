

def reverse_text(file):

    reverse = []
    reverse_text = open('zen_reverse.txt', 'w')
    original_text = open(file, 'r', encoding='utf-8')
    for elem in original_text:
        reverse.insert(0, elem)
    for i_str in reverse:
        reverse_text.write(str(i_str))

    reverse_text.close()
    original_text.close()


reverse_text('zen.txt')
answer = open('zen_reverse.txt', 'r')
print(answer.read())
answer.close()
