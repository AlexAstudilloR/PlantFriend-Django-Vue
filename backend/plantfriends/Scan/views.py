import requests
import base64
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser

def obtener_nombre_comun(nombre_cientifico):
    # URL de la API de Wikipedia para obtener el resumen de la página correspondiente al nombre científico
    url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{nombre_cientifico.replace(' ', '_')}"

    # Hacer una solicitud GET a la API de Wikipedia
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Intentar obtener el nombre común desde las primeras palabras del extracto
        if 'extract' in data:
            extracto = data['extract']
            # Tomar la primera oración como nombre común potencial
            palabras_iniciales = extracto.split('.')[0]  # Primera oración del extracto
            return palabras_iniciales
        elif 'description' in data:
            return data['description']
    return "Nombre común no encontrado"



@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def ScanPlant(request):
    # Verificar si el archivo 'image' está en la solicitud
    if 'image' not in request.FILES:
        return Response({'error': 'No se proporcionó ninguna imagen.'}, status=status.HTTP_400_BAD_REQUEST)

    image = request.FILES['image']
    encoded_image = base64.b64encode(image.read()).decode('utf-8')

    # Configurar la carga útil para la API de Plant.id
    payload = {
        "images": [encoded_image],
        "include-related-images": False
    }
    headers = {
        "Content-Type": "application/json",
        "Api-Key": settings.PLANT_API_KEY
    }

    # Enviar la solicitud a la API de Plant.id
    response = requests.post("https://api.plant.id/v2/identify", json=payload, headers=headers)
    
    if response.status_code == 200:
        result = response.json()

        # Buscar la sugerencia con la mayor probabilidad
        mejor_sugerencia = None
        mayor_probabilidad = 0
        for suggestion in result['suggestions']:
            if suggestion['probability'] > mayor_probabilidad:
                mayor_probabilidad = suggestion['probability']
                mejor_sugerencia = suggestion

        # Si hay una sugerencia con alta probabilidad, obtener nombre común
        if mejor_sugerencia:
            nombre_cientifico = mejor_sugerencia['plant_details']['scientific_name']
            nombre_comun = obtener_nombre_comun(nombre_cientifico)  # Llamar a la función para obtener el nombre común
            probabilidad = mejor_sugerencia['probability']

            # Formatear la respuesta para devolver solo la información necesaria
            data = {
                "nombre_cientifico": nombre_cientifico,
                "nombre_comun": nombre_comun,
                "probabilidad": probabilidad
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No se encontró ninguna coincidencia con alta probabilidad."}, status=status.HTTP_200_OK)
    
    else:
        return Response({'error': 'Error al procesar la imagen en la API de Plant.id.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)