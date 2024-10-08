def celcius_to_fahrenheit(celcius):
    """Konversi Celcius ke Fahrenheit."""
    return (celcius * 9/5) + 32

def fahrenheit_to_celcius(fahrenheit):
    """Konversi Fahrenheit ke Celcius."""
    return (fahrenheit - 32) * 5/9

def celcius_to_kelvin(celcius):
    """Konversi Celcius ke Kelvin."""
    return celcius + 273.15

def kelvin_to_celcius(kelvin):
    """Konversi Kelvin ke Celcius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Konversi Fahrenheit ke Kelvin."""
    celcius = fahrenheit_to_celcius(fahrenheit)
    return celcius_to_kelvin(celcius)

def kelvin_to_fahrenheit(kelvin):
    """Konversi Kelvin ke Fahrenheit."""
    celcius = kelvin_to_celcius(kelvin)
    return celcius_to_fahrenheit(celcius)

def celcius_to_reamur(celcius):
    """Konversi Celcius ke Reamur."""
    return celcius * 4/5

def reamur_to_celcius(reamur):
    """Konversi Reamur ke Celcius."""
    return reamur * 5/4

def fahrenheit_to_reamur(fahrenheit):
    """Konversi Fahrenheit ke Reamur."""
    celcius = fahrenheit_to_celcius(fahrenheit)
    return celcius_to_reamur(celcius)

def reamur_to_fahrenheit(reamur):
    """Konversi Reamur ke Fahrenheit."""
    celcius = reamur_to_celcius(reamur)
    return celcius_to_fahrenheit(celcius)

def kelvin_to_reamur(kelvin):
    """Konversi Kelvin ke Reamur."""
    celcius = kelvin_to_celcius(kelvin)
    return celcius_to_reamur(celcius)

def reamur_to_kelvin(reamur):
    """Konversi Reamur ke Kelvin."""
    celcius = reamur_to_celcius(reamur)
    return celcius_to_kelvin(celcius)

# Input dari pengguna
suhu = float(input("Masukkan suhu: "))
dari_suhu = input("Masukkan tipe suhu dari mana (C untuk Celcius, F untuk Fahrenheit, K untuk Kelvin, R untuk Reamur): ").strip().upper()
ke_suhu = input("Masukkan tipe suhu ke mana (C untuk Celcius, F untuk Fahrenheit, K untuk Kelvin, R untuk Reamur): ").strip().upper()

# Validasi input untuk tipe suhu dari mana
if dari_suhu not in ['C', 'F', 'K', 'R']:
    print("Tipe suhu asal tidak valid. Harap masukkan C, F, K, atau R.")
else:
    # Validasi input untuk tipe suhu ke mana
    if ke_suhu not in ['C', 'F', 'K', 'R']:
        print("Tipe suhu tujuan tidak valid. Harap masukkan C, F, K, atau R.")
    else:
        if dari_suhu == 'C':
            if ke_suhu == 'F':
                print(f"{suhu}°C = {celcius_to_fahrenheit(suhu):.2f}°F")
            elif ke_suhu == 'K':
                print(f"{suhu}°C = {celcius_to_kelvin(suhu):.2f}K")
            elif ke_suhu == 'R':
                print(f"{suhu}°C = {celcius_to_reamur(suhu):.2f}°R")
            else:  # ke_suhu == 'C'
                print(f"{suhu}°C tetap {suhu}°C")
        elif dari_suhu == 'F':
            if ke_suhu == 'C':
                print(f"{suhu}°F = {fahrenheit_to_celcius(suhu):.2f}°C")
            elif ke_suhu == 'K':
                print(f"{suhu}°F = {fahrenheit_to_kelvin(suhu):.2f}K")
            elif ke_suhu == 'R':
                print(f"{suhu}°F = {fahrenheit_to_reamur(suhu):.2f}°R")
            else:  # ke_suhu == 'F'
                print(f"{suhu}°F tetap {suhu}°F")
        elif dari_suhu == 'K':
            if ke_suhu == 'C':
                print(f"{suhu}K = {kelvin_to_celcius(suhu):.2f}°C")
            elif ke_suhu == 'F':
                print(f"{suhu}K = {kelvin_to_fahrenheit(suhu):.2f}°F")
            elif ke_suhu == 'R':
                print(f"{suhu}K = {kelvin_to_reamur(suhu):.2f}°R")
            else:  # ke_suhu == 'K'
                print(f"{suhu}K tetap {suhu}K")
        elif dari_suhu == 'R':
            if ke_suhu == 'C':
                print(f"{suhu}°R = {reamur_to_celcius(suhu):.2f}°C")
            elif ke_suhu == 'F':
                print(f"{suhu}°R = {reamur_to_fahrenheit(suhu):.2f}°F")
            elif ke_suhu == 'K':
                print(f"{suhu}°R = {reamur_to_kelvin(suhu):.2f}K")
            else:  # ke_suhu == 'R'
                print(f"{suhu}°R tetap {suhu}°R")
