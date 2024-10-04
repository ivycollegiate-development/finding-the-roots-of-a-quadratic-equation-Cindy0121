import cmath

def calculate_roots(a, b, c):
    discriminate = (b**2 - 4*a*c) **0.5
    
    root_1 = (-b+(discriminate)/(2*a))
    root_2 = (-b-(discriminate)/(2*a))
    return root_1, root_2
print(calculate_complex_roots(1, 2, 1))
print(calculate_complex_roots(1, 5, 6))