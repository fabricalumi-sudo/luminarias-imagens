import pandas as pd

# Dicionário com os produtos e seus links de imagem (imagem principal e adicionais)
produtos_imagens = {
    "Luminária LED - Palmeiras": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0050_2_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0050_2_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0049_1_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0051_3_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0052_4_11zon.webp",
        ]
    },
    "Luminária LED - Santos": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0061_13_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0061_13_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0056_8_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0057_9_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0058_10_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0059_11_11zon.webp",
        ]
    },
    "Luminária LED - Gremio": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0068_20_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0068_20_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0065_17_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0064_16_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0063_15_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0066_18_11zon.webp",
        ]
    },
    "Luminária LED - Internacional": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0074_26_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0074_26_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0071_23_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0069_21_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0070_22_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0072_24_11zon.webp",
        ]
    },
    "Luminária LED - Vasco": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0082_34_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0082_34_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0075_27_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0078_30_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0077_29_11zon.webp",
        ]
    },
    "Luminária LED - Corinthians": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0090_42_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0090_42_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0083_35_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0084_36_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0085_37_11zon.webp",
        ]
    },
    "Luminária LED - São paulo": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0097_49_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0097_49_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0091_43_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0089_41_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0092_44_11zon.webp",
        ]
    },
    "Luminária LED - Cruzeiro": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0102_54_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0102_54_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0099_51_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0098_50_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0096_48_11zon.webp",
        ]
    },
    "Luminária LED - Flamengo": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0117_69_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0117_69_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0111_63_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0112_64_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0113_65_11zon.webp",
        ]
    },
    "Luminária LED - Botafogo": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0123_75_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0123_75_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0120_72_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0118_70_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0121_73_11zon.webp",
        ]
    },
    "Luminária LED - Fluminense": {
        "principal": "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0131_83_11zon.webp",
        "adicionais": [
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0131_83_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0126_78_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0128_80_11zon.webp",
            "http://www.fabricalumi.com.br/media/catalog/product/i/m/img-20250715-wa0127_79_11zon.webp",
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
    # BD até BO vazios
    linha[67] = descricao_produto  # BP = 26 + 15 = 67
    linha[68] = "Luminaria para decoração"  # BQ = 26 + 16 = 68
    # BR até CL vazios
    linha[90] = 1  # CM = 26*2 + 12 = 90
    # CN até CR vazios
    linha[96] = "Branco"  # CS = 26*2 + 18 = 96
    # CT até CZ vazios
    linha[104] = 1  # DA = 26*3 + 0 = 104
    # DB até DL vazios
    linha[116] = "Alimentado por pilha"  # DM = 26*3 + 12 = 116
    # DN até FG vazios
    linha[163] = "Cabo de energia"  # FH = 156 + 7 = 163
    # FI até HS vazios
    linha[227] = 5.0  # HT = 208 + 19 = 227
    linha[228] = "centímetros"  # HU = 208 + 20 = 228
    linha[229] = 20.0  # HV = 208 + 21 = 229
    linha[230] = "centímetros"  # HW = 208 + 22 = 230
    linha[231] = 15  # HX = 208 + 23 = 231
    linha[232] = "centímetros"  # HY = 208 + 24 = 232
    # HZ até IE vazios
    linha[239] = "Brasil"  # IF = 26*8 + 5 = 239
    # IG até JD vazios
    linha[264] = "Não aplicável"  # JE = 26*9 + 4 = 264
    # JF até JQ vazios
    linha[277] = 250.0  # JR = 26*9 + 17 = 277
    linha[278] = "Gramas"  # JS = 26*9 + 18 = 278
    # JT vazio
    linha[280] = "INMETRO: 0000; ANATEL: 0000; Não aplicável"  # JU = 26*9 + 20 = 280
    
    linhas.append(linha)

# Criar DataFrame
df = pd.DataFrame(linhas, columns=colunas_letras)

# Escrever para Excel
df.to_excel("produtos_amazon_atualizado.xlsx", index=False)

print("Arquivo 'produtos_amazon_atualizado.xlsx' criado com sucesso!")
print(f"Total de produtos: {len(produtos)}")
print("Formato Amazon com colunas A-MF aplicado!") 