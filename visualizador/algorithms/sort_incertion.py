def step():
    global items, n, i, j

    # Caso final
    if i >= n:
        return {"done": True}

    # Primer paso: inicializar j
    if j is None:
        j = i
        a = j - 1
        b = j
        return {"a": a, "b": b, "swap": False, "done": False}

    # Caso: todavía comparando y tal vez haciendo desplazamiento
    a = j - 1
    b = j

    if j > 0 and items[a] > items[b]:
        # swap
        items[a], items[b] = items[b], items[a]
        j = j - 1   # actualizar j
        return {"a": a, "b": b, "swap": True, "done": False}

    # Si no hay que desplazar más
    i = i + 1
    j = None
    a = i - 1
    b = i if i < n else None
    return {"a": a, "b": b, "swap": False, "done": False}