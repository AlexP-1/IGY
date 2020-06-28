import hashlib


def hash_generator():
    with open('countries_url.txt', 'r', encoding='utf-8') as fi:
        data = fi.readlines()
    for country in data:
        hash_country = hashlib.md5(country.encode())
        yield hash_country


for hash_country in hash_generator():
    print(hash_country.hexdigest())
