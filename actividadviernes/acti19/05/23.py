def d1():
    diccionary={"Alpenrose":"Rosa alpina",
            "Amaranth":	"Amaranto",
            "American Lotus":"Loto americano",
            "Anise hyssop":	"Hisopo de anís",
            "Camellia":	"Camelia",
            "Common poppy":	"Amapola común",
            "Daffodil":	"Narciso",
            "Lavender":	"Lavanda",
            "Lilac":	"Lila",
            "Orchid":	"Orquídea"}
    return diccionary
print(d1())
flowers=input("ingrese la flor que desea buscar")

def buscar (flowers):
    if flowers in d1():
        print(flowers, "si esta en el diccionario , es", d1()[flowers])
    else:
        print(flowers, "no esta en el diccionario")
buscar(flowers)