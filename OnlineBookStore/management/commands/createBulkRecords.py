from django.core.management import BaseCommand
from ...models import *

class Command(BaseCommand):
    help = "My test command"

    def add_arguments(self, parser):
        parser.add_argument('cmdarg',type=int,nargs='*' ,default=[2,2])

    def handle(self, *args, **options):
        no_of_authors=options.get('cmdarg', None)[0]
        no_of_books = options.get('cmdarg', None)[1]

        if Author.objects.all().exists():
            last_author_id = Author.objects.all().order_by('-author_id').values("author_id")[:1][0]['author_id']
        else:
            last_author_id = 1

        self.creating_records(no_of_authors,no_of_books,last_author_id)

#################################################################################################################

    def creating_records(self,no_of_authors ,no_of_books,last_author_id):
        authors_queries=[]
        books_queries = []

        author_id_starts_from = self.getting_new_author_id(last_author_id)

        for i in range(no_of_authors):
            new_author=Author(author_id=author_id_starts_from,author_name="Author"+str(i+1),author_email_id='a@b.com',date_of_birth='1992-12-12',blog='www.google.com',total_books_sold=0)
            for j in range(no_of_books):
                new_book = Book(author=new_author,title="Book"+str(j),published_year=1999,ratings='4',no_of_copies_sold_till_date=300)
                books_queries.append(new_book)
            author_id_starts_from = self.getting_new_author_id(author_id_starts_from)

            authors_queries.append(new_author)

        self.commit(authors_queries, books_queries)



    def commit(self,authors_queries, books_queries):
        Author.objects.bulk_create(authors_queries)
        Book.objects.bulk_create(books_queries)

    #################################################################################################################

    def getting_new_author_id(self,last_id):
        return last_id+1