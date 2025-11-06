import requests

def extrair_dados(pais, indicador):

    url = f"https://servicodados.ibge.gov.br/api/v1/paises/{pais}/indicadores/{indicador}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()