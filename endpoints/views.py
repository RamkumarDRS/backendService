

from rest_framework import status
from endpoints.models import ServiceProvider
from rest_framework.decorators import api_view
from rest_framework.response import Response
from endpoints.serlializers import ServiceSerializer

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def EndpointsView(request):
    if request.method == "GET":
        try:
            endpoints_object = ServiceProvider.objects.filter(service_type=request.data.get('service_type'))
            endpoint_data = ServiceSerializer(endpoints_object, many=True)
            return Response({
                'status': True,
                'status code': status.HTTP_200_OK,
                'msg': 'Successfully retrieved data',
                'data': endpoint_data.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'status code': status.HTTP_400_BAD_REQUEST,
                'msg': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)



    if request.method == 'PUT':
        print("FROM 54 ")
        try:
            serve_obj = request.data.get('data')
            print("FROM 57 ",serve_obj)
            print(serve_obj)
            for data in serve_obj:
                print(">>>>>>>>>> ",type(data),data.get("service_Provider"))
                serve_data = ServiceProvider.objects.filter(pk=data['id'])[0]
                serve_data.service_type = data.get("service_type")
                serve_data.service_Provider = data.get("service_Provider")
                serve_data.key = data.get("key")
                serve_data.api1 = data.get("api1")
                serve_data.api2 = data.get("api2")
                serve_data.status = data.get("status")
                serve_data.save()
                print(">>>>>>>>>>!!!! ", data['id'],data.get("service_type"),data.get("service_Provider"),data.get("key"),data.get("api1"),data.get("api2"))



            return Response({
                'status': True,
                'status code': status.HTTP_200_OK,
                'msg': 'Service updated successfully',
            }, status=status.HTTP_200_OK)

        except ServiceProvider.DoesNotExist:
            return Response({
                'status': False,
                'status code': status.HTTP_400_BAD_REQUEST,
                'msg': 'Service provider not found'
            }, status=status.HTTP_400_BAD_REQUEST)










