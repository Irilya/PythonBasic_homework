
Adress_IP = input('Введите IP: ')
Adress_IP = Adress_IP.split('.')

Flag = True
if len(Adress_IP) != 4:
    print(f'Адрес — это четыре числа, разделённые точками.')
    Flag = False
elif len(Adress_IP) == 4:
    for numero in Adress_IP:
        if not numero.isdigit():
            print(f'{numero} — это не целое число.')
            Flag = False
        elif int(numero) > 255:
            print(f'{numero} превышает 255.')
            Flag = False
if Flag == True:
    print(f'IP-адрес корректен.')



