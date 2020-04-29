from django.db import models


class commentaire(models.Model):
    def __str__(self):
        return self.commentaire_text
    commentaire_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
# Create your models here.
