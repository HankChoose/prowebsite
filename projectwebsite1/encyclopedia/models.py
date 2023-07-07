from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    

'''
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

$python manage.py makemigrations
$python manage.py migrate

from .models import Book

# 创建新的Book实例
new_book = Book(title='Sample Book', author='John Doe', publication_date='2023-01-01')
new_book.save()

# 查询所有的Book实例
books = Book.objects.all()

# 查询特定条件的Book实例
filtered_books = Book.objects.filter(author='John Doe')

# 更新Book实例
book = Book.objects.get(pk=1)
book.title = 'Updated Title'
book.save()

# 删除Book实例
book = Book.objects.get(pk=1)
book.delete()



'''