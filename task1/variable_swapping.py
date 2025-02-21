print("\n" + "="*40)
print(" VARIABLE SWAPPING".center(40))
print("="*40)

# Declaring variables for swapping
x = 10
y = 20

# Print before swapping
print(f"Before Swapping:")
print(f"x = {x} (Type: {type(x).__name__})")
print(f"y = {y} (Type: {type(y).__name__})")

# Swapping with type casting
temp = int(x)
x = int(y)
y = temp

# Print after swapping
print(f"\nAfter Swapping:")
print(f"x = {x} (Type: {type(x).__name__})")
print(f"y = {y} (Type: {type(y).__name__})") 