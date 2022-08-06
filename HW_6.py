# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def n_sequence(n):
    return [int(-3)**i for i in range (n+1)]

print(n_sequence(5))