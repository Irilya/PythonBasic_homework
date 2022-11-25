import exrex


for item in range(0, 10000):
    print(f'{item:00004d}')

print('*' * 40)

print(*exrex.generate(r'\d{4}'), sep='\n')
