import string
A = {'a', '1', '!', 'B', '5', ',', 'z', '9', '.', '?'}
B = set() 
C = set()  
E = set()  
for char in A:
    if char.isdigit():
        B.add(char)
    elif char.isalpha():
        C.add(char)
    else:
        E.add(char)
print("Множина A:", A)
print("Множина B (цифри):", B)
print("Множина C (літери):", C)
print("Множина E (розділові знаки):", E)
