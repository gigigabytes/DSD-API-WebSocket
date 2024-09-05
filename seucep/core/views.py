from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.shortcuts import render


@api_view(['GET'])
def cep_detail(request, cep):
    # Aqui você pode integrar com a API de CEP dos Correios
    data = {'cep': cep, 'logradouro': 'Rua Exemplo'}
    return Response({
        'data': data,
        'links': {
            'self': reverse('cep-detail', args=[cep], request=request),
            'update': reverse('cep-update', args=[cep], request=request),
        }
    })

def index(request):
    return render(request, 'index.html')
