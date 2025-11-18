def step():
    global items, n, i, j

    # 1) Si ya terminamos
    if i >= n:
        return {"done": True}

    # 2) Inicializar j cuando empezamos con items[i]
    if j is None:
        j = i
        return {"a": j, "b": j, "swap": False, "done": False}

    # 3) Comparar y desplazar
    if j > 0 and items[j-1] > items[j]:
        items[j-1], items[j] = items[j], items[j-1]
        j -= 1
        return {"a": j, "b": j+1, "swap": True, "done": False}

    # 4) Ya no hay más swaps → avanzar
    i += 1
    j = None

    # A y B siempre deben existir → devolvemos un par válido
    return {"a": i-1, "b": i-1, "swap": False, "done": False}