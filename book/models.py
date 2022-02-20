from email.policy import default
from django.db import models

# Create your models here.

class book_store(models.Model):
    book_name=models.CharField(max_length=100, unique=True, primary_key=True)
    book_auth=models.CharField(max_length=100)
    book_page=models.IntegerField()
    book_publish=models.DateField(default='2000-01-01')
    book_publisher=models.CharField(max_length=100)
    book_image=models.ImageField(upload_to='book_image_file')
    book_pdf=models.FileField(upload_to='book_pdf_file')

    def __str__(self):
        return self.book_name
    
    def pdf(self):
        return self.book_pdf
    
    def image(self):
        return self.book_image