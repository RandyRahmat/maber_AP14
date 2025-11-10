import random

def level_13():
    a = random.randint(5, 25)
    b = random.randint(5, 25)
    c = random.randint(5, 25)
    
    print(f"\nBerapa hasil dari ({a}+{b})x{c}^2 = ")
    answer = (a+b) * (c**2)
    return answer

def level_14():
    a = random.randint(5, 25)
    b = random.randint(5, 25)
    c = random.randint(5, 25)
    d = random.randint(5, 25)
    
    print(f"\nBerapa hasil dari ({a}+{b})x({c}-{d}) = ")
    answer = (a-b) * (c-d)
    return answer

def level_15():
    a = random.randint(5, 30)
    b = random.randint(5, 30)
    c = random.randint(5, 30)
  
    print(f"({a}+{b})^2 + {c}^2 = ")
    answer = (a+b)**2 + (c**2)
    return answer

def level_16():
    a = random.randint(5, 30)
    b = random.randint(5, 30)
    c = random.randint(5, 30)
    hasil = a + b * c
    pembagi = [i for i in range(2, 30) if hasil % i == 0]
    if not pembagi:
        return level_16()
    d = random.choice(pembagi)
    answer = hasil // d
    print(f"\nBerapa hasil dari ({a}+{b}x{c})/{d} ?")
    return answer