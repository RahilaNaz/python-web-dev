# Define Boolean variables
is_sunny = True
is_warm = True
is_weekend = False

# Evaluate logical conditions
# AND operator
print("\nAND Operator:")
print("Is it sunny AND warm?", is_sunny and is_warm)
print("Is it sunny AND weekend?", is_sunny and is_weekend)

# OR operator
print("\nOR Operator:")
print("Is it sunny OR warm?", is_sunny or is_warm)
print("Is it sunny OR weekend?", is_sunny or is_weekend)

# NOT operator
print("\nNOT Operator:")
print("Is it NOT sunny?", not is_sunny)
print("Is it NOT weekend?", not is_weekend)

# Complex conditions
print("\nComplex Conditions:")
print("Is it (sunny AND warm) OR weekend?", (is_sunny and is_warm) or is_weekend)
print("Is it sunny AND (warm OR weekend)?", is_sunny and (is_warm or is_weekend)) 