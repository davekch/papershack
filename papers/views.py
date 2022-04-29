from rest_framework import permissions, viewsets
from papers.serializers import (
    AuthorListSerializer,
    RecordCreateSerializer,
    RecordListSerializer,
)
from papers.models import Record, Author


class RecordViewSet(viewsets.ModelViewSet):
    """API endpoint for records"""

    queryset = Record.objects.all()
    serializer_class = RecordListSerializer
    action_serializers = {
        "list": RecordListSerializer,
        "create": RecordCreateSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        # use a different serializer for get and post requests
        return self.action_serializers.get(self.action, self.serializer_class)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = [permissions.IsAuthenticated]
