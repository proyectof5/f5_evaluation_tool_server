from django.db import models

class CompetenceOverview(models.Model):
    competence = models.ForeignKey('competence_app.Competence', on_delete=models.CASCADE, related_name='overviews')
    weight = models.IntegerField(null=False)
    technology = models.ForeignKey('technology_app.Technology', on_delete=models.CASCADE, related_name='overviews')
    level = models.ForeignKey('level_app.Level', on_delete=models.CASCADE, related_name='overviews')

    class Meta:
        db_table = 'competence_overview'

    def __str__(self):
        return f"{self.competence}"