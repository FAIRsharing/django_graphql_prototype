from django.test import TestCase
from django.db.utils import DataError

from graphene.test import Client

from autofixture import AutoFixture, generators

from fairsharing.models import FairsharingRecord

#from django_prototype.schema import schema


class RecordTests(TestCase):

    def setUp(self):
        fixture = AutoFixture(FairsharingRecord)
        fixture.create(5)

    def test_record(self):
        record = FairsharingRecord.objects.first()

        # Is it a FairsharingRecord with the correct fields?
        self.assertTrue(isinstance(record, FairsharingRecord))
        self.assertEqual(record.__unicode__(), record.name)

        # Does it fail to save if the abbreviation is too long?
        record.abbreviation = generators.StringGenerator(max_length=130, min_length=129)
        try:
            record.save()
        except DataError:
            pass


class ApiTests(TestCase):

    def setUp(self):
        fixture = AutoFixture(FairsharingRecord)
        fixture.create(5)


    #def test_query(self):
    #    client = Client(schema)
    #    executed = client.execute(
    #        '''
    #        query {
    #          allFairsharingRecords {
    #            name
    #            id
    #          }
    #        }
    #        '''
    #        )
    #    print(executed)
    #    self.assertIsNotNone(executed)






