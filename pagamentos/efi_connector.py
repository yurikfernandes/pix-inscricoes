# encoding: utf-8

import base64
import json
from gerencianet import Gerencianet
import requests
from inscricoes import secret


credentials = {
    'client_id': secret.CLIENT_ID_HOMOLOG,
    'client_secret': secret.CLIENT_SECRET_HOMOLOG,
    'sandbox': True,
    'certificate': secret.CERT_HOMOLOG
}

class EfiConnector:
    gn = Gerencianet(credentials)
    base_url = 'https://api-pix-h.gerencianet.com.br/'
    # base_url = 'https://pix-h.api.efipay.com.br/'
    
    @classmethod
    def get_oauth_token(cls):

        path = cls.base_url+'oauth/token'
        
        auth = base64.b64encode((
                f"{credentials['client_id']}:{credentials['client_secret']}"
            ).encode()).decode()
        
        payload = json.dumps({
            "grant_type": "client_credentials"
        })

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {auth}'
        }

        response = requests.request(
            method='POST',
            url=path,
            data=payload,
            headers=headers,
            cert=credentials['certificate']
        )

        return response

    @classmethod
    def get_pix_key(cls):
        import ipdb; ipdb.set_trace()
        path = 'https://pix-h.api.efipay.com.br/v2/gn/evp'

        auth_token = json.loads(EfiConnector.get_oauth_token().text).get('access_token')

        headers = {
            'Authorization': f'Bearer {auth_token}'
        }

        response =  requests.request(
            method='POST',
            url=path,
            headers=headers,
            cert=credentials['certificate']
        )

        # response =  cls.gn.pix_create_evp()
        
        return response

    @classmethod
    def create_pix_immediate_charge(cls, payload):

        path = cls.base_url+'v2/cob'

        payload = json.dumps({
            'calendario': {
                'expiracao': payload.get('expiracao', 3600)
            },
            'devedor': {
                'cpf': payload.get('cpf'),
                'nome': payload.get('nome')
            },
            'valor': {
                'original': payload.get('valor')
            },
            'chave': payload.get('chave'),
            'solicitacaoPagador': payload.get('descricao')
        })

        auth_token = json.loads(EfiConnector.get_oauth_token().text).get('access_token')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        }

        # response =  cls.gn.pix_create_immediate_charge(body=body)
        response =  requests.request(
            method='post',
            url=path,
            data=payload,
            headers=headers,
            cert=credentials['certificate']
        )
        
        return response
    
    @classmethod
    def generate_qrcode(cls, id):

        path = cls.base_url+f'v2/loc/{id}/qrcode'

        auth_token = json.loads(EfiConnector.get_oauth_token().text).get('access_token')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        }

        response =  requests.request(
            method='get',
            url=path,
            headers=headers,
            cert=credentials['certificate']
        )
        response_data = response.json()

        return response_data.get('qrcode'), response_data.get('imagemQrcode'), response_data.get('linkVisualizacao')