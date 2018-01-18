# _*_ coding: utf-8 _*_
__author__ = 'LennonChin'
__date__ = '2017/12/2 12:56'

from rest_framework import serializers

from article.models import ArticleInfo, ArticleDetail
from material.serializers import SingleLevelCategorySerializer, TagSerializer, LicenseSerializer
from BlogBackendProject.private import PRIVATE_QINIU_POST_GET_OBJECT_BASE_URL

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        fields = ('formatted_content',)


class ArticleDetailInfoSerializer(serializers.ModelSerializer):
    category = SingleLevelCategorySerializer()
    tags = TagSerializer(many=True)
    license = LicenseSerializer()
    detail = ArticleDetailSerializer()
    browse_auth = serializers.CharField(required=False, max_length=100, write_only=True)

    class Meta:
        model = ArticleInfo
        exclude = ('browse_password', )


class ArticleBaseInfoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    front_image = serializers.SerializerMethodField()

    def get_front_image(self, obj):
        return "{0}{1}".format(PRIVATE_QINIU_POST_GET_OBJECT_BASE_URL, obj.front_image)

    class Meta:
        model = ArticleInfo
        fields = (
            'id', 'title', 'desc', 'author', 'tags', 'click_num', 'like_num', 'comment_num', 'post_type',
            'front_image', 'is_recommend', 'is_hot', 'is_banner', 'browse_password_encrypt',
            'front_image_type', 'add_time')
