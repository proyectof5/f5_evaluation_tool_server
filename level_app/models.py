from django.db import models

class Level(models.Model):
    level = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'level'

    def __str__(self):
        return f"{self.name}"