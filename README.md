# Learning Python

## Python Basics 1: Core Data Types Pt 1, Control Flow

### 1. Numbers, text, booleans, truth values
- Hashable/Not hashable:
   - Hashable:
      - Does not mutate
      - int, string, bool, tuple, frozenset
   - Nothashable:
      - Mutable
      - list, set
- do not need to specify the type in Python, does it automatically (formatting matters)
- examples provided in file

### 2. If, elif, for loops, for else, while
- format for all are in file ( very important )
- colon instead of semi colon 

### 3. Basic functions
- (f"") formatting:
   - (f"Hello, my name is {name} and I am {age} years old.")
   - Makes it so you don't have to add + between variables, simple cleaner
- Text Edit:
   - variable.upper() : VARIABLE
   - variable.lower() : variable
   - variable.title() : Variable
- Whitespace:
   - variable.strip() : removes white space from front and end
   - variable.lstrip() : "    variable"
   - variable.rstrip() : "variable    "
- Manipulation/Find:
   - variable.replace(these letters, w these)
   - print(variable.find("var") : returns index
   - print("var" in variable) : True
   - print("hi" in variable : False

## Python Basics 2: Core Data Types Pt 2

### 1. List, Tuples, Range
- Vocab:
   - Dynamic Array: can be resized at runtime
   - Static Array: fixed size
   - Hash(): Makes uniqe key that can be used to check for repeats in memory

- List:
    - can change size, ordred, dynamic array
    - index[#] O(1)
    - append [back] O(1)
    - pop [front] O(n) - have to move everything back (deque is O(1))
    - shift [middle] O(n)
    - in sequence O(n)
- Tuple:
    - cannot change tuple size, but can change elements stored in them (unhashable), fixed record/hashable, only read cannot add
    - index[#] O(1)
    - in sequence O(n)
    - can be mutable with [] ONLY - not hashable bc its changed after runtime
- Range:
    - loops/slicing, (start,stop,step) arthmetically
    - index[#] O(1)
    - in sequence O(1)

### 3. Set/Frozenset
- Notes:
  - Dict: short for dictionary ( look up )
  - Cannot have two of the same elements in either set (only multiset)
  - Uses {}
- Sets:
    - mutable, membership and uniqness
    - x in set O(1) // hash, search for uniqness
    - add remove O(1)
    - can use math:   ( fast membership )
        - (|) union
        - (&) intersection
        - (-) difference
        - (^) symetric difference
    - unordered
    - cant store unashable items (lists) - use frozenset or tuples
    0 cannot be used for hash
- Frozenset:
    - not mutable, hashable "set of things" you can use as a dict key
    - immutable
    - has composite key, constant lookup
    - slightly faster bc immutable
    - can do union, etc., but make a new frozenset ( not mutable )  

### 4. Dict
- Notes:
    - Short for "dictionary"
    - holds: {key,value}
    - uses curly braces
- Dict:
    - Mappng: each key is unique
    - Keys are hashed -> place in hash bucket, make a hashtable
    - lookup, insert, delete all O(1) (same bucket O(n))
    - insertion order (can use orderedDict)
    - must be hashable (int,str,tuple) (not list,dict)
    - dictionary is mutable

## Python Basics 3: Functions
- Notes:
   - def: used to define functions
   - "First class": can be used in functions or as parameter
 
### 1. Default: 
- Ex. (var = 5)
- can be overridden

### 2. Keyword Only Args
- Ex. (*, var = 10)
- Anything after * must be defined when calling

### 3. *Args
- Examples + Explanation:
   - I. (*var, this = 5)
   - II. (1,2,3,4,5, this = 5) this must be defined afterwards
   - Explanation: program creates tuple with *var (1,2,3,4,5) 
- var must be list, tuple, set
   - (will be unpacked)
