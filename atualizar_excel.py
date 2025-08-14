import pandas as pd

# Ler as URLs do GitHub
with open("urls_github.txt", "r") as f:
    urls_github = [line.strip() for line in f.readlines()]

# Mapeamento dos produtos para as URLs
produtos_urls = {
    "Luminária LED - Palmeiras": urls_github[0],
    "Luminária LED - Santos": urls_github[1],
    "Luminária LED - Gremio": urls_github[2],
    "Luminária LED - Internacional": urls_github[3],
    "Luminária LED - Vasco": urls_github[4],
    "Luminária LED - Corinthians": urls_github[5],
    "Luminária LED - São paulo": urls_github[6],
    "Luminária LED - Cruzeiro": urls_github[7],
    "Luminária LED - Flamengo": urls_github[8],
    "Luminária LED - Botafogo": urls_github[9],
    "Luminária LED - Fluminense": urls_github[10],
}

# Atualizar o dicionário no arquivo amazon_produtos.py
print("Atualizando amazon_produtos.py com URLs do GitHub...")

# Ler o arquivo atual
with open("amazon_produtos.py", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Substituir as URLs WebP pelas URLs GitHub PNG
for produto, url_github in produtos_urls.items():
    # Encontrar a URL WebP atual no código
    inicio = conteudo.find(f'"{produto}": {{')
    if inicio != -1:
        fim = conteudo.find('}', inicio)
        secao_produto = conteudo[inicio:fim+1]
        
        # Encontrar a URL principal atual
        inicio_principal = secao_produto.find('"principal": "') + len('"principal": "')
        fim_principal = secao_produto.find('"', inicio_principal)
        url_atual = secao_produto[inicio_principal:fim_principal]
        
        # Substituir no conteúdo completo
        conteudo = conteudo.replace(url_atual, url_github)
        print(f"✓ {produto} atualizado")

# Salvar o arquivo atualizado
with open("amazon_produtos.py", "w", encoding="utf-8") as f:
    f.write(conteudo)

print("\n" + "="*50)
print("ARQUIVO ATUALIZADO!")
print("="*50)
print("Execute: python amazon_produtos.py")
print("Para gerar o Excel com URLs do GitHub!")
print("="*50) 