## Console commants

**1. Создать двух пользователей (с помощью метода User.objects.create_user('username'))**
```
User.objects.create_user("user1")
User.objects.create_user("user2")
```


**2. Создать два объекта модели Author, связанные с пользователями**
``` 
Author.objects.create(user=User.objects.get(pk=2))  #(pk=1 is the superuser)
Author.objects.create(user=User.objects.get(pk=3))
```


**3. Добавить 4 категории в модель Category**

4 times the command below with categories allowed from the choices-list
```
Category.objects.create(name=<category>)
```


**4. Добавить 2 статьи и 1 новость.**

3 times something similar to below:

```
Post.objects.create(author=author1, type="News",title="Exiled Russian oligarch Mikhail Khodorkovsky claims Vladimir Putin is 'afraid of starting a war with Ukraine'", text="Mr Khodorkovsky says he knows he is taking a risk every time he speaks out against the Russian leader but claims that the practice is rife and has to be stopped.Speaking to Sky News, the former head of oil giant Yukos, who was imprisoned for ten years by Mr Putin's government for tax evasion and theft in a controversial case, said it was really important to fight this. He explained: Putin's clique use money in order to illegally put pressure on the British political system. And this is happening - directly, indirectly, via legal firms, via lobbying businesses, via directly influencing politicians and so on and so forth.")
```


**5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий)**

saving the posts, then adding categories to them (e.g. "POL" (politics) for the post above)
can do that several times for the same post (this way a post can have more than one category)

```
post1.category.add(Category.objects.get(pk=1))
```
or
```
pol = Category.objects.get(pk=1)
pol.name.set(post1)
```


**6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий)**

4 times something like this:
```
Comment.objects.create(post=post1,user=User.objects.get(pk=1), text="Khodorkovsky is right as usual")
```


**7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов**

like or dislike the posts/comments
```
post1.like()
comment3.dislike() etc.
```


**8. Обновить рейтинги пользователей**
```
author1.update_rating()
author2.update_rating()
```


**9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта)**
```
best_author = Author.objects.all().order_by('-rating')[0]
best_author.user.username, best_author.rating
```


**10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье**
```
best_post = Post.objects.all().order_by('-rating')[0]
best_post.time_post.strftime('%Y-%m-%d')
best_post.author.user.username
best_post.title
best_post.preview()
```


**11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье**
```
comments_best_post = best_post.comment_set.all()

for c in comments_best_post:
    print(c.time_comment.strftime('%Y-%m-%d'))
    print(c.user)
    print(c.rating)
    print(c.text)
    print()

```
