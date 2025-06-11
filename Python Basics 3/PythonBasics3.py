""" Functions
# Need def to define functions
# First class: can be used in functions or as parameter
# default: (var = 5) can be overrided
# (*, var = 10) anything after * must be defined when calling
# (*var, this = 5) var must be list, tuple, set (will be unpacked)
    # (1,2,3,4,5, this = 5) this must be defined afterwards
    # program creates tuple with *var (1,2,3,4,5)

"""


# 0. Basic simple function that takes one parameter
def greet(name):
    print(f"Hi {name}, it's nice to meet you !")


greet("Raameen")


# 1. uses defaults (only need one parameter, can override the second one)
def power(base, exp=2):
    print(base**exp)


power(5)  # 5^2 = 25
power(10, 5)  # 10^5 = 100000


# 2. * keyword only
#   if there is star, everything after must be defined when calling
def crop(text, *, width=80, ellipses="..."):
    if len(text) < width:
        print(text)
    else:
        cutoff = len(text) - width
        print(text[:cutoff] + ellipses)


crop("hiiii", width=2)


# 3. *args
def mean(*nums, round_to=2):
    if not nums:  # takes in a list of some sort to "unpack"
        raise ValueError("ERROR! No list inputted.")
    avg = sum(nums) / len(nums)
    return round(avg, round_to)


print(mean(1, 2, 3, 4, 5, round_to=2))  # need to define round_to after numbers
