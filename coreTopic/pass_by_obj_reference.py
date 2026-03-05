def immutable_func(x):
    x = x + 10
    print(f"Inside immutable_func: {x}")

def mutable_func(val):
    val.append(10)
    print(f"Inside mutable_func: {val}")

a = 10
immutable_func(a)
print(f"Outside immutable_func: {a}")

list_val = [1, 2, 3]
mutable_func(list_val)
print(f"Outside mutable_func: {list_val}")