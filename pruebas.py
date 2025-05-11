import itertools
import hashlib

def brute_force_password(target_hash, max_length=8):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for length in range(1, max_length + 1):
        for password_tuple in itertools.product(characters, repeat=length):
            guess = ''.join(password_tuple)
            # print(f"Probando: {guess}")  # Descomenta si quieres ver cada intento
            if hashlib.sha256(guess.encode()).hexdigest() == target_hash:
                return guess
    return None

# Ejemplo de uso
target_password = "abca234"  # Usa una contraseña de hasta 8 caracteres
target_hash = hashlib.sha256(target_password.encode()).hexdigest()

# CORREGIDO: max_length ahora es 8
found_password = brute_force_password(target_hash, max_length=8)

print(f"La contraseña encontrada es: {found_password}")
