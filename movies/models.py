# movies/models.py

from django.db import models
from django.contrib.auth.models import User

# ... your existing Movie and Review models ...

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')

    def __str__(self):
        return str(self.id) + ' - ' + self.name
class Review(models.Model):

    id = models.AutoField(primary_key=True)

    comment = models.CharField(max_length=255)

    date = models.DateTimeField(auto_now_add=True)

    movie = models.ForeignKey(Movie,

        on_delete=models.CASCADE)

    user = models.ForeignKey(User,

        on_delete=models.CASCADE)

    def __str__(self):

        return str(self.id) + ' - ' + self.movie.name
    
class Reply(models.Model):
    # Link each reply to a specific review
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='replies')
    # Link each reply to the user who wrote it
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # The actual text of the reply
    comment = models.TextField()
    # Automatically records when the reply was created
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.user.username} on {self.review.id}'
