from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Making A Test Api View"""
    def get(self, request, format=None):
        """Return A APIView Features!"""
        api_view = [
        'Its like a tradinational Django View',
        'It Provides more control over the application logic.',
        'It uses Http methods as get,post,patch,put,delete ',
        'It is mapped manaully to URls.'
        ]

        return Response({'message' : 'Hello!', 'api_view' : api_view})
