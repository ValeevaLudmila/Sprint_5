import random
import string

class EmailPasswordGenerator:
    def __init__(self):
        self.email = None
        self.password = None

    def generate(self):
        if self.email is None and self.password is None:
            email_length = random.randint(5, 10)
            self.email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length)) + "@example.com"

            password_length = random.randint(8, 12)
            self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

        return self.email, self.password