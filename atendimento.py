import re

atualizar = {
    'cartão de crédito' : 'Me forneça os dados do cartão',
    'informações de pagamento' : 'Por favor, me fornece o número do seu CPF',
    'forma de pagamento' : 'Por favor, me fornece o número do seu CPF',
}


acompanhar = {
    'atualizar' : 'Por favor, me infome o seu CPF',
  'status' : 'Consultando status do pedido',
  'rastrear' : 'Rastreando status do pedido',
  'saber' : 'Consultando pedido',
  'entrega' : 'Buscando informações de entregra',
}

def translater(text):
    rg_atualizar = re.compile(r'\b(?:cartão\s?de\s?crédito|forma\s?de\s?pagamento)\b', re.IGNORECASE) #regex
    rg_acompanhar = re.compile(r'\b(?:status|rastrear|saber|\s?entrega|atualizar)\b')
    match_atualizar = rg_atualizar.search(text) #Buscando pelo dicionário
    match_acompanhar = rg_acompanhar.search(text)
    resposta_auto = 'Não entendi o sua requisicao'

    if match_atualizar:
        return str(atualizar.get(match_atualizar.group(0))) # se for verdade, ele retorna em str o valor da chave
    
    elif match_acompanhar:
        return str(acompanhar.get(match_acompanhar.group(0)))


    return resposta_auto

def main():
    input_text = input(f'O que você deseja? \n') #input usuário
    resposta = translater(input_text) #função principal de busca e filtro
    print(resposta)

    if resposta == 'o que você deseja atualizar? Cartão de crétido ou informações de pagamento?':
        main() #recursiva, queria fazer em um for mas já está em cima da hora.
    

print('*Sistema funciona sem pontuação da lingua portuguesa') #(printa apenas no inicio do programa)
main()
