# script que calcula o ip para realizar a mascara do mesmo.
def calculate_subnet_mask(ip_address, prefix_length):
    if prefix_length < 0 or prefix_length > 32:
        raise ValueError("O comprimento do prefixo deve estar entre 0 e 32.")

    # Converte o endereço IP para uma lista de inteiros
    ip_parts = list(map(int, ip_address.split('.')))

    # Calcula a máscara de sub-rede
    mask = 0xffffffff ^ (1 << 32 - prefix_length) - 1

    # Converte a máscara para o formato de endereço IP
    mask_parts = []
    for _ in range(4):
        mask_parts.insert(0, str(mask & 255))
        mask >>= 8

    return ".".join(mask_parts)

if __name__ == "__main__":
    try:
        ip_address = input("Informe o endereço IP: ")
        prefix_length = int(input("Informe o comprimento do prefixo da máscara de sub-rede (0-32): "))

        subnet_mask = calculate_subnet_mask(ip_address, prefix_length)
        print("Máscara de sub-rede:", subnet_mask)
    except ValueError as e:
        print("Erro:", e)