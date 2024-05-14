import base64
from django.db import models

from pagamentos.efi_connector import EfiConnector

class Pagamento(models.Model):
    devedor_cpf = models.CharField(max_length=11, blank=True, null=True)
    devedor_nome = models.CharField(max_length=60)
    valor = models.CharField(max_length=10)
    chave = models.CharField(max_length=77, null=True, blank=True)
    descricao = models.CharField(max_length=140)
    expiracao = models.IntegerField()
    status = models.CharField(max_length=20)
    txid = models.CharField(max_length=50)
    pix_code = models.CharField(max_length=50)
    qrcode_image = models.ImageField(null=True, blank=True, upload_to="images/")
    

    def save(self, *args, **kwargs):

        # key = EfiConnector.get_pix_key()
        key = '71cdf9ba-c695-4e3c-b010-abb521a3f1be'
        payload = {
            "cpf" : self.devedor_cpf,
            "nome" : self.devedor_nome,
            "valor" : self.valor,
            "chave" : key,
            "descricao" : self.descricao,
            "expiracao": self.expiracao
        }
        response = EfiConnector.create_pix_immediate_charge(payload)
        response_data = response.json()
        
        self.txid = response_data.get('txid')
        self.status = response_data.get('status')
        self.loc = response_data.get('loc').get('id')
        self.key = key
        qrcode, imagem_qr_code, link_visualizar = EfiConnector.generate_qrcode(self.loc)
        self.pix_code = qrcode

        image = 'media/' + f"{self.txid}.png"
        image_path = f"{self.txid}.png"
        if imagem_qr_code:
            with open(image, 'wb') as fh:
                fh.write(base64.b64decode(imagem_qr_code.replace('data:image/png;base64,', '')))
        
        self.qrcode_image = image_path

        super(Pagamento, self).save(*args, **kwargs)
