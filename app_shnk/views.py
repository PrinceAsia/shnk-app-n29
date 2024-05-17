from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import SHNKGroupsFilter, SHNKDocFilter, SHNKDocPartsFilter, SHNKDocPlansFilter, SHNKSubplanFilter
from .models import (
    SHNKSystemsModel,
    SHNKGroupsModel,
    SHNKTypesModel,
    SHNKDocumentsModel,
    SHNKDocPartsModel, SHNKDocPlansModel,
    SHNKSubPlansModel,
)
from .permissions import IsSuperUserORReadOnly
from .serializers import (
    SHNKSystemsSerializer, SHNKSystemsGETSerializer,
    SHNKGroupsSerializer, SHNKGroupsGETSerializer,
    SHNKTypesSerializer,
    SHNKDocGETSerializer, SHNKDocSerializer, SHNKRatingSerializer,
    SHNKDocPartSerializer, SHNKDocPartsGETSerializer,
    SHNKDocPlansGETSerializer, SHNKDocPlanSerializer,
    SHNKSubPlansSerializer, SHNKSubPlansGETSerializer,
)


# Create your views here.
class SHNKSystemsViewSet(ModelViewSet):
    queryset = SHNKSystemsModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKSystemsGETSerializer
        return SHNKSystemsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


class SHNKGroupsViewSet(ModelViewSet):
    queryset = SHNKGroupsModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SHNKGroupsFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKGroupsGETSerializer
        return SHNKGroupsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


class SHNKTypesViewSet(ModelViewSet):
    queryset = SHNKTypesModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]
    serializer_class = SHNKTypesSerializer


class SHNKDocumentsViewSet(ModelViewSet):
    queryset = SHNKDocumentsModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SHNKDocFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKDocGETSerializer
        return SHNKDocSerializer


class SHNKDocPartViewSet(ModelViewSet):
    queryset = SHNKDocPartsModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SHNKDocPartsFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKDocPartsGETSerializer
        return SHNKDocPartSerializer


class SHNKDocPlanViewSet(ModelViewSet):
    queryset = SHNKDocPlansModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SHNKDocPlansFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKDocPlansGETSerializer
        return SHNKDocPlanSerializer


class SHNKSubPlanViewSet(ModelViewSet):
    queryset = SHNKSubPlansModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SHNKSubplanFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKSubPlansModel
        return SHNKSubPlansSerializer


@api_view(['GET'])
def shnk_full_search(request):
    keyword = request.GET.get('keyword', None)
    if keyword:
        shnk_docs = list(SHNKDocumentsModel.objects.filter(shnk_name_uz__icontains=keyword).values_list('id'))
        shnk_parts = list(SHNKDocPartsModel.objects.filter(part_text_uz__icontains=keyword).values_list('part_document'))
        shnk_plans = list(SHNKDocPlansModel.objects.filter(plan_title_uz__icontains=keyword).values_list('plan_document'))
        shnk_subplans = list(SHNKSubPlansModel.objects.filter(
            sub_plan_title_uz__icontains=keyword).values_list('sub_plan_document'))

        res = shnk_docs + shnk_parts + shnk_plans + shnk_subplans

        result = [0] * len(res)

        for i in range(len(res)):
            result[i] = res[i][0]

        shnk_list = SHNKDocumentsModel.objects.filter(id__in=set(result))
        serializer = SHNKDocSerializer(shnk_list, many=True)

        return Response({'result': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response(data={'message': 'Insert keyword please'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def shnk_rating(request, shnk_id):
    if request.user.is_authenticated:
        serializer = SHNKRatingSerializer(data=request.data)
        if serializer.is_valid():
            rating = serializer.data['rating']
            stars = SHNKDocumentsModel.objects.get(id=shnk_id)
            for i in range(1, 6):
                if [request.user.id, i] in stars.shnk_rating:
                    stars.shnk_rating.remove([request.user.id, i])
                    stars.shnk_rating.append([request.user.id, rating])
                    stars.save()
                    break
            else:
                stars.shnk_rating.append([request.user.id, rating])
                stars.save()
            return Response(
                data={'Your stars': rating, 'Average rating': stars.average_rating()},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    return Response(
        data={'message': 'You are not logged in, login please'},
        status=status.HTTP_401_UNAUTHORIZED
    )
