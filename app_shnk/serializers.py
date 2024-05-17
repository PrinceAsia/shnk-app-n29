from rest_framework.serializers import ModelSerializer, Serializer, IntegerField, SerializerMethodField

from app_shnk.models import (
    SHNKSystemsModel,
    SHNKGroupsModel,
    SHNKTypesModel, SHNKDocumentsModel,
    SHNKDocPartsModel, SHNKDocPlansModel,
    SHNKSubPlansModel,
)


class SHNKSystemsSerializer(ModelSerializer):
    class Meta:
        model = SHNKSystemsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class SHNKSystemsGETSerializer(ModelSerializer):
    system_name = SerializerMethodField(method_name='get_system_name', read_only=True)

    class Meta:
        model = SHNKSystemsModel
        fields = ('id', 'code', 'system_name')

    def get_system_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.system_name_ru
            return obj.system_name_uz
        except:
            return obj.system_name_uz


class SHNKGroupsSerializer(ModelSerializer):
    class Meta:
        model = SHNKGroupsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class SHNKGroupsGETSerializer(ModelSerializer):
    group_name = SerializerMethodField(method_name='get_group_name', read_only=True)

    class Meta:
        model = SHNKGroupsModel
        fields = ('id', 'group_code', 'group_name')

    def get_group_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.group_name_ru
            return obj.group_name_uz
        except:
            return obj.group_name_uz


class SHNKTypesSerializer(ModelSerializer):
    class Meta:
        model = SHNKTypesModel
        fields = '__all__'


class SHNKDocGETSerializer(ModelSerializer):
    shnk_name = SerializerMethodField(method_name='get_shnk_name', read_only=True)
    shnk_average_rating = SerializerMethodField(method_name='get_shnk_average_rating', read_only=True)

    class Meta:
        model = SHNKDocumentsModel
        fields = ('id', 'shnk_code', 'shnk_name', 'shnk_average_rating')

    def get_shnk_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.shnk_name_ru
            return obj.shnk_name_uz
        except:
            return obj.shnk_name_uz

    def get_shnk_average_rating(self, obj):
        return obj.average_rating()


class SHNKDocSerializer(ModelSerializer):
    class Meta:
        model = SHNKDocumentsModel
        fields = '__all__'


class SHNKDocPartsGETSerializer(ModelSerializer):
    part_name = SerializerMethodField(method_name='get_part_name', read_only=True)

    class Meta:
        model = SHNKDocPartsModel
        fields = '__all__'

    def get_part_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.part_title_ru
            return obj.part_title_uz
        except:
            return obj.part_title_uz


class SHNKDocPartSerializer(ModelSerializer):
    class Meta:
        model = SHNKDocPartsModel
        fields = '__all__'


class SHNKDocPlansGETSerializer(ModelSerializer):
    plan_name = SerializerMethodField(method_name='get_plan_name', read_only=True)

    class Meta:
        model = SHNKDocPlansModel
        fields = '__all__'

    def get_plan_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.plan_title_ru
            return obj.plan_title_uz
        except:
            return obj.plan_title_uz


class SHNKDocPlanSerializer(ModelSerializer):
    class Meta:
        model = SHNKDocPlansModel
        fields = '__all__'


class SHNKSubPlansGETSerializer(ModelSerializer):
    sub_plan_name = SerializerMethodField(method_name='get_sub_plan_name', read_only=True)

    class Meta:
        model = SHNKSubPlansModel
        fields = '__all__'

    def get_sub_plan_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.sub_plan_title_ru
            return obj.sub_plan_title_uz
        except:
            return obj.sub_plan_title_uz


class SHNKSubPlansSerializer(ModelSerializer):
    class Meta:
        model = SHNKSubPlansModel
        fields = '__all__'


class SHNKRatingSerializer(Serializer):
    rating = IntegerField(min_value=1, max_value=5)
