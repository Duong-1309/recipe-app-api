import logging

from django.db.models import Q
# from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@swagger_auto_schema(

)
class ListDemos(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = None
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_summary='Tên apis',
        operation_description='Mô tả apis',
        manual_parameters=[
            openapi.Parameter(description='Các param')
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT, properties={
                'aaa': 'aa'
            }, description='Các data trong body request'
        ),
        responses={
            HTTP_200_OK: openapi.Response(
                description='Mô tả trạng thái response',
                schema=openapi.Schema(
                    description='các data response',
                    type=openapi.TYPE_OBJECT, properties={
                        'aaa': 'aa'
                    }
                )
            )
        }
    )
    def get(self, request, format=None):
        """
        Return a list of all demos.
        """
        demos = [{'name': 'Demo one'}, {'name': 'Demo second'}]
        names = [demo['name'] for demo in demos]
        return Response(names, HTTP_200_OK)
