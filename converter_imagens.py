import requests
import os
from PIL import Image
import io

# URLs das imagens WebP originais
urls_webp = [
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0050_2_11zon.webp",  # Palmeiras
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0061_13_11zon.webp",  # Santos
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0068_20_11zon.webp",  # Gremio
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0074_26_11zon.webp",  # Internacional
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0082_34_11zon.webp",  # Vasco
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0090_42_11zon.webp",  # Corinthians
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0097_49_11zon.webp",  # São Paulo
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0102_54_11zon.webp",  # Cruzeiro
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0117_69_11zon.webp",  # Flamengo
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0123_75_11zon.webp",  # Botafogo
    "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0131_83_11zon.webp",  # Fluminense
]

# Nomes dos times para os arquivos
times = [
    "palmeiras", "santos", "gremio", "internacional", "vasco",
    "corinthians", "saopaulo", "cruzeiro", "flamengo", "botafogo", "fluminense"
]

# Criar pasta para as imagens
os.makedirs("imagens", exist_ok=True)

print("Baixando e convertendo imagens...")

# URLs GitHub que serão geradas
urls_github = []

for i, (url, time) in enumerate(zip(urls_webp, times)):
    try:
        print(f"Processando {time}...")
        
        # Baixar a imagem WebP
        response = requests.get(url)
        response.raise_for_status()
        
        # Converter WebP para PNG
        img = Image.open(io.BytesIO(response.content))
        
        # Salvar como PNG
        nome_arquivo = f"luminaria_{time}.png"
        caminho_arquivo = os.path.join("imagens", nome_arquivo)
        img.save(caminho_arquivo, "PNG")
        
        # Gerar URL do GitHub
        url_github = f"https://raw.githubusercontent.com/fabricalumi-sudo/luminarias-imagens/main/imagens/{nome_arquivo}"
        urls_github.append(url_github)
        
        print(f"✓ {time} convertido para PNG")
        
    except Exception as e:
        print(f"✗ Erro ao processar {time}: {e}")
        urls_github.append("")

print("\n" + "="*50)
print("COMANDOS PARA SUBIR NO GITHUB:")
print("="*50)
print("cd imagens")
print("git add .")
print('git commit -m "Add luminarias PNG images"')
print("git push")

print("\n" + "="*50)
print("URLS DO GITHUB GERADAS:")
print("="*50)
for time, url in zip(times, urls_github):
    print(f"{time}: {url}")

print("\n" + "="*50)
print("PRÓXIMOS PASSOS:")
print("="*50)
print("1. Execute os comandos git acima")
print("2. Aguarde o upload terminar")
print("3. Execute: python atualizar_excel.py")
print("="*50)

# Salvar URLs para usar no próximo script
with open("urls_github.txt", "w") as f:
    for url in urls_github:
        f.write(url + "\n")

print(f"\nTotal: {len([u for u in urls_github if u])} imagens convertidas com sucesso!") 