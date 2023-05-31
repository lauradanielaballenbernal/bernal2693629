def añadir1(d1):
    n = input("Ingrese la clave que desea añadir: ")
    x = input("Ingrese el valor que desea añadir: ")
    d1[n] = x
def llaves(d1):
    keys = d1.keys()
    return keys
def reverse_dictionary(d1):
    reversed_dict = {value: key for key, value in d1.items()}
    return reversed_dict
def remove_entry(dictionary, key):
    if key in dictionary:
        del dictionary[key]
def search_value(dictionary, value):
    keys = [key for key, val in dictionary.items() if val == value]
    return keys




