from collections import deque

grafo = {
    "Manaus":      ["Belém", "Fortaleza"],
    "Belém":       ["Manaus", "Recife", "Fortaleza"],
    "Fortaleza":   ["Manaus", "Belém", "Recife", "Salvador"],
    "Recife":      ["Belém", "Fortaleza", "Salvador", "BH"],
    "Salvador":    ["Fortaleza", "Recife", "BH", "Brasília"],
    "BH":          ["Recife", "Salvador", "RJ", "Brasília", "SP"],
    "Brasília":    ["Salvador", "BH", "SP", "Goiânia"],
    "RJ":          ["BH", "SP"],
    "SP":          ["BH", "Brasília", "RJ", "Curitiba", "Goiânia"],
    "Goiânia":     ["Brasília", "SP", "Curitiba"],
    "Curitiba":    ["SP", "Goiânia", "Porto Alegre"],
    "Porto Alegre":["Curitiba"]
}


def bfs(origem, destino):
    if origem == destino:
        print(f"Origem e destino são o mesmo centro: {origem}")
        return

    fila = deque()
    fila.append([origem])

    visitados = set()
    visitados.add(origem)

    while fila:
        caminho_atual = fila.popleft()
        no_atual = caminho_atual[-1]

        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                novo_caminho = caminho_atual + [vizinho]

                if vizinho == destino:
                    paradas = len(novo_caminho) - 1
                    print(f"Rota encontrada: {' → '.join(novo_caminho)}")
                    print(f"Número de paradas: {paradas}")
                    return

                visitados.add(vizinho)
                fila.append(novo_caminho)

    print(f"Não existe rota entre {origem} e {destino}.")


print("------------------------------")
print("Teste 1: Manaus → Porto Alegre")
print("------------------------------")
bfs("Manaus", "Porto Alegre")

print()
print("------------------------------")
print("Teste 2: Belém → Goiânia")
print("------------------------------")
bfs("Belém", "Goiânia")

print()
print("------------------------------")
print("Teste 3: Fortaleza → RJ")
print("------------------------------")
bfs("Fortaleza", "RJ")
