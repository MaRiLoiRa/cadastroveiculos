import streamlit as st
import pandas as pd
from datetime import datetime
import io


# Inicializa uma lista para armazenar os carros
if 'carros' not in st.session_state:
    st.session_state.carros = []


# Título do aplicativo
st.title('🚗 Anotações de Carros Pernoite')
st.subheader('Adicione os detalhes abaixo:')


# Formulário para adicionar informações do carro
with st.form(key='carro_form'):
    col1, col2 = st.columns(2)
    with col1:
        modelo = st.text_input('Modelo do Carro').upper()
        cor = st.text_input('Cor').upper()
    with col2:
        placa = st.text_input('Placa').upper()
        localizacao = st.text_input('Localização onde está parado').upper()
    
    
    # Botão para adicionar o carro
    submit_button = st.form_submit_button('Adicionar Carro')

    # Validação dos campos
    if submit_button:
        if modelo and cor and placa and localizacao:
            data_atual = datetime.now().strftime('%d/%m/%y')
            st.session_state.carros.append({
                'Modelo': modelo,
                'Cor': cor,
                'Placa': placa,
                'Localização': localizacao,
                'Data': data_atual
            })
            st.success('Carro adicionado!')
        else:
            st.error('Por favor, preencha todos os campos antes de adicionar o carro.')

# Exibir a lista de carros
if st.session_state.carros:
    st.subheader('📝 Carros Adicionados:')
    df_carros = pd.DataFrame(st.session_state.carros)
    st.write(df_carros)

    # Cria um arquivo Excel em memória
    output = io.BytesIO()
    df_carros.to_excel(output, index=False, engine='openpyxl')
    output.seek(0)

    # Botão para baixar o arquivo Excel
    st.download_button(
        label='Baixar Arquivo Excel',
        data=output,
        file_name='carros.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


# Estilo CSS
st.markdown("""
<style>
    .stButton { margin: 15px; }
    .stTextInput { margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)
