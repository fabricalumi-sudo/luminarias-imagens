import pandas as pd

# Dicionário com os produtos e seus links de imagem (imagem principal e adicionais)
produtos_imagens = {
    "Luminária LED - São paulo": {
        "principal": "https://raw.githubusercontent.com/fabricalumi-sudo/luminarias-imagens/refs/heads/main/imagens/luminaria_saopaulo.png",
        "adicionais": [
            "https://raw.githubusercontent.com/fabricalumi-sudo/luminarias-imagens/refs/heads/main/imagens/luminaria_saopaulo.png",
            "https://raw.githubusercontent.com/fabricalumi-sudo/luminarias-imagens/refs/heads/main/imagens/luminaria_saopaulo.png",
            "https://raw.githubusercontent.com/fabricalumi-sudo/luminarias-imagens/refs/heads/main/imagens/luminaria_saopaulo.png",
            "https://raw.githubusercontent.com/fabricalumi-sudo/luminarias-imagens/refs/heads/main/imagens/luminaria_saopaulo.png",
        ]
    },
}

# Lista completa de todos os produtos
produtos = list(produtos_imagens.keys())

marca = "FL FÁBRICALASER"

# Descrição do produto
descricao_produto = """Luminária LED 3D em acrílico com design exclusivo e acabamento premium. Base com luz LED RGB multicolorida controlada por botão ou controle remoto. Alimentação via USB ou pilhas. Acrílico de alta resistência com acabamento premium. Luz suave ideal para criar ambiente aconchegante. Não esquenta e tem baixa voltagem sendo seguro e econômico. Ideal para decoração de quartos, salas, escritórios, estúdios ou setups. Presente criativo e personalizável."""

# Lista de colunas de A até MF
colunas_letras = []
# Gerar colunas A-Z (26 colunas)
for i in range(26):
    colunas_letras.append(chr(65 + i))
# Gerar colunas AA-AZ (26 colunas)
for i in range(26):
    colunas_letras.append('A' + chr(65 + i))
# Gerar colunas BA-BZ (26 colunas)
for i in range(26):
    colunas_letras.append('B' + chr(65 + i))
# Gerar colunas CA-CZ (26 colunas)
for i in range(26):
    colunas_letras.append('C' + chr(65 + i))
# Gerar colunas DA-DZ (26 colunas)
for i in range(26):
    colunas_letras.append('D' + chr(65 + i))
# Gerar colunas EA-EZ (26 colunas)
for i in range(26):
    colunas_letras.append('E' + chr(65 + i))
# Gerar colunas FA-FZ (26 colunas)
for i in range(26):
    colunas_letras.append('F' + chr(65 + i))
# Gerar colunas GA-GZ (26 colunas)
for i in range(26):
    colunas_letras.append('G' + chr(65 + i))
# Gerar colunas HA-HZ (26 colunas)
for i in range(26):
    colunas_letras.append('H' + chr(65 + i))
# Gerar colunas IA-IZ (26 colunas)
for i in range(26):
    colunas_letras.append('I' + chr(65 + i))
# Gerar colunas JA-JZ (26 colunas)
for i in range(26):
    colunas_letras.append('J' + chr(65 + i))
# Gerar colunas KA-KZ (26 colunas)
for i in range(26):
    colunas_letras.append('K' + chr(65 + i))
# Gerar colunas LA-LZ (26 colunas)
for i in range(26):
    colunas_letras.append('L' + chr(65 + i))
# Gerar colunas MA-MF (6 colunas) = Total: 26*12 + 6 = 318 colunas
for i in range(6):  # MA-MF
    colunas_letras.append('M' + chr(65 + i))

linhas = []

for i, produto in enumerate(produtos, start=1):
    time_nome = produto.replace('Luminária LED - ', '')
    nome_produto = f"Luminária LED 3D Acrílico Abajur {time_nome}"
    sku = f"FL-{i:03d}"
    
    # Obter imagem principal do produto
    imagens_data = produtos_imagens.get(produto, {})
    imagem_principal = imagens_data.get("principal", "")
    
    # Criar linha com o número correto de colunas (318)
    linha = [''] * len(colunas_letras)
    
    # Preencher apenas as colunas especificadas nas posições CORRETAS
    linha[0] = sku  # A: SKU
    linha[1] = "Criar ou substituir (atualização completa)"  # B
    linha[2] = "LAMP"  # C
    linha[3] = nome_produto  # D: nome_produto
    linha[4] = "FL FÁBRICALASER"  # E
    linha[5] = "Isento de GTIN"  # F
    # G vazio (posição 6)
    linha[7] = "Casa > Iluminação > Abajures e Luminárias > Abajures (17406464011)"  # H
    linha[8] = "Casa > Iluminação > Abajures e Luminárias > Abajures (17406464011)"  # I
    linha[9] = "Casa > Iluminação > Abajures e Luminárias > Luminárias de Mesa (17355089011)"  # J
    linha[10] = "Casa > Iluminação > Abajures e Luminárias > Abajures (17406464011)"  # K
    linha[11] = "Casa > Iluminação > Abajures e Luminárias > Abajures (17406464011)"  # L
    # M vazio (posição 12)
    linha[13] = 1  # N
    # O vazio (posição 14)
    linha[15] = marca  # P: marca
    # Q vazio (posição 16)
    linha[17] = "Novo"  # R
    # S vazio (posição 18)
    linha[19] = 59.9  # T: preço
    # U vazio (posição 20)
    linha[21] = "Modelo padrão da Amazon"  # V
    # W, X, Y vazios
    linha[25] = imagem_principal  # Z: imagem principal
    # W até AZ vazios
    # BA vazio
    linha[53] = "DEFAULT"  # BB = 26 + 1 = 53
    linha[54] = 1000  # BC = 26 + 2 = 54
    # BD até BF vazios
    linha[58] = 59.9  # BG = 26 + 6 = 58
    # BH até BO vazios
    linha[67] = descricao_produto  # BP = 26 + 15 = 67
    linha[68] = "Luminaria para decoração"  # BQ = 26 + 16 = 68
    # BR até CL vazios
    linha[90] = 1  # CM = 26*2 + 12 = 90
    # CN até CR vazios
    linha[96] = "Branco"  # CS = 26*2 + 18 = 96
    # CT até CZ vazios
    linha[104] = 1  # DA = 26*3 + 0 = 104
    # DB até DL vazios
    linha[127] = "Alimentado por pilha"  # DX = 26*3 + 19 = 97
    linha[174] = "Cabo de energia"  #fs
    
  

    
    linha[244] = 15  # IK
    linha[245] = "centímetros"  # IL
    linha[246] = 15  # IM
    linha[247] = "centímetros"  # IN
    linha[248] = 5  # IO
    linha[249] = "centímetros"  # IP
    linha[256] = "Brasil"  # IW
    linha[281] = "Não aplicável"  
    linha[297] = "INMETRO: 0000; ANATEL: 0000; Não aplicável"  

   
    linhas.append(linha)

# Criar DataFrame
df = pd.DataFrame(linhas, columns=colunas_letras)

# Escrever para Excel
df.to_excel("produtos_amazon_final.xlsx", index=False)

print("Arquivo 'produtos_amazon_atualizado.xlsx' criado com sucesso!")
print(f"Total de produtos: {len(produtos)}")
print("Formato Amazon com colunas A-MF aplicado!") 