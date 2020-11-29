from django.db import models
# importing User and Recipe models here


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(null=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'Author: {self.author} Content: {self.body}'