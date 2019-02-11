import random
import string

from autofixture import generators, register, AutoFixture

from fairsharing.models import FairsharingRecord

from django_prototype.settings import DATACITE_PREFIX


def generate_doi(prefix, size=6):
    suffix = ''.join(random.choice(string.ascii_uppercase +
                                   string.ascii_lowercase + string.digits) for _ in range(size))
    return '%s/FAIRsharing.%s' % (prefix, suffix)


####################################
# The actual records themselves... #
####################################
class FairsharingRecordAutoFixture(AutoFixture):
    field_values = {
        'name': generators.StringGenerator(max_length=10, min_length=8),
        'abbreviation': generators.StringGenerator(max_length=3, min_length=2),
        'homepage': generators.URLGenerator(),
        'description': generators.LoremGenerator(),
        'doi': generators.StaticGenerator(generate_doi(DATACITE_PREFIX))
    }


register(FairsharingRecord, FairsharingRecordAutoFixture)
