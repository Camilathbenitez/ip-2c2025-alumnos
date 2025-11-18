# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor a la izquierda (None = arrancar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1       # insertion sort arranca en el segundo elemento
    j = None


def step():
    global items, n, i, j

    # --- 1) Algoritmo terminado ---
    if i >= n:
        return {"a": None, "b": None, "swap": False, "done": True}

    # --- 2) Primer paso de la iteración: inicializar j ---
    if j is None:
        j = i
        # devolvemos A y B como índices válidos
        return {"a": j-1 if j > 0 else None, "b": j, "swap": False, "done": False}

    # --- 3) Desplazamientos (un paso por vez, sin ciclos) ---
    # Mientras haya que desplazar: items[j-1] > items[j]
    if j > 0 and items[j-1] > items[j]:
        # swap adyacente
        items[j-1], items[j] = items[j], items[j-1]
        a, b = j-1, j
        j -= 1     # seguimos hacia la izquierda
        return {"a": a, "b": b, "swap": True, "done": False}

    # --- 4) Si ya no hay más desplazamientos ---
    # Avanzamos a la siguiente i
    i += 1
    j = None
    return {"a": None, "b": None, "swap": False, "done": False}