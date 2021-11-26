#comando para instalar REQUESTS, no cmd digital : pip install requests e depois importar pra uso
import  requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code) #código de sucesso
    print(response.json()) #traz informação do http
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

if __name__ == '__main__':
    retorna_dados_cep('01001000')

