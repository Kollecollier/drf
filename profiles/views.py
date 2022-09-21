from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(APIView):

    def get(self,request):
        profile = Profile.objects.all()
        return Response(ProfileList)
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)