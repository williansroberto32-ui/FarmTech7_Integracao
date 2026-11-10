
# ==================================================
# FARMTECH 4 - PREVISAO INTELIGENTE
# FIAP - Inteligencia Artificial
# Projeto FarmTech Solutions
# ==================================================

# Etapa 1 - Preparacao do ambiente

import pandas as pd
import numpy as np

print("=" * 50)
print("FARMTECH SOLUTIONS - PREVISAO INTELIGENTE")
print("=" * 50)

print("\nIniciando sistema de analise agricola...")

# Configuracao para reproducibilidade
np.random.seed(42)

print("Ambiente inicial configurado com sucesso!")

# ==================================================
# Etapa 2 - Dados agricolas de exemplo
# ==================================================

dados = pd.DataFrame({
    "umidade": [30, 45, 60, 35, 70, 55, 40, 65, 50, 75],
    "ph": [5.5, 6.0, 6.5, 5.8, 6.8, 6.2, 5.9, 6.7, 6.1, 7.0],
    "irrigacao": [10, 15, 20, 12, 25, 18, 14, 22, 17, 27],
    "fertilizante": [5, 8, 10, 6, 12, 9, 7, 11, 8, 13],
    "produtividade": [20, 30, 42, 25, 50, 38, 28, 46, 35, 53]
})

print("\nDADOS AGRICOLAS:")
print(dados)

print("\nRESUMO ESTATISTICO:")
print(dados.describe())

# ==================================================
# Etapa 3 - Preparacao para Machine Learning
# ==================================================

# Variaveis de entrada
X = dados[["umidade", "ph", "irrigacao", "fertilizante"]]

# Variavel que queremos prever
y = dados["produtividade"]

print("\nVARIAVEIS DE ENTRADA:")
print(X.head())

print("\nVARIAVEL ALVO - PRODUTIVIDADE:")
print(y.head())

print("\nDados preparados para Machine Learning!")

# ==================================================
# Etapa 4 - Treinamento do modelo de regressao
# ==================================================

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Separar dados de treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Criar o modelo
modelo = LinearRegression()

# Treinar a Inteligencia Artificial
modelo.fit(X_treino, y_treino)

print("\nTREINAMENTO DO MODELO:")
print("Modelo de Regressao Linear treinado com sucesso!")

print("\nRegistros para treinamento:", len(X_treino))
print("Registros para teste:", len(X_teste))
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Gerar previsões para os dados de teste
y_previsto = modelo.predict(X_teste)

# Calcular as métricas de desempenho
mae = mean_absolute_error(y_teste, y_previsto)
mse = mean_squared_error(y_teste, y_previsto)
rmse = mse ** 0.5
r2 = r2_score(y_teste, y_previsto)

print("\nAVALIAÇÃO DO MODELO:")
print(f"MAE:  {mae:.2f}")
print(f"MSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.2f}")
import streamlit as st

