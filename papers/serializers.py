from rest_framework import serializers
from papers.models import Author, Record
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class AuthorCreateSerializer(serializers.Serializer):
    """serializer to create multiple authors from a comma seperated list of names"""

    authors = serializers.CharField(source="name")

    def create(self, validated_data):
        author_names = validated_data["name"].split(",")
        authors = []
        for author_name in author_names:
            author, _new = Author.objects.get_or_create(
                name=author_name.strip().upper()
            )
            authors.append(author)
        return authors


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    """serializer to display a single author"""

    class Meta:
        model = Author
        fields = ["name", "url"]


class RecordCreateSerializer(serializers.ModelSerializer):
    authors = AuthorCreateSerializer()

    class Meta:
        model = Record
        fields = ["title", "authors"]

    def create(self, validated_data):
        author_names = validated_data.pop("authors")
        authors = AuthorCreateSerializer().create(author_names)
        record = Record.objects.create(**validated_data)
        record.authors.set(authors)
        return record


class RecordListSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    # tags = TagListSerializerField()
    authors = AuthorListSerializer(many=True)

    class Meta:
        model = Record
        fields = ["title", "authors", "url"]
