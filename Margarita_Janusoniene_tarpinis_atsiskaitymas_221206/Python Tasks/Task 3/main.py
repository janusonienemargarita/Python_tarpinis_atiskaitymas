# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}


def showObjectValues(audi):
    new_list = []

    for value in audi.values():

        new_list.append(value)
    return new_list

print(showObjectValues(audi))
#######################################################

def showObjectKeys(audi):
    new_list3 = []

    for key in audi.keys():

        new_list3.append(key)
    return new_list3


print(showObjectKeys(audi))