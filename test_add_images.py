


import clesperanto as cle


import numpy as np

input1 = np.asarray([[1, 2, 3]])
input2 = np.asarray([[4, 5, 6]])

print("init ok")
print("============================")

reference = np.asarray([[5, 7, 9]])
output = cle.add_images_weighted(input1, input2)
result = cle.pull(output)

print(result)
print(reference)
assert(np.array_equal(result, reference))

print("with missing parameters ok")
print("============================")

reference = np.asarray([[9, 12, 15]])
output = cle.add_images_weighted(input1, input2, None, 1, 2)
result = cle.pull(output)

print(result)
print(reference)
assert(np.array_equal(result, reference))

print("with None as output ok")
print("============================")



reference = np.asarray([[9, 12, 15]])
output = cle.add_images_weighted(input1, input2, None, weight1=1, weight2=2)
result = cle.pull(output)

print(result)
print(reference)
assert(np.array_equal(result, reference))

print("with named parameters ok")
print("============================")



reference = np.asarray([[9, 12, 15]])
output = cle.add_images_weighted(input1, input2, weight1=1, weight2=2)
result = cle.pull(output)

print(result)
print(reference)
assert(np.array_equal(result, reference))

print("with named parameters and missing parameters ok")
print("============================")


reference = np.asarray([[9, 12, 15]])
output = cle.add_images_weighted(input1, input2, weight2=2, weight1=1)
result = cle.pull(output)

print(result)
print(reference)
assert(np.array_equal(result, reference))

print("with named parameters in wrong order and missing parameters ok")
print("============================")

