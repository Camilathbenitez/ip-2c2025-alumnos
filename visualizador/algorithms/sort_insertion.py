def step():
    global items, n, i, j

    # 1) Si ya terminamos todo
    if i >= n:
        return {"done": True}

    # 2) Si j es None → recién empezamos a trabajar con items[i]
    if j is None:
        j = i
        return {"a": j-1 if j > 0 else None, "b": j, "swap": False, "done": False}

    # 3) Si todavía hay que desplazar hacia la izquierda
    if j > 0 and items[j-1] > items[j]:
        # Hacer UN SOLO swap: intercambiar j-1 con j
        items[j-1], items[j] = items[j], items[j-1]

        j -= 1  # seguir en la próxima llamada

        return {"a": j, "b": j+1, "swap": True, "done": False}

    # 4) Si ya no hay que desplazar → avanzar i
    i += 1
    j = None

    return {"a": None, "b": None, "swap": False, "done": False}