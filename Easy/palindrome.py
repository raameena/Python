from collections import deque
x = 121
"""
:type x: int
:rtype: bool
        """

palx = deque(list(str(x)))

reversex = deque([])
chars = list(str(x))
for x in chars:
    reversex.appendleft(x)
    print(x)

print(palx == reversex)
