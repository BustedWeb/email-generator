import random
import pandas as pd

def gen_emails(n: int, output_file: str = "emails.txt"):
    names = pd.read_csv("nombres.txt")["name"].tolist()
    lastnames = pd.read_csv("apellidos.txt")["lastname"].tolist()
    domains = ['gmail.com']

    generated = set()

    while len(generated) < n:
        name = random.choice(names)
        lastname = random.choice(lastnames)
        domain = random.choice(domains)

        if random.choice([True, False]):
            if random.choice([True, False]):
                lastname += str(random.randint(1, 99))
            else:
                name += random.choice(['_', '-'])

        email = f"{name}{lastname}@{domain}".lower()
        if email not in generated:
            generated.add(email)

    with open(output_file, "w") as f:
        for email in generated:
            f.write(email + "\n")

    return output_file