# program1.py
modal = 100000000
laba = 0
bulan = 8

for i in range(1, bulan + 1):
    if i <= 2:
        laba_bulan = 0
        print(f'Laba bulan ke-{i} sebesar: {laba_bulan}')
    elif i == 3 or i == 4:
        laba_bulan = modal * 0.01
        laba += laba_bulan
        print(f'Laba bulan ke-{i} sebesar: {laba_bulan}')
    elif i == 5 or i == 6 or i == 7:
        laba_bulan = modal * 0.05
        laba += laba_bulan
        print(f'Laba bulan ke-{i} sebesar: {laba_bulan}')
    elif i == 8:
        laba_bulan = modal * 0.02  # Mengubah ke 2% untuk bulan ke-8
        laba += laba_bulan
        print(f'Laba bulan ke-{i} sebesar: {laba_bulan}')

print(f'Total laba adalah: {laba}')
