from app.core.security import hash_password, verify_password


password = "MyPassword123"

hashed = hash_password(password)

print("Original:", password)
print("Hash:", hashed)

print("Correct password:",
      verify_password("MyPassword123", hashed))

print("Wrong password:",
      verify_password("WrongPassword", hashed))