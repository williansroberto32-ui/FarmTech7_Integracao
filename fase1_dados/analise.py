import csv
import matplotlib.pyplot as plt

cultturas = []
lucros = []
margens = []

with open("resultados_agrosmart.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        cultturas.append(linha["Cultura"])
        lucros.append(float(linha["Lucro (R$)"]))
        margens.append(float(linha["Margem de Lucro (%)"]))

# Grafico de lucro por cultura

plt.figure(figsize=(8, 5))
plt.bar(cultturas, lucros, color='skyblue')
plt.title("Lucro por Cultura")
plt.xlabel("Cultura")
plt.ylabel("Lucro (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafico de margem de lucro por cultura
plt.figure(figsize=(8, 5))
plt.bar(cultturas, margens, color='lightgreen')
plt.title("Margem de Lucro por Cultura")
plt.xlabel("Cultura")
plt.ylabel("Margem de Lucro (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()