from django_tenants.test.cases import TenantTestCase
# Create your tests here.
from loot.models import Loot


class LootTests(TenantTestCase):

    @classmethod
    def setUpTestData(cls):
        cls.some_loot = Loot.objects.create(name="Torches", quantity=2, value_gold=0.2)

    def test_loot(self):
        self.assertEqual(self.some_loot.value_per_unit, 0.1)
