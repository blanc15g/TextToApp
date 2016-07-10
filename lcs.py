

def findOverlap(nouns, title):
    a = nouns.lower().split()
    b = title.lower().split()
    return lcs(a,b)

def lcs(a,b):
    if len(a) == 0 or len(b) == 0:
        return []
    if a[-1] == b[-1]:
        return lcs(a[:-1],b[:-1]) + [a[-1]]
    opt1 = lcs(a[:-1],b)
    opt2 = lcs(a,b[:-1])
    if len(opt1) > len(opt2):
        return opt1
    return opt2

print(findOverlap('five guys delivery alexandria', 'Five Guys Burgers and Fries - Order Delivery - Burgers - Old Town Alexandria - Alexandria, VA - 21 Photos & 83 Reviews - Phone Number - Menu - Yelp'))

# def lcs(a, b):
#     """Returns the length of the Longest cd common subsequence of a and b"""
#     lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
#     # row 0 and column 0 are initialized to 0 already
#     for i, x in enumerate(a):
#         for j, y in enumerate(b):
#             if x == y:
#                 lengths[i+1][j+1] = lengths[i][j] + 1
#             else:
#                 lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
#     # read the substring out from the matrix
#     result = 0
#     x, y = len(a), len(b)
#     while x != 0 and y != 0:
#         if lengths[x][y] == lengths[x-1][y]:
#             x -= 1
#         elif lengths[x][y] == lengths[x][y-1]:
#             y -= 1
#         else:
#             assert a[x-1] == b[y-1]
#             result = 1 + result
#             x -= 1
#             y -= 1
#     return result
