# encoding: utf-8

from gerencianet import Gerencianet

import secret


credentials = {
    'client_id': secret.CLIENT_ID_HOMOLOG,
    'client_secret': secret.CLIENT_SECRET_HOMOLOG,
    'sandbox': True,
    'certificate': secret.CERT_HOMOLOG
}

gn = Gerencianet(credentials)

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '12345678909',
        'nome': 'Francisco da Silva'
    },
    'valor': {
        'original': '123.45'
    },
    'chave': '71cdf9ba-c695-4e3c-b010-abb521a3f1be',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

import ipdb; ipdb.set_trace()
response =  gn.pix_create_immediate_charge(body=body)
print(response)