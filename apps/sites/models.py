from django.db import models
from django.db import connection
from django.db.models import Sum


class SummaryManager(models.Manager):

    def get_sum(self):
        return self.select_related(
            'site').values(
            'site', 'site__name').annotate(
            Sum('a_value'),
            Sum('b_value'))

    def get_average(self):

        result_list = []
        with connection.cursor() as cursor:
            cursor.execute("""
                    SELECT site.id, site.name,
                    AVG(site_data.a_value) as a_value__avg,
                    AVG(site_data.b_value) as b_value__avg
                    FROM site_data INNER JOIN site
                    WHERE site_data.site_id = site.id
                    GROUP BY site_data.site_id
                    ORDER BY site.id
                """)

            for row in cursor.fetchall():
                result_list.append({
                    'site': row[0],
                    'site__name': row[1],
                    'a_value__avg': row[2],
                    'b_value__avg': row[3]
                })
        return result_list


class SiteModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'Site: %s' % self.name

    class Meta:
        db_table = 'site'


class SiteDataModel(models.Model):
    site = models.ForeignKey(
        SiteModel, on_delete=models.CASCADE, related_name='site_data')
    a_value = models.DecimalField(max_digits=10, decimal_places=2)
    b_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(null=True, blank=True)
    objects = models.Manager()
    summary = SummaryManager()

    def __str__(self):
        return '%s (%s, %s)' % (self.site, self.a_value, self.b_value)

    class Meta:
        db_table = 'site_data'
