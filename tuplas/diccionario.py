diccionary={"amarrillo": "yellow",
            "verde": "green",
            "morado": "purple",
            "azul": "blue",
            "cafe":"brown",
            "gris": "gray",
            "naranga": "orange",
            "rosado":"pink",
            "rojo": "red",
            "negro": "black"}
colors=["rojo", "negro" , "blue" ,"yellow"]

for color in colors:
    if color in diccionary:
        print(color, "es", diccionary[color])
    else:
        print(color, "no esta en el diccionario")
        #lbS