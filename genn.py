import random
import string


# script que gera chaves aleatorias ai é só ficar testando para ver se funciona.
def generate_key():
    key_parts = []
    for _ in range(5):
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        key_parts.append(part)
    return '-'.join(key_parts)

def generate_keys(quantity):
    keys = [generate_key() for _ in range(quantity)]
    return keys

def save_keys_to_file(keys):
    with open('keys.txt', 'w') as file:
        for key in keys:
            file.write(key + '\n')

if __name__ == "__main__":
    try:
        quantity = int(input("Informe a quantidade de chaves que deseja gerar: "))
        if quantity <= 0:
            raise ValueError("A quantidade de chaves deve ser maior que zero.")
        
        keys = generate_keys(quantity)
        save_keys_to_file(keys)
        print(f"{quantity} chaves foram geradas e salvas no arquivo keys.txt.")
    except ValueError as e:
        print("Erro:", e)
