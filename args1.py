# *args enables functions to receive an arbitrary number of arguments.
# It is a special syntax in Python used in function definitions to allow a variable number of positional arguments.
def print_args(*args):
    print(f"args is a {type(args)} with {len(args)} elements.")
    print(args)

print_args(1)
print_args(1, 2)
print_args([73, 42])
print_args([73, 42], "oi", "rodrigo", False)
print_args()

# The 5 characters *args aren't special.
# The  asterisk * immediately to the left of a parameter name is responsible for this process.
# We can write *args as *bananas or *abracadabra.
# args is always a tuple, which can be empty.
def print_args(*abracadabra):
    print(f"abracadabra is a {type(abracadabra)} with {len(abracadabra)} elements.")
    print(abracadabra)

print_args("hello",1,2,5.3)
