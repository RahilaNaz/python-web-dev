print("\n" + "="*40)
print("3. VARIABLE DATA TYPES".center(40))
print("="*40)

# Declaring variables with different data types
int_var = 25                    # Integer
float_var = 3.14               # Float
str_var = "Hello World"        # String
bool_var = True                # Boolean
list_var = [1, 2, 3]          # List
tuple_var = (4, 5, 6)         # Tuple
dict_var = {"key": "value"}    # Dictionary
set_var = {7, 8, 9}           # Set

# Printing variables with their data types
print(f"Integer:    {int_var} ({type(int_var).__name__})")
print(f"Float:      {float_var} ({type(float_var).__name__})")
print(f"String:     {str_var} ({type(str_var).__name__})")
print(f"Boolean:    {bool_var} ({type(bool_var).__name__})")
print(f"List:       {list_var} ({type(list_var).__name__})")
print(f"Tuple:      {tuple_var} ({type(tuple_var).__name__})")
print(f"Dictionary: {dict_var} ({type(dict_var).__name__})")
print(f"Set:        {set_var} ({type(set_var).__name__})")
print("="*40) 