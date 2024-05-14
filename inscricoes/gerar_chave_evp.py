from gerencianet import Gerencianet

import secret

credentials = {
    'client_id': secret.CLIENT_ID_HOMOLOG,
    'client_secret': secret.CLIENT_SECRET_HOMOLOG,
    'sandbox': True,
    'certificate': secret.CERT_HOMOLOG
}

gn = Gerencianet(credentials)

response = gn.pix_create_evp()
print(response)
