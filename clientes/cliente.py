dados=[]
idades=[]
rendas=[]

def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

with open('clientes/clientes.txt', 'r') as f:
    dados=f.readlines()

for linha in dados:
        partes = linha.strip().split(';')
        idade = int(partes[2])
        renda = float(partes[3])
        
        idades.append(idade)
        rendas.append(renda)

print(f"Média de idade: {calcular_media(idades)}")
print(f"Média de renda mensal: {calcular_media(rendas)}")