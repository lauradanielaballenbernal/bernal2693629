class vehiculo:
    pass
class landvehiculo(vehiculo):
    pass
class trackeddvehiculo(vehiculo):
    pass

for cls1 in [vehiculo,landvehiculo,trackeddvehiculo]:
    for cls2 in [vehiculo,landvehiculo,trackeddvehiculo]:
     print (issubclass(cls1, cls2),end="\t")
    print()