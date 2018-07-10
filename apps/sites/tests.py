from django.test import TestCase

from decimal import Decimal
from .models import SiteModel, SiteDataModel


class SiteTest(TestCase):

    def setUp(self):

        self.site = SiteModel.objects.create(id=1, name='XYZ Site')

        self.site_data = SiteDataModel.objects.create(
            site=self.site,
            a_value=Decimal(5.0),
            b_value=Decimal(5.0))

    def test_site_model(self):
        self.assertEqual(str(self.site), "Site: XYZ Site")
        self.assertEqual(self.site.name, "XYZ Site")

    def test_site_data_model(self):
        self.assertEqual(self.site_data.a_value, Decimal(5.0))
        self.assertEqual(self.site_data.b_value, Decimal(5.0))

    def test_site_list_page(self):
        response = self.client.get('/sites/')
        self.assertEqual(response.status_code, 200)

    def test_site_detail_page(self):
        response = self.client.get('/sites/%s/' % self.site.id)
        self.assertEqual(response.status_code, 200)

    def test_site_summary_sum_page(self):
        response = self.client.get('/summary/')
        self.assertEqual(response.status_code, 200)

    def test_site_summary_avg_page(self):
        response = self.client.get('/summary-average/')
        self.assertEqual(response.status_code, 200)
