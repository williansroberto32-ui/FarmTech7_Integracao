🌱 FarmTech Vision | FIAP — Fase 6

## 🎥 Vídeo de apresentação

Assista à demonstração do projeto FarmTech Vision, apresentando YOLO, CNN e os resultados obtidos:

[▶️ Assistir ao vídeo no YouTube](https://youtu.be/KAMchSnCNTw)

💻 Notebook completo no Google Colab

O notebook original contém os códigos, treinamentos, gráficos, testes e análises das Entregas 1 e 2 do projeto FarmTech Vision.

[▶️ Abrir notebook completo no Google Colab](https://colab.research.google.com/drive/1-IoLx01Z3ldkd7XAfPfp8b4Ct-jAo6Tk?usp=sharing)

Observação: o arquivo original também está disponível neste repositório, mas, devido ao seu tamanho, pode não ser exibido diretamente pelo GitHub.

**Dataset e resultados — Google Drive**

[📂 Acessar dataset e resultados do FarmTech Vision](https://drive.google.com/drive/folders/1lw_90JsEhRCuIaEEDhY7vsptgCgL0i8n?usp=sharing)

A pasta compartilhada contém as imagens, anotações e resultados dos experimentos realizados nas Entregas 1 e 2.

🎯 Sobre o projeto

O FarmTech Vision é um projeto acadêmico desenvolvido no curso de Tecnólogo em Inteligência Artificial da FIAP, com foco em Visão Computacional e aplicação de modelos de Inteligência Artificial para identificação de produtos em imagens.

O projeto utiliza duas classes de produtos: Coca-Cola e cereal Nescau, explorando diferentes técnicas de detecção e classificação.

🔍 Objetivo

Desenvolver, treinar e avaliar modelos de visão computacional, comparando três abordagens:

1. YOLO tradicional: modelo pré-treinado para detecção genérica de objetos.
2. YOLO personalizado: modelo treinado especificamente para identificar e localizar Coca-Cola e cereal Nescau.
3. Rede Neural Convolucional (CNN): modelo para classificação das imagens entre as duas classes.

🛠️ Tecnologias utilizadas

- Python
- Google Colab
- Ultralytics YOLO
- TensorFlow / Keras
- OpenCV
- NumPy e Matplotlib
- Scikit-learn
- Make Sense AI
- GitHub

📁 Dataset

Foram utilizadas 80 imagens, distribuídas da seguinte forma:

Conjunto| Quantidade
Treinamento| 64 imagens
Validação| 8 imagens
Teste| 8 imagens
Total| 80 imagens

As classes utilizadas foram "Coca_Cola" e "Cereal".

As imagens destinadas ao treinamento do YOLO personalizado foram anotadas com caixas delimitadoras, permitindo identificar a posição dos objetos.

🚀 Entrega 1 — YOLO personalizado

Na primeira entrega, foram realizados dois treinamentos do modelo YOLO, utilizando 30 e 60 épocas.

Comparação dos treinamentos

Métrica| 30 épocas| 60 épocas
Precision| 0,956| 0,957
Recall| 0,936| 0,927
mAP50| 0,936| 0,938
mAP50-95| 0,736| 0,786
Tempo registrado| 129,65 s| 221,06 s

O treinamento de 60 épocas apresentou melhor resultado em mAP50-95, indicando maior precisão na localização dos objetos sob critérios mais exigentes.

O tempo médio de inferência registrado para o modelo personalizado foi de 4,76 ms por imagem, nas condições avaliadas no Google Colab.

🧠 Entrega 2 — Comparação de modelos

Na segunda entrega, foram analisadas três abordagens de visão computacional.

YOLO tradicional

O modelo pré-treinado realizou 18 detecções nas oito imagens avaliadas, com tempo médio de inferência de 5,4 ms.

Entretanto, apresentou dificuldades para identificar corretamente os produtos específicos, realizando algumas classificações genéricas inadequadas.

YOLO personalizado

O modelo treinado com 60 épocas apresentou:

- Precision: 0,957
- Recall: 0,927
- mAP50: 0,938
- mAP50-95: 0,786

Os resultados demonstraram desempenho promissor na identificação e localização dos produtos estudados.

Rede Neural Convolucional (CNN)

A CNN foi treinada durante 15 épocas para classificar as imagens entre Coca-Cola e cereal Nescau.

Na avaliação registrada, apresentou:

- Acurácia no teste: 100%
- Perda no teste: 0,1603
- Imagens avaliadas: 8
- Classificações corretas: 8

Embora a CNN tenha acertado todas as imagens do conjunto de teste, o número reduzido de amostras limita a capacidade de generalização das conclusões.

📊 Comparação final

Modelo| Finalidade| Resultado
YOLO tradicional| Detecção genérica| 18 detecções em 8 imagens
YOLO personalizado| Detecção e localização dos produtos| mAP50 de 0,938
CNN| Classificação de imagens| 100% de acurácia em 8 imagens

Os modelos YOLO realizam detecção e localização de objetos, enquanto a CNN desenvolvida neste projeto realiza classificação de imagens. Portanto, as métricas devem ser interpretadas considerando essas diferenças.

📓 Notebooks do projeto

Notebook otimizado — visualização no GitHub:

"FarmTech_Vision_Fase6_GitHub.ipynb" (FarmTech_Vision_Fase6_GitHub.ipynb)

Notebook original:

"FarmTech_Vision_Fase6_pbl_fase6.ipynb" (FarmTech_Vision_Fase6_pbl_fase6.ipynb)

A versão otimizada mantém o código e as análises, mas não inclui as saídas de execução armazenadas, como gráficos e imagens geradas. Essas evidências precisam ser reproduzidas ao executar as células no ambiente configurado.

⚠️ Limitações e melhorias futuras

O conjunto de dados utilizado é relativamente pequeno, especialmente para avaliar a capacidade de generalização dos modelos.

Como melhorias futuras, destacam-se:

- Ampliar a quantidade e a diversidade das imagens.
- Realizar testes em diferentes condições de iluminação e posicionamento.
- Avaliar os modelos em novos conjuntos de dados independentes.
- Organizar e disponibilizar evidências visuais dos experimentos.
- Aprimorar a reprodutibilidade do projeto.

🎓 Instituição

FIAP — Tecnólogo em Inteligência Artificial

Projeto acadêmico — Fase 6

FarmTech Vision | Inteligência Artificial e Visão Computacional

👥 Integrantes do Grupo — FIAP

Integrante| RM
Maurício| 571019
Fernando| 569974
Willians| 573314
Matheus| 572385
Felipe| 564288

Curso: Tecnólogo em Inteligência Artificial
Instituição: FIAP
Projeto: FarmTech Vision — Fase 6
