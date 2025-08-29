                             PROJETO DE ANÁLISE EXPLORATÓRIA DE DADOS – IMDB

<p align="center">
  <img src="images/mao-segurando-objetos-de-entretenimento-isolados.jpg" alt="Cinema" width="900"/>
</p>


Este projeto realiza uma Análise Exploratória de Dados (EDA) no dataset desafio_indicium_imdb.csv, explorando estatísticas, visualizações e testes iniciais de modelagem preditiva.

O notebook contém etapas de preparação de dados, gráficos exploratórios, análise de texto (WordCloud) e modelos de Machine Learning básicos (Regressão, Random Forest e XGBoost).

---

ESTRUTURA DO PROJETO
```
Projeto
├── EDA.ipynb                
├── save_trained_models.py    
├── load_trained_models.py   
├── modelos_pkl/              
│   ├── cat_pipe.pkl
│   ├── num_log_pipe.pkl
│   ├── num_plain_pipe.pkl
│   └── pipe.pkl
├── desafio_indicium_imdb.csv
└── requirements.txt          #
```

---
INSTALAÇÃO
1. Clone o repositório
```
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado)
```
# Criar ambiente virtual
python -m venv .venv

# Ativar (Linux/Mac)
source .venv/bin/activate

# Ativar (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

3. Instale as dependências

As bibliotecas necessárias estão listadas em requirements.txt. Para instalar:
```
pip install -r requirements.txt
```

Exemplo de requirements.txt (gerado via pip freeze):
```
matplotlib==3.9.2
numpy==2.1.1
pandas==2.2.3
scikit-learn==1.5.2
scipy==1.14.1
seaborn==0.13.2
wordcloud==1.9.3
xgboost==2.1.1
```
---
EXECUÇÃO

Certifique-se de que o arquivo desafio_indicium_imdb.csv está na raiz do projeto.

Inicie o Jupyter Notebook:
```
jupyter notebook
```

Abra o arquivo EDA.ipynb e execute as células na ordem para reproduzir as análises.


---


TECNOLOGIAS USADAS

Python 3.12 (recomendado)

Jupyter Notebook

Pandas – manipulação de dados

NumPy – operações numéricas

Matplotlib / Seaborn – visualizações gráficas

Scikit-learn – pré-processamento e modelagem

WordCloud – geração de nuvem de palavras

XGBoost – algoritmo de gradient boosting

---
REPRODUTIBILIDADE

Se você adicionar ou atualizar bibliotecas, lembre-se de atualizar o requirements.txt:
```
pip freeze > requirements.txt
```

Assim, quem clonar o repositório poderá recriar exatamente o mesmo ambiente.

Salvando Modelos

Os modelos são salvos utilizando o script save_trained_models.py.
No final do seu notebook, após treinar os modelos/pipelines, basta rodar:
```
from save_trained_models import save_models, quick_report

saved, skipped, errors = save_models(
    globals(),
    ["cat_pipe", "num_log_pipe", "num_plain_pipe", "pipe"],  # nomes das variáveis dos modelos
    outdir="modelos_pkl"
)

quick_report(saved, skipped, errors)
```

---
RESULTADO ESPERADO

Os modelos serão salvos dentro da pasta modelos_pkl/:
```
modelos_pkl/cat_pipe.pkl
modelos_pkl/num_log_pipe.pkl
modelos_pkl/num_plain_pipe.pkl
modelos_pkl/pipe.pkl
```

---
CARREGANDO OS MODELOS

Para reabrir os modelos salvos, utilize o script load_trained_models.py:
```
from load_trained_models import load_models

# Carrega os modelos em um dicionário
models = load_models(["cat_pipe", "num_log_pipe", "num_plain_pipe", "pipe"])

# Exemplo: acessando o modelo principal (pipe)
pipe_model = models["pipe"]

# Fazendo previsões
y_pred = pipe_model.predict(X_test)
```

---
BOAS PRÁTICAS

- Sempre reexecute o notebook antes de salvar os modelos, garantindo que todos foram treinados.

- Para reprodutibilidade, mantenha as versões de bibliotecas fixadas em requirements.txt.
