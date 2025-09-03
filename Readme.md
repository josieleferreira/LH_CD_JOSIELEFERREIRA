                             PROJETO DE ANÁLISE EXPLORATÓRIA DE DADOS – IMDB


Este projeto realiza uma Análise Exploratória de Dados (EDA) no dataset imdb.csv, explorando estatísticas, visualizações e testes iniciais de modelagem preditiva.

O notebook contém etapas de preparação de dados, gráficos exploratórios, análise de texto (WordCloud) e modelos de Machine Learning básicos (Regressão e Random Forest).

---

ESTRUTURA DO PROJETO
```
LH_CD_JOSIELE/
│── dados/                
│── notebook/              
│   └── case_imdb.ipynb
│── artifacts/             
│   ├── imdb_rf_*.pkl
│   └── imdb_rf_*_meta.json
│── reports/              
│   └── Apresentação IMDB.pdf
│── requirements.txt       
│── Readme.md          
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

Certifique-se de que o arquivo imdb.csv está na raiz do projeto.

Inicie o Jupyter Notebook:
```
jupyter notebook notebook/case_imdb.ipynb

```

Abra o arquivo case_imdb.ipynb e execute as células na ordem para reproduzir as análises.


---


TECNOLOGIAS USADAS

Python 3.12.3

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

Para recarregar o modelo salvo
```
import joblib
model = joblib.load("artifacts/imdb_rf_<timestamp>.pkl")
pred = model.predict([seu_input])
```

---
RESULTADO ESPERADO

Modelagem:

- Diferentes algoritmos foram avaliados.

- O modelo escolhido foi o Random Forest Regressor (RF), por apresentar melhor desempenho no conjunto de validação

Métricas de teste:

- RMSE = 0.197

- MAE = 0.150

- R² = 0.41

Os modelos serão salvos dentro da pasta artifacts:
```
imdb_rf_20250903-153913_meta.json
imdb_rf_20250903-153913.pkl
```

---
RESULTADOS E CONCLUSÕES

- O modelo conseguiu capturar parcialmente a relação entre variáveis e a nota no IMDB, alcançando um R² de ~0.41.

- Principais fatores relacionados ao sucesso de um filme: número de votos, metascore, gênero e sinopse.

- Apesar do dataset relativamente pequeno, a solução demonstra o uso de Machine Learning aplicado em regressão real.

---

BOAS PRÁTICAS

- Sempre reexecute o notebook antes de salvar os modelos, garantindo que todos foram treinados.

- Para reprodutibilidade, mantenha as versões de bibliotecas fixadas em requirements.txt.
