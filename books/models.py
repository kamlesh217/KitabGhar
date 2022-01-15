from django.db import models

# Create your models here.

class book_store(models.Model):
    book_name=models.CharField(max_length=50,unique=True, primary_key=True)
    book_auth=models.CharField(max_length=50)
    book_page=models.IntegerField()
    book_image=models.ImageField(upload_to="pic")
    book_pdf=models.FileField(upload_to='pdfs/')
    book_publish=models.CharField(max_length=50)

#book_publish=models.DateField(("01/01/2000"), auto_now=False, auto_now_add=False)

