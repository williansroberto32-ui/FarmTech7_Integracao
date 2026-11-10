# 🌱 FarmTech Solutions — Fase 3

## Banco de Dados Oracle para Monitoramento Agrícola

Projeto acadêmico desenvolvido no curso de Inteligência Artificial da FIAP, utilizando Oracle SQL Developer.

## 🎯 Objetivo
Organizar e consultar dados coletados por sensores agrícolas, apoiando o monitoramento das condições de cultivo e futuras integrações com o sistema FarmTech.

## 🛠️ Tecnologias
- Oracle Database
- Oracle SQL Developer
- Linguagem SQL

## 📊 Estrutura dos dados
A tabela `TB_SENSOR_DADOS` contém:

- `ID_SENSOR`: identificador do registro e chave primária.
- `TIPO_SENSOR`: tipo do sensor.
- `VALOR_MEDICAO`: valor registrado.
- `UNIDADE_MEDIDA`: unidade da medição.
- `DATA_COLETA`: data e hora da coleta.

O projeto considera medições agrícolas, como temperatura, umidade, pH e nutrientes NPK, além do contexto de irrigação.

## 📁 Arquivos
- `farmtech3_banco_dados.sql`: script principal e consultas.
- `farmtech3_banco_dados_backup.sql`: cópia de segurança do script.
- `farmtech3_estrutura_tabela.sql`: definição simplificada da tabela.

## 🔎 Consulta SQL
```sql
SELECT *
FROM TB_SENSOR_DADOS
ORDER BY ID_SENSOR;
```

## 🔗 Próximos passos
Integrar os dados do projeto às demais etapas do FarmTech Solutions, conforme os requisitos da Fase 7.

## 👨‍💻 Autor
Willians Roberto da Silva — FIAP