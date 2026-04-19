import os

diretorio = os.path.dirname(os.path.abspath(__file__))
print(f"Pasta atual: {diretorio}")
print("Arquivos encontrados nesta pasta:")
print(os.listdir(diretorio))

arquivo_alvo = "seguranca.log"
if os.path.exists(os.path.join(diretorio, arquivo_alvo)):
    print(f"\n✅ O arquivo {arquivo_alvo} foi encontrado!")
else:
    print(f"\n❌ O arquivo {arquivo_alvo} NÃO foi encontrado.")