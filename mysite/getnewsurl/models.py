from django.db import models

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_content = models.TextField()
    news_filename = models.CharField(max_length=350, default=None)
    news_time_publish = models.DateTimeField('news date published')
    news_language = models.CharField(max_length=2)
    news_domain = models.CharField(max_length=50)
    news_date_download = models.DateTimeField('news date download')
    news_url = models.CharField(max_length=300)
    news_deletion = models.BooleanField()

    def __str__(self):
        return self.news_title

class News_Authors(models.Model):
    author_fkey = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=30)

class News_Images(models.Model):
    image_fkey = models.ForeignKey(News, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=300)
    image_description = models.CharField(max_length=200)
    image_stance = models.CharField(max_length=20)

class News_Movies(models.Model):
    movie = models.ForeignKey(News, on_delete=models.CASCADE)
    movie_url = models.CharField(max_length=300)
    movie_description = models.CharField(max_length=200)
    movie_stance = models.CharField(max_length=20)

class News_Label(models.Model):
    news_fkey = models.OneToOneField(News, on_delete=models.CASCADE, primary_key = True)
    news_label = models.CharField(choices = (
        ('f', "Fake"),
        ('r', "Real"),
    ),max_length=1)

    def __str__(self):
        return self.news_label

class News_Stance(models.Model):
    news_fkey = models.OneToOneField(News, on_delete=models.CASCADE, primary_key = True)
    news_stance = models.CharField(choices= (
        ("Ag", "Agrees"),
        ("Da", "Disagrees"),
        ("D~", "Discusses"),
        ("Ur", "Unrelated")
    ),max_length=2)
    news_true_language = models.CharField(max_length=2)

    def __str__(self):
        return self.news_stance