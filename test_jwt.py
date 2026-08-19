import jwt

from app.core.security import (
    create_access_token,
    SECRET_KEY,
    ALGORITHM
)


token = create_access_token(1)

print("TOKEN:")
print(token)

payload = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=[ALGORITHM]
)

print("PAYLOAD:")
print(payload)