from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum


#ignore doesnt work on database end
def validate_min_length(text):
    print("hello")
    if len(text) < 255:
        raise ValidationError(
            _("your post cannot be that short"),
            params={"value": text}
        )

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating =  models.IntegerField(default=0)


    def update_rating(self):

        # rating of the posts of the author
        author_post_rating = self.post_set.aggregate(postRating=Sum('rating'))  #try with just post

        p_rating = 0

        p_rating += author_post_rating.get('postRating')

        # rating of the comments of the author
        author_comment_rating = self.user.comment_set.aggregate(commentRating=Sum('rating')) #dont think user is needed here
        c_rating = 0
        c_rating += author_comment_rating.get('commentRating')

        #rating of the comments to the articles of the author
        author_posts = self.post_set.all()

        p_c_rating = 0

        for p in author_posts:
            comments = p.comment_set.all()
            for c in comments:
                p_c_rating += c.rating

        self.rating = p_rating * 3 + c_rating + p_c_rating
        self.save()



class Category(models.Model):
    POLITICS = "POL"
    SPORTS = "SPR"
    TECH = "TCH"
    LIFESTYLE = "LFS"
    BUSINESS = "BUS"
    ENTERTAINMENT = "ENT"
    UNKNOWN = "UNK"

    GENRES = [
        (POLITICS, "Politics"),
        (SPORTS, "Sports"),
        (TECH, "Technology"),
        (LIFESTYLE, "Lifestyle"),
        (BUSINESS, "Business"),
        (ENTERTAINMENT, "Entertainment"),
        (UNKNOWN, "Unknown")
    ]

    name = models.CharField(max_length=3, choices = GENRES, unique=True)



class Post(models.Model):

    BLOG = "Blog"
    NEWS = "News"

    TYPES = [
        (BLOG, "Blogpost"),
        (NEWS, "Newsarticle")
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE) #try: related_name="post"
    type = models.CharField(max_length=4, choices=TYPES)
    time_post = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')  #assuming a post can have more than one category
    title = models.CharField(max_length=255)
    text = models.TextField(validators=[validate_min_length])
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1   #assuming that a post can have a negative rating
        self.save()

    def preview(self):
        return self.text[:124] + " ..."



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete =models.CASCADE)




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_comment = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1   #assuming that a post can have a negative rating
        self.save()
