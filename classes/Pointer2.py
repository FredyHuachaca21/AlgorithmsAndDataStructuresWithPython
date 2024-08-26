dictionary_one = {
    'value': 11
}

dictionary_two = dictionary_one

print("Antes de actualizar el valor")
print("dictionary_one = ", dictionary_one)
print("dictionary_two = ", dictionary_two)

print("\n dictionary_one apunta a la dirección de memoria: ", id(dictionary_one))
print(" dictionary_two apunta a la dirección de memoria: ", id(dictionary_two))

dictionary_two['value'] = 22

print("\nDespués de actualizar el valor")
print("dictionary_one = ", dictionary_one)
print("dictionary_two = ", dictionary_two)

print("\n dictionary_one apunta a la dirección de memoria: ", id(dictionary_one))
print(" dictionary_two apunta a la dirección de memoria: ", id(dictionary_two))
