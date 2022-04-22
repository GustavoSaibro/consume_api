from .serializers import CandidatoSerializer
from .models import Candidato
import requests


def get_candidatos(url='http://localhost:8081/candidatos'):
    request = requests.get(url)    
    request_status = request.status_code
    id = None

    if request_status == 200:
        data = request.json()
        data = data['candidato'][0] 
        serialzier = CandidatoSerializer(data=data)
        # print(serialzier)

        if serialzier.is_valid():       
            serialzier.save()
            id = serialzier.data.get('id')
        #     # print(id)
        #     candidato = Candidato.objects.get(pk=id)       

    return id
                