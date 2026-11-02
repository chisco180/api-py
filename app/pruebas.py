# from argon2 import PasswordHasher
# from argon2.exceptions import VerifyMismatchError


# pwd_context = PasswordHasher()
# while True:
#     password_input = input("digite la contrasena:")
#     password_hashed = pwd_context.hash("metro")

#     try:
#         pwd_context.verify(password_hashed, password_input)
#         print("Contrasena correcta")
#         break
#     except VerifyMismatchError:
#         print("Contraseña incorrecta")

# print("Felicidades pegaste el ingreso de la contrasena")


import sqlalchemy

version = sqlalchemy.__version__

print(version)
