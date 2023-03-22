# `unpack` permits to unpack a sequence into distinct variables
# and it is done by using the `*` operator

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


def unpacking_list():
    coins = [100, 50, 25]
    print(total(*coins), "Knuts")  # unpacking works with lists, tuples etc... because they preserve order


def unpacking_dict():  # clearer
    coins = {"galleons": 100, "sickles": 50, "knuts": 25}
    print(total(**coins), "Knuts")  # two asterisks are used to unpack dictionaries


# It turns out that in python asterisks are also used by functions
# to accept an arbitrary number of arguments
#
# e.g.,: def foo(*args): print(args)
#        def bar(**kwargs): print(kwargs)
def f(*args, **kwargs):  # *args represents a variable numebr of positional arguments
                         # **kwargs represents a variable number of keyword arguments,
                         # i.e, named arguments -> it will be a dictionary
    print("Positional:", args)
    print("Named:", kwargs)

# Notice that, the `print` function is a function that accepts an arbitrary number of arguments
# whose prototype is something like:
#    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)


def main():
    #unpacking_dict()
    f(100, 50, 25)
    f(100, 50, 25, 10, 5, 1)
    f(100, 50, 25, 10, 5, 1, galleons=100, sickles=50, knuts=25)  # hence, in unpacking_dict() using **coins
                                                                  # was like passing named arguments



if __name__ == "__main__":
    main()