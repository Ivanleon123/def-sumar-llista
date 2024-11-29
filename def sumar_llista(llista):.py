def sumar_llista(llista):
    """Suma tots els elements d'una llista."""
    total = 0
    for num in llista:
        total += num
    return total

def multiplicar_llista(llista):
    """Multiplica tots els elements d'una llista."""
    total = 1
    for num in llista:
        total *= num
    return total

# Proves de les funcions
print(sumar_llista([1, 2, 3, 4]))  # Retorna 10
print(sumar_llista([5, 5, 5]))     # Retorna 15
print(sumar_llista([-1, 1, 0]))    # Retorna 0

print(multiplicar_llista([1, 2, 3, 4]))  # Retorna 24
print(multiplicar_llista([5, 5, 5]))     # Retorna 125
print(multiplicar_llista([-1, 1, 0]))    # Retorna 0