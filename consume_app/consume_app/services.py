from .serializers import CandidatoSerializer
import requests


def get_candidatos(url='http://localhost:8081/candidatos'):
    request = requests.get(url)    
    request_status = request.status_code

    if request_status == 200:
        data = request.json()
        data = data['candidato'][0] 
        serialzier = CandidatoSerializer(data=data)

        if serialzier.is_valid():       
            serialzier.save()
        return True

    return False
                