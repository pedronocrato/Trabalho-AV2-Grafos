from collections import deque

# Representação do grafo como lista de adjacência
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
    # Caso origem e destino sejam iguais
    if origem == destino:
        print(f"Origem e destino são o mesmo centro: {origem}")
        return

    # Fila do BFS: cada elemento é o caminho percorrido até o momento
    fila = deque()
    fila.append([origem])

    # Controle de nós visitados para evitar ciclos
    visitados = set()
    visitados.add(origem)

    while fila:
        caminho_atual = fila.popleft()
        no_atual = caminho_atual[-1]

        # Visita cada vizinho do nó atual
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                novo_caminho = caminho_atual + [vizinho]

                # Chegou ao destino
                if vizinho == destino:
                    paradas = len(novo_caminho) - 1
                    print(f"Rota encontrada: {' → '.join(novo_caminho)}")
                    print(f"Número de paradas: {paradas}")
                    return

                visitados.add(vizinho)
                fila.append(novo_caminho)

    # Se saiu do while sem encontrar, não existe rota
    print(f"Não existe rota entre {origem} e {destino}.")


# Testes solicitados
print("=" * 50)
print("Teste 1: Manaus → Porto Alegre")
print("=" * 50)
bfs("Manaus", "Porto Alegre")

print()
print("=" * 50)
print("Teste 2: Belém → Goiânia")
print("=" * 50)
bfs("Belém", "Goiânia")

print()
print("=" * 50)
print("Teste 3: Fortaleza → RJ")
print("=" * 50)
bfs("Fortaleza", "RJ")
