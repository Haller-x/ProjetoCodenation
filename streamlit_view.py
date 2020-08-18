import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showfileUploaderEncoding', False)

def generate_plot(df,column):
    plt.figure(figsize=[8,8])
    plt.title("Distribuição da coluna: {}".format(column))
    sns.countplot(y=df[column].values)
    plt.xlabel('Quantidade de Ocorrências')
    plt.ylabel('Valores')
    plt.show()
    return st.pyplot()

def main():
    st.title('Projeto Final CodeNation')
    st.sidebar.image(Image.open('img/codenationbanner.png'),width=200)
    st.sidebar.text('Desenvolvido por Germano Yoneda')
    file = st.sidebar.file_uploader('Upload csv file',type='csv',)
    if file:
        df = pd.read_csv(file)
        df_portifolio= pd.DataFrame(df)
        columns = df_portifolio.columns
        ids_portifolio = df_portifolio.iloc[:,1].tolist()
        market = pd.read_csv('market_cluster.csv')
        portifolio_cluster = market.loc[market.iloc[:,0].isin(ids_portifolio),:]
        lista_remover = ['de_faixa_faturamento_estimado','de_faixa_faturamento_estimado_grupo', 'vl_faturamento_estimado_aux','qt_filiais']
        market = market.drop(lista_remover,axis=1)
        chart_options = st.sidebar.multiselect('Escolha os gráficos que gostaria de ver:',market.columns[1::])
        if chart_options == 0 or chart_options==True:
            for options in chart_options:
                generate_plot(portifolio_cluster,options)
        st.sidebar.markdown('''---------''')
        st.sidebar.text('Gráficos por Cluster')
        chosen_cluster = st.sidebar.selectbox('Selecione um cluster para avaliar:',portifolio_cluster['Clusters'].value_counts().index,index=0)
        if chosen_cluster == 0 or chosen_cluster==True:
            df_chosen_cluster = portifolio_cluster.loc[portifolio_cluster.Clusters== chosen_cluster,:]
            charts_clusters = st.sidebar.multiselect('Escolha os gráficos que gostaria de ver:',market.columns[1:-1:])
            if charts_clusters:
                    for options in charts_clusters:
                        generate_plot(df_chosen_cluster,options)

if __name__ == '__main__':
    main()