from rest_framework import status
from endpoints.models import ServiceProvider
from rest_framework.decorators import api_view
from rest_framework.response import Response

from endpoints.serlializers import ServiceSerializer


@api_view(['GET', 'POST','DELETE','PUT'])
def EndpointsView(request):
        if request.method == "GET":
             endpoints_object = ServiceProvider.objects.all()
             endpoint_data = ServiceSerializer(endpoints_object, many=True)
             return Response({'msg': 'Successfully retrieved data', 'data':endpoint_data.data}, status=status.HTTP_200_OK)

        if request.method == 'PUT':
            serve_obj = ServiceProvider.objects.get(serviceType=request.data.get('serviceType'))
            serializer = ServiceSerializer(serve_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'service updated successfully', 'data': serializer.data},
                                status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



