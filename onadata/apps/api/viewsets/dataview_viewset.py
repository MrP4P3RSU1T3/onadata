from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from onadata.apps.logger.models.data_view import DataView
from onadata.apps.api.permissions import DataViewViewsetPermissions

from onadata.libs.serializers.dataview_serializer import DataViewSerializer
from onadata.libs.serializers.data_serializer import JsonDataSerializer
from onadata.libs.utils.export_tools import str_to_bool


class DataViewViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing DataViews.
    """
    queryset = DataView.objects.select_related()
    serializer_class = DataViewSerializer
    permission_classes = [DataViewViewsetPermissions]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'data':
            serializer_class = JsonDataSerializer
        else:
            serializer_class = self.serializer_class

        return serializer_class

    @action(methods=['GET'])
    def data(self, request, format='json', **kwargs):
        """ Retrieve the data from the xform using this dataview """
        start = request.GET.get("start")
        limit = request.GET.get("limit")
        count = request.GET.get("count")

        self.object = self.get_object()
        data = DataView.query_data(self.object, start, limit,
                                   str_to_bool(count))
        if 'error' in data:
            raise ParseError(data.get('error'))

        serializer = self.get_serializer(data, many=True)

        return Response(serializer.data)