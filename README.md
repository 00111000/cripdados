# 🔐 CripDados - Simples criptografador de arquivos

**CripDados** é uma ferramenta simples de linha de comando desenvolvida em Python para **criptografar** e **descriptografar arquivos** com segurança usando a biblioteca `cryptography`.

---

## 🚀 Funcionalidades

- 🔒 Criptografa arquivos com uma chave gerada automaticamente.
- 🔓 Descriptografa arquivos usando a chave salva no disco.
- ✅ Interface via terminal com menu interativo.
- 💡 Armazena a chave em um arquivo chamado `chave.txt` (reutilizável).

---

## 🛠️ Requisitos

- Python 3.8+
- Biblioteca [`cryptography`](https://pypi.org/project/cryptography/)

Instale com:

```
pip install cryptography
```

📦 Como usar
Clone o repositório e execute:

```
git clone https://github.com/seu-usuario/filecrypt.git
cd filecrypt
python criptografar.py
```
🔧 Menu principal:
```
c = Criptografar arquivo
d = Descriptografar arquivo
s = Sair
```
🧠 Como funciona
Ao criptografar um arquivo:
É gerada uma chave única (Fernet key)
Essa chave é salva em chave.txt
O conteúdo do arquivo é criptografado e sobrescrito
Ao descriptografar:
A chave de chave.txt é usada
O conteúdo criptografado é restaurado ao original

⚠️ Não perca o arquivo chave.txt, ele é essencial para recuperar o conteúdo!

🎓 Autor
Desenvolvido por 00111000
