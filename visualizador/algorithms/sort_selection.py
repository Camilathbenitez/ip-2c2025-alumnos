# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    
    if i >= n - 1:
        return {"done": True}

    if fase == "buscar":
        
        if j < n:
            a = min_idx
            b = j
            
            if items[j] < items[min_idx]:
                min_idx = j
                a = min_idx
            
            j += 1
            
            return {"a": a, "b": b, "swap": False, "done": False}
        
        else:
            fase = "swap"
            return {"a": i, "b": min_idx, "swap": False, "done": False}
        
    elif fase == "swap":
        
        swap_realizado = False
        a = i
        b = min_idx
        
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            swap_realizado = True
            
        # Reinicio
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        
        return {"a": a, "b": b, "swap": swap_realizado, "done": False}
