from decimal import Decimal

from django.test import SimpleTestCase
from django_tenants.test.cases import FastTenantTestCase

from loot.models import Loot
from users.models import TenantUser
from utils.assets import get_css
from utils.colors import gamma_correction, get_percieved_lightness, is_bright_color
from utils.markdown import md_to_html, autolink
from utils.money import format_money
from utils.urls import name2url


class BaseTest(FastTenantTestCase):
    @classmethod
    def setup_tenant(cls, tenant):
        # Creates the tenant user needed to set up tenant.owner_id

        tenant_user = TenantUser.objects.get_or_create(email="test@example.com")
        tenant.name = "public"
        tenant.email = "test2@example.com"

        # For django-tenant-users

        tenant.owner_id = 1
        tenant.tenants = [1]
        return tenant

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.setUpTestData()


class ColorsTests(SimpleTestCase):
    def test_gamma_correction(self):
        r, g, b = 10, 120, 255
        self.assertEqual(gamma_correction(r), 0.003035269835488375)
        self.assertEqual(gamma_correction(g), 0.18782077230067787)
        self.assertEqual(gamma_correction(b), 1)

    def test_percieved_lightness(self):
        self.assertLess(get_percieved_lightness((10, 120, 255)), 53)
        self.assertGreater(get_percieved_lightness((10, 120, 255)), 52)

    def test_is_bright_color(self):
        self.assertFalse(is_bright_color("#123321"))
        self.assertTrue(is_bright_color("#58b783"))
        self.assertTrue(is_bright_color("#af6bce"))


class MarkdownTests(SimpleTestCase):
    def test_basic_markdown(self):
        self.assertHTMLEqual(
            md_to_html("**test** *it*", replacements={})[0],
            "<p><strong>test</strong> <em>it</em></p>"
        )

    def test_nb_md(self):
        self.assertHTMLEqual(
            md_to_html("This\nis\nTest", replacements={})[0],
            "<p>This<br>is<br>Test</p>"
        )

    def test_bleach(self):
        self.assertEqual(
            md_to_html(
                "<script>console.log()</script> <a onclick='console.log()'>Hi</button>", replacements={})[0],
            "&lt;script&gt;console.log()&lt;/script&gt;\n<p><a>Hi&lt;/button&gt;</a></p>"
        )


class AutoLinkTests(BaseTest):
    @classmethod
    def setUpTestData(cls):
        cls.some_loot = Loot.objects.create(name="Torches", quantity=2, value_gold=0.2)

    def test_name2url(self):
        self.assertEqual(
            name2url(),
            {'Torches': ('/loot/1/edit', self.some_loot)}
        )

    def test_autolink(self):
        self.assertEqual(
            autolink("these Torches"),
            ("these [Torches](/loot/1/edit)", {"loo1"})
        )

    def test_basic_markdown(self):
        self.assertHTMLEqual(
            md_to_html("most Torches we found")[0],
            '<p>most<a href="/loot/1/edit">Torches</a>we found</p>'
        )


class MoneyTests(SimpleTestCase):
    def test_money_conversion(self):
        self.assertEqual(format_money(Decimal("0.1")), "1 SP")
        self.assertEqual(format_money(Decimal("0.001")), "")
        self.assertEqual(format_money(Decimal("0.01")), "1 CP")
        self.assertEqual(format_money(Decimal("1.1")), "1 GP 1 SP")
        self.assertEqual(format_money(Decimal("100")), "100 GP")
        self.assertEqual(format_money(Decimal("0")), "")


class ScssTests(SimpleTestCase):
    def test_scss(self):
        css, sourcemap = get_css(debug=True)
        self.assertIn("body", css)
        self.assertIn(".scss", sourcemap)
