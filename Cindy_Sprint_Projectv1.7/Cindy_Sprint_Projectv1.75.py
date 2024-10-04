import cmath

def calculate_roots(a, b, c):
    discriminate = b**2 - 4*a*c
    
    root_1 = cmath.sqrt(discriminate)
    root_2 = cmath.sqrt(discriminate)
    return root_1, root_2
print(calculate_complex_roots(1, 1, 1))
