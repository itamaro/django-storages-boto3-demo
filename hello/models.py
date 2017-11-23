from django.db import models


class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return 'Greeting: %s' % (self.when)
