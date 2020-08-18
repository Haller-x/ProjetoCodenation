#Desafio Prático CodeNation
###Por Germano Yoneda

Para começar faça o download dos arquivos:
[Mercado](https://codenation-challenges.s3-us-west-1.amazonaws.com/ml-leads/estaticos_market.csv.zip)
[Portifólio 1](https://codenation-challenges.s3-us-west-1.amazonaws.com/ml-leads/estaticos_portfolio1.csv)
[Portifólio 2](https://codenation-challenges.s3-us-west-1.amazonaws.com/ml-leads/estaticos_portfolio2.csv)
[Portifólio 3](https://codenation-challenges.s3-us-west-1.amazonaws.com/ml-leads/estaticos_portfolio3.csv)

Então clone o repositório:
```sh
git clone https://github.com/Haller-x/ProjetoCodenation.git
```
Então crie um ambiente virtual, eu usei o anaconda:
```sh
conda create --name envname python=3.7
conda activate envname
```
Instale na pasta que foi baixada abra o terminal e execute:
```sh
pip install -r requirements.txt
```

## Descrição dos arquivos projeto
-`preprocessing.ipynb` Jupyter notebook que processa os dados: remove colunas,
	preenche dados NaN, e cria um novo `csv` que será usado no `modelo_final.ipynb`

-`modelo_final.ipynb` Jupyter notebook que aplica o LabelEncoder, avalia o número de clusters ideal e cria o modelo.
	Também gera arquivos csv de mercado e de cada portifólio, ambos com a coluna de cluster já atribuída (apenas com as colunas utilizadas).


-`streamlit_view.py` Utiliza o arquivo de mercado gerado pelo `modelo_final.ipynb` para buscar os ID's e avaliar as características.
	* Foi realizado dessa forma pela limitação de performance do streamlit*

# Streamlit:
	- Após executar os jupyter notebooks `preprocessing.ipynb` e `modelo_final.ipynb` digite no terminal:
```sh
streamlit run streamlit_view.py
```