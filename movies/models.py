from django.db import models
from users.models import User


class Rating(models.TextChoices):
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"
    OTHER = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(
        max_length=20, choices=Rating.choices, default=Rating.OTHER
    )
    synopsis = models.TextField(null=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    orders = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="ordered_movies",
    )

    def __repr__(self) -> str:
        return f"Movie [{self.id}] - {self.title}"


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_orders",
    )
    user_creator = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_order",
    )
    buyed_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __repr__(self) -> str:
        return f"MovieOrder [{self.id}] - {self.price}"
