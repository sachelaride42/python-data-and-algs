my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start, target=''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        # pelo modo que está organizado o antes e dentro desse while, current é
        # valor que já possui o menor valor calculado real no dic distances
        for node, distance in graph[current]:
            # Aqui é avaliado se a distancia de um nó (node) diretamente
            # ao nó current (o qual já tem a menor distancia calculada correta) somada
            # com essa distancia já calculada é menor que a distancia já calculada no
            # grafo distances para esse nó sendo avaliado (node)
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

    #targets_to_print = [target] if target else graph
    #for node in targets_to_print:
    #    if node == start:
    #        continue
    #    print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    #return distances, paths


shortest_path(my_graph, 'A')