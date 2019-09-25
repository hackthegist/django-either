from django.db import models

# Create your models here.
class Question(models.Model):
    """A question, which will be selected as either A and B"""

    title = models.CharField(max_length=100) 
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)
    image_a = models.ImageField()
    image_b = models.ImageField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['-pk']

    def __str__(self):
        """Unicode representation of Question."""
        return f'{title}'


class Answer(models.Model):
    """A user's pick and a comment"""

    pick = models.IntegerField()
    comment = models.TextField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Answer."""

        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['-pk']

    def __str__(self):
        """Unicode representation of Answer."""
        return f'{pick}, {comment}'
