import cmath

def calculate_roots(a, b, c):
    discriminate = (b**2 - 4*a*c) 
    
    root_1 = (-b+cmath.sqrt(discriminate)/(2*a))
    root_2 = (-b-cmath.sqrt(discriminate)/(2*a))
    return root_1, root_2

if discriminate > 0:
    print("There are two roots: (root_1) and (root_2)")
elif discriminate == 0:
    print("There are one real root at (root_1)")
else:
    return root_1, root_2

print(calculate_roots(1, 2, 1))
print(calculate_roots(1, 5, 6))