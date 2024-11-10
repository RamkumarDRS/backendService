from rest_framework import status
from endpoints.models import ServiceProvider
from rest_framework.decorators import api_view
from rest_framework.response import Response

from endpoints.serlializers import ServiceSerializer


# @api_view(['GET', 'POST','DELETE','PUT'])
# def EndpointsView(request):
#         if request.method == "GET":
#              endpoints_object = ServiceProvider.objects.all()
#              endpoint_data = ServiceSerializer(endpoints_object, many=True)
#              return Response({'msg': 'Successfully retrieved data', 'data':endpoint_data.data}, status=status.HTTP_200_OK)
#
#         if request.method == 'PUT':
#             serve_obj = ServiceProvider.objects.get(serviceType=request.data.get('serviceType'))
#             serializer = ServiceSerializer(serve_obj, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg': 'service updated successfully', 'data': serializer.data},
#                                 status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from endpoints.models import ServiceProvider
from rest_framework.decorators import api_view
from rest_framework.response import Response
from endpoints.serlializers import ServiceSerializer

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def EndpointsView(request):
    if request.method == "GET":
        try:
            # Fetching all ServiceProvider objects
            endpoints_object = ServiceProvider.objects.all()
            # Serializing the data to convert to a list of JSON objects
            endpoint_data = ServiceSerializer(endpoints_object, many=True)
            return Response({
                'status': True,
                'status code': status.HTTP_200_OK,
                'msg': 'Successfully retrieved data',
                'data': endpoint_data.data  # this will be an array of objects
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'status code': status.HTTP_400_BAD_REQUEST,
                'msg': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        try:
            # Trying to get the ServiceProvider instance based on the serviceType field
            serve_obj = ServiceProvider.objects.get(serviceType=request.data.get('serviceType'))
            # Serializing the object with the new data from the request
            serializer = ServiceSerializer(serve_obj, data=request.data)
            if serializer.is_valid():
                # Save the updated data
                serializer.save()
                return Response({
                    'status': True,
                    'status code': status.HTTP_200_OK,
                    'msg': 'Service updated successfully',
                    'data': serializer.data  # updated data after saving
                }, status=status.HTTP_200_OK)
            return Response({
                'status': False,
                'status code': status.HTTP_400_BAD_REQUEST,
                'msg': 'Validation error',
                'errors': serializer.errors  # validation errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except ServiceProvider.DoesNotExist:
            return Response({
                'status': False,
                'status code': status.HTTP_400_BAD_REQUEST,
                'msg': 'Service provider not found'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': False,
                'status code': status.HTTP_400_BAD_REQUEST,
                'msg': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

