num_one = 11
num_two = num_one

print("Antes de actualizar el valor de num_two")
print("num_one = ", num_one)
print("num_two = ", num_two)

print("\n num_one apunta a la dirección de memoria: ", id(num_one))
print(" num_two apunta a la dirección de memoria: ", id(num_two))

num_two = 22

print("\nDespués de actualizar el valor de num_two")
print("num_one = ", num_one)
print("num_two = ", num_two)

print("\n num_one apunta a la dirección de memoria: ", id(num_one))
print(" num_two apunta a la dirección de memoria: ", id(num_two))