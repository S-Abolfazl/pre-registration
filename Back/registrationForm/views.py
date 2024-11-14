from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import RegistrationForm
from .serializers import RegistrationFormSerializer


class RegistrationFormListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, form_id=None):
        if form_id:
            form = RegistrationForm.objects.get(form_id=form_id)
            serializer = RegistrationFormSerializer(form)
        else:
            forms = RegistrationForm.objects.all()
            serializer = RegistrationFormSerializer(forms, many=True)

        return Response(
            data={
                'msg': 'ok',
                'data': serializer.data[0]
            },
            status=status.HTTP_200_OK
        )


class RegistrationFormCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_id = request.user.id

        data = request.data.copy()
        data['student_id'] = user_id

        serializer = RegistrationFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    'msg': 'ok',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                'msg': 'error',
                'data': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class RegistrationFormUpdateView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, form_id):
        form = get_object_or_404(RegistrationForm, form_id=form_id)
        serializer = RegistrationFormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    'msg': 'ok',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'msg': 'error',
                'data': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class RegistrationFormDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, form_id):
        form = get_object_or_404(RegistrationForm, form_id=form_id)
        form.delete()
        return Response(
            data={
                'msg': 'ok',
                'data': f'Registration form {form_id} deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )
