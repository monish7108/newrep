from django.db import models

class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    author_name = models.CharField(max_length=25)
    author_email_id = models.EmailField()
    date_of_birth = models.DateField()
    blog = models.URLField()
    total_books_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.author_name

    class Meta:
        ordering = ('author_id',)



class Book(models.Model):

    BOOK_RATINGS = (
        ('1', 'DIRT'),
        ('2', 'MILD'),
        ('3', 'MODERATE'),
        ('4', 'HIGH'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    published_year = models.IntegerField()
    ratings = models.CharField(max_length=1, choices=BOOK_RATINGS)
    no_of_copies_sold_till_date = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        new_author = Author.objects.get(author_name=self.author)
        total = new_author.total_books_sold
        total= total+self.no_of_copies_sold_till_date
        new_author.total_books_sold=total
        new_author.save()
        super(Book, self).save(*args, **kwargs)

    class Meta:
        ordering = ('ratings',)