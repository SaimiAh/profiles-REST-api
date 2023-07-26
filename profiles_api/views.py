from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status

class HelloApiView(APIView):
    """Making A Test Api View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Return A APIView Features!"""
        api_view = [
        'Its like a tradinational Django View',
        'It Provides more control over the application logic.',
        'It uses Http methods as get,post,patch,put,delete ',
        'It is mapped manaully to URls.'
        ]

        return Response({'message' : 'Hello!', 'api_view' : api_view})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})
