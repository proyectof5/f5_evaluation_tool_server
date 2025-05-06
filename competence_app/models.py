from django.db import models

class Competence(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'competence'

    def __str__(self):
        return f"{self.name}"