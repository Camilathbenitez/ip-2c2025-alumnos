tems = []
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

    
    # Si ya recorrimos todos los elementos, terminamos
    if i >= n:
        return {"done": True}
    
    # Si j es None, iniciamos desplazamiento para el elemento en posición i
    if j is None:
        j = i
        a = j - 1
        b = j
        return {"a": a, "b": b, "swap": False, "done": False}

    # Calculamos a y b en cada paso antes de comparar
    a = j - 1
    b = j

    # Si el elemento anterior es mayor, hacemos un swap
    if j > 0 and items[a] > items[b]: #comparacion
        items[a], items[b] = items[b], items[a] #intercambio
        j = j - 1
        return {"a": a, "b": b, "swap": True, "done": False}

    # Si no hay que desplazar más, avanzamos al siguiente elemento
    a = j - 1
    b = j
    i = i + 1
    j = None
   
    return {"a": a, "b": b, "swap": False, "done": False}