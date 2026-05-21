# 🕸️ Motor de Extração de Dados e Monitoramento de Preços

Este projeto é um script de automação desenvolvido em Python para realizar Web Scraping. Ele coleta dados públicos de produtos (nome, preço e disponibilidade) e gera um relatório estruturado automaticamente.

## 🚀 O Problema Resolvido
Copiar e colar preços de concorrentes manualmente leva horas e está sujeito a erros humanos. Este script acessa o e-commerce alvo, faz a raspagem dos dados em segundos e entrega uma planilha limpa e pronta para análise de inteligência de negócios (BI).

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Requests:** Para requisições HTTP e comunicação com o servidor.
* **BeautifulSoup4:** Para o parsing e extração dos elementos HTML.
* **Pandas / Openpyxl:** Para estruturação dos dados e exportação direta para Excel (`.xlsx`).

## ⚙️ Como Executar
1. Clone o repositório.
2. Instale as dependências: `pip install requests beautifulsoup4 pandas openpyxl`
3. Execute o script: `python scraper_concorrencia.py`
4. O arquivo `concorrencia_ciencia.xlsx` será gerado no mesmo diretório.

## 📊 Demonstração do Sistema

**Console de Processamento (Logs em Tempo Real):**
<img width="1277" height="942" alt="print terminal projeto 1" src="https://github.com/user-attachments/assets/84717d96-664f-44f8-a4ac-1df5f43e4b4f" />


**Relatório Final Gerado (Excel):**
<img width="1341" height="367" alt="tabela excel projeto 1" src="https://github.com/user-attachments/assets/d8091492-ac28-46b8-8116-7a1ad905e768" />
