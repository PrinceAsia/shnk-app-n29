from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = 'abstract_model'


class SHNKSystemsModel(AbstractBaseModel):
    code = models.CharField(max_length=2, unique=True)
    system_name_uz = models.CharField(max_length=255, unique=True)
    system_name_ru = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.system_name_uz}"

    class Meta:
        db_table = 'shnk_systems'
        verbose_name_plural = 'SHNK systems'


class SHNKGroupsModel(AbstractBaseModel):
    group_code = models.CharField(max_length=15)
    group_name_uz = models.CharField(max_length=255)
    group_name_ru = models.CharField(max_length=255)
    group_system = models.ForeignKey(SHNKSystemsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group_code} - {self.group_name_uz}"

    class Meta:
        db_table = 'shnk_groups'
        verbose_name_plural = 'SHNK groups'


class SHNKTypesModel(AbstractBaseModel):
    type_name_uz = models.CharField(max_length=10, unique=True)
    type_name_ru = models.CharField(max_length=10, unique=True, null=True)
    type_description_uz = models.CharField(max_length=255, null=True)
    type_description_ru = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.type_name_uz} - {self.type_description_uz}"

    class Meta:
        db_table = 'shnk_types'
        verbose_name_plural = 'SHNK types'


class SHNKDocumentsModel(AbstractBaseModel):
    shnk_name_uz = models.CharField(max_length=255, unique=True)
    shnk_name_ru = models.CharField(max_length=255, unique=True, null=True)
    shnk_code = models.CharField(max_length=10)
    shnk_type = models.ForeignKey(SHNKTypesModel, on_delete=models.CASCADE)
    shnk_file_uz = models.FileField(upload_to='shnk', null=True, blank=True)
    shnk_file_ru = models.FileField(upload_to='shnk', null=True, blank=True)
    shnk_group = models.ForeignKey(SHNKGroupsModel, on_delete=models.CASCADE)
    shnk_rating = models.JSONField(default=list)

    def __str__(self):
        return f"{self.shnk_name_uz} - {self.shnk_name_ru}"

    def average_rating(self):
        if len(self.shnk_rating) == 0:
            return 0
        summa = sum([i[1] for i in self.shnk_rating])
        return summa // len(self.shnk_rating)

    class Meta:
        db_table = 'shnk_documents'
        verbose_name_plural = 'SHNK documents'


class SHNKDocPartsModel(AbstractBaseModel):
    part_title_uz = models.CharField(max_length=255, unique=True)
    part_title_ru = models.CharField(max_length=255, unique=True, null=True)
    part_number = models.IntegerField()
    part_text_uz = RichTextField(null=True)
    part_text_ru = RichTextField(null=True)
    part_document = models.ForeignKey(SHNKDocumentsModel, on_delete=models.CASCADE)
    has_plan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.part_title_uz} - {self.part_title_ru}"

    class Meta:
        db_table = 'shnk_doc_parts'
        verbose_name_plural = 'SHNK doc_parts'


class SHNKDocPlansModel(AbstractBaseModel):
    plan_title_uz = models.CharField(max_length=255, unique=True)
    plan_title_ru = models.CharField(max_length=255, unique=True, null=True)
    plan_number = models.IntegerField()
    plan_text_uz = RichTextField(null=True)
    plan_text_ru = RichTextField(null=True)
    plan_part = models.ForeignKey(SHNKDocPartsModel, on_delete=models.CASCADE)
    plan_document = models.ForeignKey(SHNKDocumentsModel, on_delete=models.CASCADE)
    has_subplan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.plan_title_uz} - {self.plan_title_ru}"

    class Meta:
        db_table = 'shnk_doc_plans'
        verbose_name_plural = 'SHNK Document PLans'


class SHNKSubPlansModel(AbstractBaseModel):
    sub_plan_title_uz = models.CharField(max_length=255, unique=True)
    sub_plan_title_ru = models.CharField(max_length=255, unique=True, null=True)
    sub_plan_number = models.IntegerField()
    sub_plan_text_uz = RichTextField()
    sub_plan_text_ru = RichTextField(null=True)
    sub_plan_plan = models.ForeignKey(SHNKDocPlansModel, on_delete=models.CASCADE)
    sub_plan_document = models.ForeignKey(SHNKDocumentsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sub_plan_title_uz} - {self.sub_plan_title_ru}"

    class Meta:
        db_table = 'shnk_sub_plans'
        verbose_name_plural = 'SHNK Sub PLans'
