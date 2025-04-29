import streamlit as st
import requests

def buscar_cep(cep):
    respuesta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return respuesta

st.set_page_config(
    page_title="Busca CEP",
    page_icon="✉️"
)
st.title("Sistema de busca de CEP")
st.divider()

menu = st.sidebar
cep = menu.text_input("Digite o CEP")
boton = menu.button("Pesquisar")

if boton:
    respuesta = buscar_cep(cep)
    
    if respuesta.status_code == 200:
        st.success("CEP encontrado con suceso!!", icon="✅")
        datos = respuesta.json()

        col1, col2 = st.columns(2)

        col1.markdown(f"**CEP:** {datos['cep']}")
        col1.markdown(f"**Logradouro:** {datos['logradouro']}")
        col1.markdown(f"**Complemento:** {datos['complemento']}")
        col1.markdown(f"**Unidade:** {datos['unidade']}")
        col1.markdown(f"**Bairro:** {datos['bairro']}")
        col1.markdown(f"**Localidade:** {datos['localidade']}")
        col1.markdown(f"**UF:** {datos['uf']}")
        col2.markdown(f"**Estado:** {datos['estado']}")
        col2.markdown(f"**Regiao:** {datos['regiao']}")
        col2.markdown(f"**IBGE:** {datos['ibge']}")
        col2.markdown(f"**GIA:** {datos['gia']}")
        col2.markdown(f"**DDD:** {datos['ddd']}")
        col2.markdown(f"**Siafi:** {datos['siafi']}")
        st.balloons()
    else:
        st.error("O CEP informado e invalido", icon="❌")

