items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1  # empezamos desde el segundo elemento
    j = None

def step():
    global items, n, i, j

    if i >= n:
        return {"done": True}

    if j is None:
        j = i
        a = j - 1
        b = j
        return {"a": a, "b": b, "swap": False, "done": False}

    a = j - 1
    b = j
    if j > 0 and items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}

    i += 1
    j = None
    a = i - 1
    b = i
    return {"a": a, "b": b, "swap": False, "done": False}