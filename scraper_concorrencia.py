import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time

# Configuração de log para aspecto profissional no terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [SISTEMA] - %(message)s')

def extrair_dados_produtos(url_alvo):
    """Varre a página alvo e extrai informações cruas dos produtos."""
    logging.info(f"Conectando ao servidor alvo: {url_alvo}")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        resposta = requests.get(url_alvo, headers=headers)
        resposta.raise_for_status() # Verifica se a conexão foi bem sucedida
        
        soup = BeautifulSoup(resposta.text, 'html.parser')
        produtos_extraidos = []
        
        # Encontra todos os blocos de produtos na página
        blocos = soup.find_all('article', class_='product_pod')
        logging.info(f"{len(blocos)} produtos localizados. Iniciando extração...")
        
        for bloco in blocos:
            # Extrai título, preço e estoque
            titulo = bloco.h3.a['title']
            preco_texto = bloco.find('p', class_='price_color').text
            preco = float(preco_texto.replace('£', '').replace('Â', '').strip())
            estoque = bloco.find('p', class_='instock availability').text.strip()
            
            produtos_extraidos.append({
                'Nome_Produto': titulo,
                'Preco_Varejo': preco,
                'Status_Estoque': estoque,
                'Data_Coleta': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')
            })
            
        return produtos_extraidos

    except Exception as e:
        logging.error(f"Falha na extração: {e}")
        return []

def gerar_relatorio(dados, nome_arquivo="relatorio_precos.csv"):
    """Transforma a lista de dicionários em um arquivo CSV estruturado usando Pandas."""
    if not dados:
        logging.warning("Nenhum dado para exportar.")
        return

    df = pd.DataFrame(dados)
    
    # Cálculos básicos de inteligência de negócios (Business Intelligence)
    media_preco = df['Preco_Varejo'].mean()
    logging.info(f"Análise rápida: Preço médio da concorrência: £{media_preco:.2f}")
    
    # Exporta diretamente para o formato oficial do Excel (.xlsx)
    df.to_excel(nome_arquivo.replace('.csv', '.xlsx'), index=False)
    logging.info(f"Relatório gerado com sucesso no formato Excel: {nome_arquivo.replace('.csv', '.xlsx')}")

if __name__ == "__main__":
    # URL de teste voltada para web scraping legal
    URL_MERCADO = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
    
    logging.info("--- INICIANDO MOTOR DE SCRAPING ---")
    inicio_tempo = time.time()
    
    dados_brutos = extrair_dados_produtos(URL_MERCADO)
    gerar_relatorio(dados_brutos, "concorrencia_ciencia.xlsx")
    
    tempo_total = time.time() - inicio_tempo
    logging.info(f"--- OPERAÇÃO CONCLUÍDA EM {tempo_total:.2f} SEGUNDOS ---")