from math import pow


def calculate_emi(p, r, n):
    r = r / (12 * 100)
    return p * r * pow(1 + r, n) / (pow(1 + r, n) - 1)
