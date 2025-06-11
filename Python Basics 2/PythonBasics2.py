# Python Basics #2: Core Data Types Pt 2
    # List, Tuples, Range
    # Set Frozenset
    # Dict

"""
# Vocab:
   Dynamic Array: can be resized at runtime
   Static Array: fixed size
   Hash(): Makes uniqe key that can be used to:
        # check for repeats in memory

List: can change size, ordred, dynamic array
    # index[#] O(1)
    # append [back] O(1)
    # pop [front] O(n) - have to move everything back (deque is O(1))
    # shift [middle] O(n)
    # in sequence O(n)
Tuple: cannot change tuple size, but can change elements stored in them (unhashable),
fixed record/hashable, only read cannot add
    # index[#] O(1)
    # in sequence O(n)
    # can be mutable with [] ONLY - not hashable bc its changed after runtime
Range: loops/slicing, (start,stop,step) arthmetically
    # index[#] O(1)
    # in sequence O(1)

"""

# Tuple example:

date = ("Friday", "June", 9)  # cant add to tuple
day, month, number = date  # assign names ( Dictionary )
print(day)  # print individual
hash(date)

mutable = ([], "Brackets allow change")  # brackets = mutable ! hashable
mutable[0].append("Look!")
print(mutable)

"""
Dict: short for dictionary ( look up )
Cannot have two of the same elements in either set (only multiset)
Sets: mutable, membership and uniqness
    # x in set O(1) // hash, search for uniqness
    # add remove O(1)
    # can use math:   ( fast membership )
        - (|) union
        - (&) intersection
        - (-) difference
        - (^) symetric difference
    # unordered
    # cant store unashable items (lists) - use frozenset or tuples
    # cannot be used for hash
Frozenset: not mutable, hashable "set of things" you can use as dict key
    # immutable
    # has composite key, constant lookup
    # slightly faster bc immutable

Functions for frozensets and sets:
syntax:                     what it does:               time:
x in s	                    membership	                O(1) avg.
s.add(x)	                add element	                O(1)
s.remove(x) / discard(x)	delete (raises / silent)	O(1)
`s1	                        s2ors1.union(s2)`	        union
s1 & s2	                    intersection	            O(min(len))
s1 - s2	                    difference	                O(len(s1))
len(s)	                    size	                    O(1)
<, <=, >, >=	            subset / superset test	    O(min(len))

frozensets can do union, etc. but make new frozenset ( not mutable )
"""


# set mutation helpers
s ={}
h = {}
t= s | h
s.update(t)              # union in-place  ( |= )
s.intersection_update(t) # keep common     ( &= )
s.difference_update(t)   # remove t elems  ( -= )

# set example union:

visitors = {"ada", "grace"}
new_batch = {"alan", "ada"}
unique_users = visitors | new_batch  # union

for stuff in unique_users:
    if "grace" in visitors:  # very fast look up ( hash process )
        print("hi")
        break

text = "The quick brown fox jumps over the lazy dog"
words = set(text.lower().split())
stopwords = {"the", "a", "of", "and", "to"}
uniqieWords = words - stopwords  # prints unique words
print(uniqieWords)
sameWords = words & stopwords
print(sameWords)


"""
Dict function:
    # Mappng: each key is unique
    # Keys are hashed -> place in hash bucket, make a hashtable
    # lookup, insert, delete all O(1) (same bucket O(n))
    # insertion order (can use orderedDict)
    # must be hashable (int,str,tuple) (not list,dict)
    # dictionary is mutable

holds: {key,value}

operations:
Syntax	Meaning	Notes
d[k]	                        get value for k	                        KeyError if absent
d[k] = v	                    insert / overwrite	
d.get(k, default)	            safe lookup	returns                     None unless you pass a default
d.setdefault(k, default)	    like get,default back if key missing	One-liner for “fetch-or-create”
del d[k] / d.pop(k[, default])	delete key	
len(d)	                        item count	                            O(1)
Iteration	                    for k in d: (keys) for k,v in d.items():	Fast; produces views—live snapshots
"""

# examples for dict from chat for reference:
# Construction
d = dict(a=1, b=2)  # keyword
d = dict([("a", 1), ("b", 2)])
d = {"a": 1, "b": 2}

# Access / mutation
v = d["a"]  # KeyError if missing
v = d.get("a", 0)  # safe
d["c"] = 3
d.setdefault("d", 0)

# Delete
del d["b"]
x = d.pop("c", None)

# Views
for k, v in d.items():
    ...
keys = d.keys()
values = d.values()

# Merge (3.9+)
other = {}
combined = d | {"z": 9}  # new dict
d |= other  # in-place
