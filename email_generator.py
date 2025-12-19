import random
import string


class EmailGenerator:
    def __init__(self):
        self.domains = [
            "gmail.com", "gmx.de", "yahoo.com", "outlook.com", "icloud.com",
            "hotmail.com", "web.de", "aol.com", "mail.ru", "protonmail.com"
        ]

    def generate_random_name(self, length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def generate_random_email(self):
        random_name = self.generate_random_name(random.randint(5, 15))
        random_domain = random.choice(self.domains)
        return f"{random_name}@{random_domain}"