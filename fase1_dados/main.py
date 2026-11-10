# AgroSmart Analytics
# Projeto: autoral de portfolio - Inteligência Artificial 
# Sistema para gestão e análise de dados agrícolas 
import csv
import os

print("=" * 50)
print(" AgroSmart Analytics") 
print(" Gestão Inteligente de dados agrícolas")
print("=" * 50)

culturas = ["Café", "Cana-de-açúcar"] 
print("\nCulturas disponíveis:")
print(f"1 - {culturas[0]}")
print(f"2 - {culturas[1]}")
while True:
    opcao = input("\nEscolha uma cultura (1 ou 2): ")
    if opcao == "1":
        print(f"Você Selecionou: {culturas[0]}")
        break
    elif opcao == "2":
        print(f"Você Selecionou: {culturas[1]}")
        break
    else:
        print("Opção inválida. Tente novamente.")
cultura_escolhida = culturas[int(opcao) - 1]
print("\n--- Calculo da area de plantio ---")
comprimento = float(input("Informe o comprimento do terreno em metros: "))
largura = float(input("Informe a largura do terreno em metros: "))
area_m2 = comprimento * largura
area_hectares = area_m2 / 10000
print(f"\nCultura Selecionada: {cultura_escolhida}")
print(f"Área total: {area_m2:.2f} m²")
print(f"Área total: {area_hectares:.4f} hectares")

print("\n--- Estimativa de produção ---")
produtividade = float(input("Informe a produtividade esperada (toneladas por hectare): "))
producao_estimada = area_hectares * produtividade
print(f"Produtividade informada: {produtividade:.2f} t/ha")
print(f"Produção estimada: {producao_estimada:.2f} toneladas")

print("\n--- Estimativa de receita ---")
preco_tonelada = float(input("Informe o preço estimado por tonelada (R$): "))
receita_estimada = producao_estimada * preco_tonelada
print(f"Preço por tonelada: R$ {preco_tonelada:.2f}")
print(f"Receita estimada: R$ {receita_estimada:.2f}")

print("\n--- Análise de custos e lucro ---")
custo_hectare = float(input("Informe o custo de produção por hectare (R$): "))
custo_total = area_hectares * custo_hectare
lucro_estimado = receita_estimada - custo_total
print(f"Custo total de produção: R$ {custo_total:.2f}")
print(f"Lucro estimado: R$ {lucro_estimado:.2f}")

print("\n" + "=" * 50)
print("Resumo - AgroSmart Analytics")
print("=" * 50)
print(f"Cultura: {cultura_escolhida}")
print(f"Area plantada: {area_hectares:.4f} hectares")
print(f"Produção estimada: {producao_estimada:.2f} toneladas")
print(f"Receita estimada: R$ {receita_estimada:.2f}")
print(f"Custo total: R$ {custo_total:.2f}")
print(f"Lucro estimado: R$ {lucro_estimado:.2f}")
print("=" * 50)
print("\n--- Situação Financeira ---")
if lucro_estimado > 0:
    print("Resultado: Lucro")
elif lucro_estimado == 0:
    print("Resultado: Equilíbrio")
else:
    print("Resultado: Prejuízo")

if receita_estimada != 0:
    margem_lucro = (lucro_estimado / receita_estimada) * 100
    print(f"Margem de lucro: {margem_lucro:.2f}%")
else:
    print("Margem de lucro: nao pode ser calculada porque a receita é zero)")
    margem_lucro = "Nao calculada"

# Salvando resultados em CSV
nome_arquivo = "resultados_agrosmart.csv"
arquivo_existe = os.path.exists(nome_arquivo)
with open(nome_arquivo, mode="a", newline="", encoding="utf-8") as arquivo_csv:
    writer = csv.writer(arquivo_csv)

    if not arquivo_existe:
        writer.writerow(["Cultura", "Area (ha)", "Produção (t)", "Receita (R$)", "Custo (R$)", "Lucro (R$)", "Margem de Lucro (%)"])

    writer.writerow([cultura_escolhida, area_hectares, producao_estimada, receita_estimada, custo_total, lucro_estimado, margem_lucro])