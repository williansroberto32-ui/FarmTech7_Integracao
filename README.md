# FarmTech Solutions — Fase 7: Integração

Projeto acadêmico da FIAP que reúne os serviços das Fases 1 a 6 em uma única estrutura e oferece uma dashboard Streamlit para acessar os módulos, consultar a previsão agrícola e enviar alertas por e-mail usando AWS SNS.

> A aplicação contém dados agrícolas demonstrativos. A Fase 2 abre a simulação ESP32 no Wokwi; a Fase 3 disponibiliza os scripts Oracle; e a Fase 6 abre o notebook de visão computacional e exibe os resultados salvos. O envio de alertas AWS depende de um tópico SNS e de credenciais temporárias válidas do Learner Lab.

## Integrantes

Confiram os nomes completos e RMs antes da publicação:

| Integrante | RM |
|---|---:|
| Willians | 573314 |
| Maurício | 571019 |
| Fernando | 569974 |
| Matheus | 572385 |
| Felipe | 564288 |

## Estrutura

```text
FarmTech7_Integracao/
├── fase1_dados/                  # AgroSmart Analytics e CSV de resultados
├── fase2_iot/                    # ESP32, circuito e arquivos Wokwi
├── fase3_oracle/                 # Scripts SQL e documentação do banco
├── fase4_dashboard/              # Dashboard Streamlit e previsão por regressão
├── fase5_aws/                    # Publicação de alertas AWS SNS
├── fase6_visao_computacional/    # Notebook YOLO, matrizes e resultados
├── evidencias/                   # Capturas da configuração AWS
├── requirements.txt
└── README.md
```

## Executar a dashboard

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run fase4_dashboard/main.py
```

No macOS/Linux:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run fase4_dashboard/main.py
```

## Módulos disponíveis

- **Fase 1 — Dados:** informa cultura, dimensões do terreno, produtividade, preço e custo; o painel executa `fase1_dados/main.py` e registra o resultado no CSV.
- **Fase 2 — IoT:** abre a simulação Wokwi do ESP32, com DHT22, LDR, botões NPK e relé para irrigação simulada.
- **Fase 3 — Oracle:** permite baixar os scripts SQL para execução no Oracle SQL Developer. A dashboard não conecta ao banco automaticamente.
- **Fase 4 — Dashboard e previsão:** mostra a base simulada, métricas do modelo de regressão, gráficos e simulador de produtividade.
- **Fase 5 — Alertas AWS:** monta uma mensagem com umidade, pH e ação recomendada e a publica no tópico SNS configurado.
- **Fase 6 — Visão computacional:** abre o notebook no Colab e mostra os resultados e a matriz de confusão salvos na pasta.

## Configurar o alerta AWS SNS

1. No AWS Academy/Learner Lab, crie um tópico SNS Standard e registre uma assinatura de e-mail. Confirme a inscrição pelo e-mail recebido.
2. Copie a região e o ARN do tópico para uso local. A função de envio lê `AWS_REGION` e `FARMTECH_SNS_TOPIC_ARN` do ambiente.
3. Ative o Learner Lab e configure no terminal local as credenciais temporárias indicadas no painel da AWS (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` e `AWS_SESSION_TOKEN`). Não cole credenciais no código, no README ou no GitHub. As credenciais expiram quando a sessão termina.
4. Abra a dashboard e use **Fase 5 - Alertas AWS** para publicar uma notificação de demonstração.

Exemplo para definir as variáveis não secretas no PowerShell:

```powershell
$env:AWS_REGION = "REGIAO_DO_TOPICO"
$env:FARMTECH_SNS_TOPIC_ARN = "ARN_DO_TOPICO_SNS"
```

As variáveis de credencial devem ser preenchidas somente com os valores temporários fornecidos pelo Learner Lab, na sessão local ativa. Não salve esses valores em arquivos versionados. O boto3 utiliza a cadeia padrão de credenciais da AWS.

## Evidências AWS

Adicionar em `evidencias/` capturas do tópico SNS, região, assinatura confirmada e publicação de teste. Não incluir capturas que exponham access keys, tokens, senhas ou outros segredos. Descrever no vídeo a configuração e demonstrar o recebimento do e-mail.

## Vídeo demonstrativo

Publicar no YouTube como **não listado**, com duração de até 10 minutos, mostrando a dashboard, os módulos, a previsão e o alerta. Inserir o link aqui e no arquivo `.txt` enviado no Portal do Aluno.

**Link do vídeo:** preencher após publicar.

## Entrega

O repositório deve permanecer privado e ser compartilhado com o perfil `fiap-tutoria`. No Portal do Aluno, enviar somente um arquivo `.txt` contendo o link do repositório privado e o link do vídeo não listado.

## Observações

- Os valores do modelo e os limites de recomendação da dashboard são demonstrativos e devem ser ajustados à cultura e às condições reais do solo.
- A conversão do LDR para pH e as leituras de NPK são simulações, não medições agronômicas reais.
- Não versionar credenciais, tokens AWS, `.env`, pastas `.venv` ou `__pycache__`.

## Status da integração AWS SNS

O tópico SNS foi criado e a inscrição do e-mail foi confirmada. No teste de envio pela aplicação, ocorreu um erro de resposta do Botocore. Por isso, não foi possível confirmar o recebimento do alerta por e-mail.