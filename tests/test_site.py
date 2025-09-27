# Importando as bibliotecas necessárias
import pytest
from bs4 import BeautifulSoup

# Lendo o arquivo HTML principal do projeto
with open('index.html', 'r') as f:
    html_doc = f.read()

# O BeautifulSoup "parseia" o HTML, transformando-o em um objeto que podemos inspecionar
soup = BeautifulSoup(html_doc, 'html.parser')

# --- Nossos 5 Testes Unitários ---

# Teste 1: Verifica se o título da página está correto
def test_titulo_da_pagina():
    """Verifica se a tag <title> contém o texto esperado."""
    assert soup.title.string == "Meu Portfólio"

# Teste 2: Verifica se o cabeçalho principal (h1) existe e está correto
def test_cabecalho_principal():
    """Verifica se a tag <h1> existe e contém o nome correto."""
    h1_tag = soup.find('h1')
    assert h1_tag is not None
    assert h1_tag.string == "Meu Nome"

# Teste 3: Verifica se o subtítulo (h2) existe
def test_subtitulo_existe():
    """Verifica se a tag <h2>, que representa o cargo, existe."""
    h2_tag = soup.find('h2')
    assert h2_tag is not None

# Teste 4: Verifica se a seção de projetos existe
def test_secao_projetos_existe():
    """Verifica se existe uma seção com o título 'Meus Projetos'."""
    h3_projetos = soup.find('h3', string="Meus Projetos")
    assert h3_projetos is not None

# Teste 5: Verifica se há pelo menos dois projetos na lista
def test_numero_minimo_de_projetos():
    """Verifica se a lista de projetos (<ul>) contém pelo menos dois itens (<li>)."""
    lista_projetos = soup.find('ul')
    assert lista_projetos is not None
    assert len(lista_projetos.find_all('li')) >= 2
