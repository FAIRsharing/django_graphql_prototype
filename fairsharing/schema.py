import graphene
import json

from graphene_django.types import DjangoObjectType

from fairsharing.models import FairsharingRecord


# A definition for Graphene of the FairsharingRecord already defined in models.py
class FairsharingRecordType(DjangoObjectType):
    class Meta:
        model = FairsharingRecord


# Presumably we'll need one of these classes for everything we would like to be able to create or modify
# with the API
class FairsharingRecordInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    abbreviation = graphene.String(required=True)
    doi = graphene.String(required=True)
    homepage = graphene.String(required=True)
    description = graphene.String(required=True)


# And one of these to actually do the modification
class CreateFairsharingRecord(graphene.Mutation):
    class Arguments:
        record_data = FairsharingRecordInput(required=True)

    ok = graphene.Boolean()
    record = graphene.Field(lambda: FairsharingRecord)

    @staticmethod
    def mutate(root, info, record_data=None):
        record = FairsharingRecord.objects.create(
            name=record_data.name,
            abbreviation=record_data.abbreviation,
            doi=record_data.doi,
            homepage=record_data.homepage,
            description=record_data.description
        )
        ok = True
        return CreateFairsharingRecord(record=record, ok=ok)


# All the queries are to be defined here, so presumably yet another long boilerplate list
class Query(object):
    all_fairsharing_records = graphene.List(FairsharingRecordType)
    fairsharing_record = graphene.Field(FairsharingRecordType,
                                        id=graphene.Int(),
                                        name=graphene.String())

    def resolve_all_fairsharing_records(self, info, **kwargs):
        return FairsharingRecord.objects.all()

    def resolve_fairsharing_record(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return FairsharingRecord.objects.get(pk=id)

        if name is not None:
            return FairsharingRecord.objects.get(name=name)

        return None


# All the mutations, i.e. creations and modifications, to go here.
class Mutation(object):
    create_fairsharing_record = CreateFairsharingRecord.Field()


