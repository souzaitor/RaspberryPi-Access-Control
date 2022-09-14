import requests


id_usuário = input()

x = requests.get('http://34.95.149.23/acesso_dc/acesso.php?card=' + id_usuário)

if x.text == 'LIBERADO':
    print("relay ligado")
else:
    print("relay desligado")