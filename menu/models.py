from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, null=True)
    named_url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name

    def get_named_url(self):
        from django.urls import reverse, NoReverseMatch
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        return self.url or '#'
