# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j#global llama a las variables de afuera, modificandolas dentro de la funcion
    items = list(vals)
    n = len(items)
    i = 0 #cantidad de pasadas
    j = 0 #indice de la lista

def step():
    #TODO:
    global items, n, i, j
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    a=j 
    b=j+1 #adyacente del indice,elemento de al lado 
 # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True
    if  i < n-1:
      if items[a]>items[b]:#sin ciclos for porque funciona "paso a paso"
         items[a],items[b]= items[b],items[a] #intercambio de menor a mayof
         swap=True
      else:
         swap=False 
      
    j=j+1#aumento el indice
      
    if j >= n-i-1:#si hay que reiniciar el indice
       j=0
       i=i+1
      #Devolver {"a": a, "b": b, "swap": swap, "done": False}.    
    return  {"a": a, "b": b, "swap": swap, "done": False}
    # Cuando no queden pasos, devolvé {"done": True}.
    if i >=n-1:
       return {"done": True}