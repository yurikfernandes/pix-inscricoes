from rest_framework import serializers

from pagamentos.models import Pagamento


class PagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagamento
        exclude = ['chave', 'status', 'txid', 'pix_code']

    def get_photo_url(self, obj):
        import ipdb; ipdb.set_trace()
        request = self.context.get('request')
        photo_url = self.qrcode_image.figerprint.photo_url
        return request.build_absolute_uri(photo_url)