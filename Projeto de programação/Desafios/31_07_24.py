def num_perfeito(num_maior):
    perfeitos = []
    for num in range(1, num_maior + 1): 
        divisores = []
        for c in range(1, num):
            if num % c == 0:
                divisores.append(c)
        if sum(divisores) == num:
            perfeitos.append(num)
    print(perfeitos)
            
    
num_perfeito(50000)