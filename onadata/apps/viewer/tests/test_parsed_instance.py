from onadata.apps.viewer.models.parsed_instance import get_where_clause

from onadata.apps.main.tests.test_base import TestBase


class TestParsedInstance(TestBase):
    def test_get_where_clause_with_json_query(self):
        query = '{"name": "bla"}'
        where, where_params = get_where_clause(query)
        self.assertEqual(where, [u"json->>%s = %s"])
        self.assertEqual(where_params, ["name", "bla"])

    def test_get_where_clause_with_string_query(self):
        query = 'bla'
        where, where_params = get_where_clause(query)
        self.assertEqual(where, [u"json::text ~* cast(%s as text)"])
        self.assertEqual(where_params, ["bla"])

    def test_get_where_clause_with_integer(self):
        query = '11'
        where, where_params = get_where_clause(query)
        self.assertEqual(where, [u"json::text ~* cast(%s as text)"])
        self.assertEqual(where_params, [11])
