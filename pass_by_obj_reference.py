def immutable_func(x):
    x = ("modified", "new one")
    print(f"Inside immutable_func: {x}")


def mutable_func(val):
    val = {"role": "modified developer"}
    print(f"Inside mutable_func: {val}")


a = ("original",)
immutable_func(a)
print(f"Outside immutable_func: {a}")

list_val = {"role": "developer"}
mutable_func(list_val)
print(f"Outside mutable_func: {list_val}")
