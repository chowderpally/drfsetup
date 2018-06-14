from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import StringSerializer


class StringView(APIView):
    def post(self, request):
        """
        The method that handles the POST request from the endpoint api/
        and returns the arguments that are passed as the url parameters
        along with the errors if any
        :param request:
        :return: Response with data & the errors if any
        """
        # Serializer that holds the data that is coming from the URL parameters
        # request.data is the dictionary that carries the URL parameters passed
        serializer = StringSerializer(data=request.data)

        # Checking whether the Serializer is valid ones or not
        if serializer.is_valid():
            return Response(data=request.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
