#!/usr/bin/env python3
import math

pi_numeric = math.pi
pi_approx = round(pi_numeric, 2)
computation_valid = pi_approx == 314 / 100

print("Language: Python")
print(f"Version: {3}")
print(f"Pi approx: {pi_approx:.2f}")
print(f"Computation valid: {computation_valid}")
