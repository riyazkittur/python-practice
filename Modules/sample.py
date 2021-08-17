import box

findArea = box.area

print("Area is :", findArea(2, 4))

print("Volume is :", box.volume(2, 4, 6))

print("Module name is : ", box.__name__)
print("doc is ", box.__file__, box.__doc__, box.__package__)

print(dir(box))
