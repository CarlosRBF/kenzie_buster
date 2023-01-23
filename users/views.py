from django.shortcuts import get_list_or_404

from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer
from .models import User

from .permissions import MyCustomPermissionTokenValid


class LoginView(TokenObtainPairView):
    ...


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermissionTokenValid]

    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermissionTokenValid]

    def get(self, request: Request, user_id: int) -> Response:
        user = User.objects.get(pk=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)
