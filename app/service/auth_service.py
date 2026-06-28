from app.config.security import create_access_token


class AuthService:

    def login(self, username, password):

        if username == "admin" and password == "1234":

            token = create_access_token({"sub": username})

            return {
                "access_token": token,
                "token_type": "bearer"
            }

        raise ValueError("Contraseña incorrecta")