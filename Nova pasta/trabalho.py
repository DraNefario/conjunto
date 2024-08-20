def processar_operacao(tipo, conjunto1, conjunto2):
    if tipo == 'U':
        return conjunto1.union(conjunto2)
    elif tipo == 'I':
        return conjunto1.intersection(conjunto2)
    elif tipo == 'D':
        return conjunto1.difference(conjunto2)
    elif tipo == 'C':
        return C(conjunto1, conjunto2)
    else:
        return 'Operação inváida'
    
def C(conjunto1, conjunto2):
    resultado = []
    for i in conjunto1:
        for j in conjunto2:
            par = [i,j]
            resultado.append(par)
    return resultado

def ler_conjunto(linhas):
    return set(linhas.strip().split(', '))

with open('documento.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

num_operacao = int(linhas[0].strip())

indice = 1

for _ in range(num_operacao):
    tipo = linhas[indice].strip()
    conjunto1 = ler_conjunto(linhas[indice +1])
    conjunto2 = ler_conjunto(linhas[indice +2])

    resultado = processar_operacao(tipo, conjunto1, conjunto2)

    print(f'Operação: {tipo}')
    print(f'Conjunto 1: {conjunto1}')
    print(f'Conjunto 2: {conjunto2}')
    print(f'Resultado: {resultado}')
    print('---')
    
    indice += 3    