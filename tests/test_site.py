# Importando as bibliotecas necessárias
import pytest
from bs4 import BeautifulSoup
import os  # <-- Importação adicionada

# --- Início da Alteração ---
# Construindo o caminho absoluto para index.html com base no diretório atual do script de teste
# Isso garante que o caminho funcione, independentemente de onde o pytest seja executado.
base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, 'index.html')

# Lendo o arquivo HTML principal do projeto
# Usamos o caminho construído (html_path) em vez de apenas 'index.html'
try:
    with open(html_path, 'r', encoding='utf-8') as f: # Adicionado encoding='utf-8' para robustez
        html_doc = f.read()
except FileNotFoundError:
    # Se o arquivo não for encontrado no caminho esperado, podemos levantar um erro mais claro
    # ou, para o propósito do teste rodar, você pode querer apenas que o teste falhe.
    # No entanto, para fins de correção, manter a leitura direta do arquivo é o objetivo.
    # Vou manter a leitura simples.
    pass

# O BeautifulSoup "parseia" o HTML, transformando-o em um objeto que podemos inspecionar
# Adicionamos uma verificação simples caso a leitura falhe
if 'html_doc' in locals():
    soup = BeautifulSoup(html_doc, 'html.parser')
else:
    # Cria um objeto BeautifulSoup vazio se a leitura falhar para evitar NameError nos testes
    soup = BeautifulSoup('', 'html.parser')
# --- Fim da Alteração ---

# --- Nossos 5 Testes Unitários ---

# Teste 1: Verifica se o título da página está correto
def test_titulo_da_pagina():
    """Verifica se a tag <title> contém o texto esperado."""
    # Adicionamos um 'if' para garantir que 'soup.title' não seja None, embora o assert do string já ajude
    if soup.title:
        assert soup.title.string == "Meu Portfólio"
    else:
        # Força o teste a falhar se a página não foi carregada (ou o título não existe)
        assert False, "Tag <title> não encontrada ou arquivo HTML não carregado."

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
