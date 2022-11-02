#arbitrary argument *args
# = x number of arguments
def printName(*args):
    print(args) #printtaa tuplena
    print(args[0])

#printName("ruokatunti","on kohta")

def printCountries(country3,country2,country1):
    print("biggest is",country2)

#pass as keyword argument
printCountries(country1='suomi',country2='ruotsi',country3='norja')

#arbitrary keyword arguments **kwargs
def printKids(**kwargs):
    print(kwargs) # printtaa dictionaryn
    print(kwargs['eka']) #'Adam

printKids(eka='Adam',toka='Eva')

#yleisesti näitä näkee konstruktoreissa:
class Test:        #tuple    #dictionary
    def __init__(self,*args,**kwargs):
        pass
            

