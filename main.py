dict1 = {'bananas': 7, 'apples': 3, 'pears': 14}
dict2 = {'bananas': 3, 'apples': 6, 'grapes': 9}

def merge_max_mappings(dict1, dict2):
    aux = dict1.copy()
    for clave in dict2:
        if clave in aux:
            aux[clave] = max(aux[clave], dict2[clave])
        else:
            aux[clave] = dict2[clave]
    return aux

print(merge_max_mappings(dict1, dict2))
print(dict1)
print(dict2)