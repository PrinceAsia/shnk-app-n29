import django_filters

from .models import SHNKGroupsModel, SHNKDocumentsModel, SHNKDocPartsModel, SHNKDocPlansModel, SHNKSubPlansModel


class SHNKGroupsFilter(django_filters.FilterSet):
    group_system = django_filters.CharFilter(lookup_expr='exact', required=True)

    class Meta:
        model = SHNKGroupsModel
        fields = ['group_system']


class SHNKDocFilter(django_filters.FilterSet):
    shnk_group = django_filters.CharFilter(lookup_expr='exact', required=True)

    class Meta:
        model = SHNKDocumentsModel
        fields = ['shnk_group']


class SHNKDocPartsFilter(django_filters.FilterSet):
    part_shnk = django_filters.CharFilter(lookup_expr='exact', required=True)

    class Meta:
        model = SHNKDocPartsModel
        fields = ['part_shnk']


class SHNKDocPlansFilter(django_filters.FilterSet):
    plan_part = django_filters.CharFilter(lookup_expr='exact', required=True)

    class Meta:
        model = SHNKDocPlansModel
        fields = ['plan_part']


class SHNKSubplanFilter(django_filters.FilterSet):
    sub_plan_part = django_filters.CharFilter(lookup_expr='exact', required=True)

    class Meta:
        model = SHNKSubPlansModel
        fields = ['sub_plan_part']