st.set_page_config(
    page_title="FarmTech 7 - Sistema Integrado",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 FarmTech Solutions — Sistema Integrado")
st.subheader("FarmTech 7 | Consolidação das Fases 1 a 6")
st.caption(
    "Painel demonstrativo com previsão agrícola, acesso aos serviços das fases "
    "anteriores e notificações AWS SNS."
)

st.info(
    "A base possui apenas 10 registros simulados. "
    "As previsões e recomendações são demonstrativas."
)

st.subheader("Desempenho do modelo")
col1, col2, col3, col4 = st.columns(4)
col1.metric("MAE", f"{mae:.2f}")
col2.metric("MSE", f"{mse:.2f}")
col3.metric("RMSE", f"{rmse:.2f}")
col4.metric("R²", f"{r2:.2f}")

st.subheader("Dados agrícolas")
st.dataframe(dados)

st.subheader("Relação entre variáveis agrícolas e produtividade")
grafico1, grafico2 = st.columns(2)

with grafico1:
    st.markdown("**Umidade e produtividade**")
    st.scatter_chart(
        dados,
        x="umidade",
        y="produtividade",
        color="ph"
    )

with grafico2:
    st.markdown("**Irrigação e produtividade**")
    st.scatter_chart(
        dados,
        x="irrigacao",
        y="produtividade",
        color="fertilizante"
    )

st.subheader("Simulador de produtividade")
st.caption(
    "Os limites das recomendações são demonstrativos e devem ser ajustados "
    "conforme a cultura e as condições do solo."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    umidade_nova = st.number_input(
        "Umidade (%)", min_value=0, max_value=100, value=50
    )

with col2:
    ph_novo = st.number_input(
        "pH", min_value=0.0, max_value=14.0, value=6.0, step=0.1
    )

with col3:
    irrigacao_nova = st.number_input(
        "Irrigação (valor simulado)", min_value=0, value=15
    )

with col4:
    fertilizante_novo = st.number_input(
        "Fertilizante (valor simulado)", min_value=0, value=8
    )

if st.button("Prever produtividade"):
    novo_cenario = pd.DataFrame({
        "umidade": [umidade_nova],
        "ph": [ph_novo],
        "irrigacao": [irrigacao_nova],
        "fertilizante": [fertilizante_novo]
    })

    previsao = modelo.predict(novo_cenario)[0]
    st.metric("Produtividade prevista", f"{previsao:.2f}")

    if umidade_nova < 40:
        st.warning("Umidade baixa: avalie a necessidade de irrigação.")
    elif umidade_nova >= 70:
        st.info("Umidade elevada: acompanhe o solo antes de irrigar.")
    else:
        st.success("Umidade dentro da faixa usada nesta demonstração.")

    if ph_novo < 5.5 or ph_novo > 7.0:
        st.warning("Confira o pH do solo e as necessidades da cultura.")
        # ==================================================
# FarmTech 7 - Serviços integrados
# ==================================================
from pathlib import Path
import subprocess
import sys

raiz_projeto = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(raiz_projeto / "fase5_aws"))
st.header("Serviços integrados do FarmTech")

aba1, aba2, aba3, aba5, aba6 = st.tabs([
    "Fase 1 - Dados",
    "Fase 2 - IoT",
    "Fase 3 - Oracle",
    "Fase 5 - Alertas AWS",
    "Fase 6 - Visão Computacional"
])

with aba1:
    st.subheader("AgroSmart Analytics")
    st.caption("Informe os dados para executar o serviço da Fase 1.")

    with st.form("form_fase1"):
        cultura = st.selectbox("Cultura", ["Café", "Cana-de-açúcar"])
        comprimento = st.number_input(
            "Comprimento do terreno (m)", min_value=0.1, value=100.0
        )
        largura = st.number_input(
            "Largura do terreno (m)", min_value=0.1, value=50.0
        )
        produtividade = st.number_input(
            "Produtividade esperada (t/ha)", min_value=0.0, value=10.0
        )
        preco = st.number_input(
            "Preço estimado por tonelada (R$)", min_value=0.0, value=1000.0
        )
        custo = st.number_input(
            "Custo de produção por hectare (R$)", min_value=0.0, value=5000.0
        )
        executar_fase1 = st.form_submit_button("Executar AgroSmart")

    if executar_fase1:
        pasta_fase1 = raiz_projeto / "fase1_dados"
        entradas = "\n".join([
            "1" if cultura == "Café" else "2",
            str(comprimento),
            str(largura),
            str(produtividade),
            str(preco),
            str(custo)
        ]) + "\n"

        try:
            resultado = subprocess.run(
                [sys.executable, str(pasta_fase1 / "main.py")],
                input=entradas,
                text=True,
                capture_output=True,
                cwd=str(pasta_fase1),
                timeout=30
            )
            st.code(resultado.stdout or resultado.stderr)

            if resultado.returncode == 0:
                st.success("Serviço da Fase 1 concluído.")
            else:
                st.error("O serviço da Fase 1 retornou um erro.")
        except Exception as erro:
            st.error(f"Não foi possível executar a Fase 1: {erro}")

with aba2:
    st.subheader("Monitoramento IoT e irrigação")
    st.write(
        "O circuito usa ESP32, DHT22, LDR e relé. "
        "A simulação da Fase 2 é executada no Wokwi."
    )
    st.link_button(
        "Abrir simulação da Fase 2 no Wokwi",
        "https://wokwi.com/projects/479071299180016641"
    )

with aba3:
    st.subheader("Scripts do banco Oracle")
    st.write("Baixe um script para abrir e executar no Oracle SQL Developer.")

    arquivos_sql = [
        "farmtech3_estrutura_tabela.sql",
        "farmtech3_banco_dados.sql",
        "farmtech3_banco_dados_backup.sql"
    ]

    colunas_sql = st.columns(3)
    for coluna, nome_arquivo in zip(colunas_sql, arquivos_sql):
        caminho_sql = raiz_projeto / "fase3_oracle" / nome_arquivo
        if caminho_sql.exists():
            coluna.download_button(
                label=f"Baixar {nome_arquivo}",
                data=caminho_sql.read_bytes(),
                file_name=nome_arquivo,
                mime="text/plain",
                key=f"download_{nome_arquivo}"
            )

with aba6:
    st.subheader("FarmTech Vision")
    st.write(
        "O notebook otimizado e os resultados da Fase 6 estão organizados "
        "na pasta do projeto."
    )
    st.link_button(
        "Abrir notebook da Fase 6 no Google Colab",
        "https://colab.research.google.com/drive/1-IoLx01Z3ldkd7XAfPfp8b4Ct-jAo6Tk?usp=sharing"
    )

    pasta_fase6 = raiz_projeto / "fase6_visao_computacional"
    imagem_resultados = pasta_fase6 / "results.png"
    matriz_confusao = pasta_fase6 / "confusion_matrix.png"

    if imagem_resultados.exists():
        st.image(
            str(imagem_resultados),
            caption="Resultados do modelo de visão computacional",
            width="stretch"
        )

    if matriz_confusao.exists():
        st.image(
            str(matriz_confusao),
            caption="Matriz de confusão",
            width="stretch"
        )

with aba5:
    st.subheader("Alertas agrícolas por e-mail")
    st.caption(
        "O alerta utiliza os valores de umidade e pH informados "
        "no simulador da Fase 4."
    )

    if umidade_nova < 40:
        nivel = "ALERTA DE IRRIGAÇÃO"
        recomendacao = (
            "Umidade abaixo do limite de demonstração. "
            "Avaliar a necessidade de irrigação."
        )
    else:
        nivel = "MONITORAMENTO"
        recomendacao = (
            "Umidade acima do limite de demonstração. "
            "Continuar monitorando o solo."
        )

    mensagem = (
        f"FarmTech 7 - {nivel}\n"
        f"Umidade do solo: {umidade_nova:.1f}%\n"
        f"pH do solo: {ph_novo:.2f}\n"
        f"Recomendação: {recomendacao}"
    )

    st.write(f"**Condição:** {nivel}")
    st.write(f"**Recomendação:** {recomendacao}")

    if st.button("Enviar notificação AWS SNS", key="enviar_alerta_sns"):
        try:
            from notificacao_sns import enviar_alerta

            id_mensagem = enviar_alerta(
                mensagem,
                assunto="FarmTech 7 - alerta agrícola",
            )
            st.success(f"Notificação enviada. ID: {id_mensagem}")
        except Exception as erro:
            st.error(f"Não foi possível enviar a notificação: {erro}")

    st.info(
        "Para enviar de verdade, configure o tópico SNS e as credenciais "
        "temporárias do AWS Academy/Learner Lab no ambiente, sem gravá-las "
        "no código ou no GitHub."
    )
