lista = [1,2,1,1,5]
        
for numero in lista[:]:# .copy():
    if numero==1:
        lista.remove(numero)

print(lista)
