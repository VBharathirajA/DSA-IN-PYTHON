import math
complexities = [
   ("O(1)", lambda n: 1),
   ("O(log n)", lambda n: math.log2(n)),
   ("O(n)", lambda n: n),
   ("O(n log n)", lambda n: n * math.log2(n)),
   ("O(n^2)", lambda n: n**2),
   ("O(2^n)", lambda n: 2**n),
   ("O(n!)", lambda n: math.factorial(n))
]
n = 10
for name, func in complexities:
   print(f"{name:<8} -> {func(n)} steps (n={n})")
