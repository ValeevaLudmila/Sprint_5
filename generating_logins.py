import random
import string

class EmailPasswordGenerator:
    def generate(self):
        # Генерируем случайный email
        email_length = random.randint(5, 10)
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length)) + "@example.com"

        # Генерируем случайный пароль (минимум 8 символов)
        password_length = random.randint(8, 12)
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

        return email, password

# Функции для обратной совместимости
def generate_email():
    return EmailPasswordGenerator().generate()[0]

def generate_password():
    return EmailPasswordGenerator().generate()[1]