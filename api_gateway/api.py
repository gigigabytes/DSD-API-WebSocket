from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def cep_detail(request, cep):
    # Chamar API de CEP dos Correios aqui
    data = {'cep': cep, 'logradouro': 'Rua Exemplo'}
    return Response({
        'data': data,
        'links': {
            'self': reverse('cep-detail', args=[cep], request=request),
            'update': reverse('cep-update', args=[cep], request=request),
        }
    })
