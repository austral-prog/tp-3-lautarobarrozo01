def check_vowels():
    # Código a implementar utilizando input.
    nombre = input().lower()
    print("Contiene a: " + str("a" in nombre))
    print("Contiene e: " + str("e" in nombre))
    print("Contiene i: " + str("i" in nombre))
    print("Contiene o: " + str("o" in nombre))
    print("Contiene u: " + str("u" in nombre))


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
