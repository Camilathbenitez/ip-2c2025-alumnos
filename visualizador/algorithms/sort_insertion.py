# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    # TODO
    global items, n, i, j
    # - Si i >= n: devolver {"done": True}.
    
    if i > n:
        return {"done": True}
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap
    
    if j is None:
        
        j = i #indice de la lista
        a= j-1 #adyacente(izquierda)
        b=j
        return {"a": a, "b": b, "swap": False, "done": False}
   
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True
    a=j-1
    b=j
    if j > 0 and items[a] > items[b]: #comparo indices, de izquierda a derecha
        items[a], items[b] = items[b], items[a] #intercambio 
        j = j-1
        return {"a": a, "b": b, "swap": True, "done": False}
   

    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    #siguente indice
    
    
    i=i+1
    j = None 
    return {"a": a, "b": b, "swap": False, "done": False} 



