from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post, Author, User
from datetime import datetime
from django.shortcuts import render
from .filters import PostFilter
from .forms import PostForm
# Create your views here.
"""
def showresults(request):
    if request.method =="POST":
        fromdate = request.POST.get("from")
        todate = request.POST.get("to")
        searchresult = Post.objects.raw('select title from portal_post where date_post between "'+fromdate+'" and "'+todate+'"')
        return render(request, 'flatpages/posts.html', {"data": searchresult})
    else:

        displaydata = Post.objects.all()
        return render(request, 'flatpages/posts.html', {"data": displaydata})

"""
@method_decorator(login_required, name='dispatch')
class PostAdd(PermissionRequiredMixin, CreateView):
    """
    createviews save automatically and do not require saving like if it was listfew with post function
    """
    #model = Post
    template_name = 'flatpages/add.html'
    context_object_name = 'posts'

    form_class = PostForm
    success_url = '/news/'

    permission_required = ('portal.add_post',)

    """
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)
    """

@method_decorator(login_required, name='dispatch')
class Posts(ListView):
    model = Post
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    ordering = ['-time_post'] #TODO; do it by date
    paginate_by = 3# поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['authors'] = Author.objects.all()
        #context['test'] ="TEST"

        return context

    """

    dont need below because now we only display and search in separate site

    def get_queryset(self):
        queryset = super().get_queryset()
        return PostFilter(self.request.GET, queryset=queryset).qs
    """


@method_decorator(login_required, name='dispatch')
class PostSearch(ListView):
    model = Post
    template_name = 'flatpages/search.html'
    context_object_name = 'posts'
    ordering = ['-time_post'] #TODO; do it by date
    paginate_by = 3 # поставим постраничный вывод в один элемент
    #form_class = PostForm

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['authors'] = Author.objects.all()
        #context['form'] = PostForm()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return PostFilter(self.request.GET, queryset=queryset).qs


    """
    def post(self, request, *args, **kwargs):
        # берём значения для нового товара из POST-запроса отправленного на сервер
        title = request.POST['title']
        text = request.POST['text']
        author_id = request.POST['author']
        print(type(author_id))
        #category = request.POST['category']

        post = Post(title=title, text=text, author__user = author_id)#, category=category)  # создаём новый товар и сохраняем
        post.save()
        return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.
    """



"""
class PostList(ListView):
    model = Post
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'#
    queryset = Post.objects. ("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра

        return context

"""
@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):
    model = Post
    template_name = "flatpages/post.html"
    contect_object_name = 'post'
    queryset = Post.objects.all()

# дженерик для редактирования объекта
@method_decorator(login_required, name='dispatch')
class PostUpdate(PermissionRequiredMixin,UpdateView):
    template_name = 'flatpages/add.html'
    form_class = PostForm
    success_url = '/news/'

    permission_required = ('portal.change_post',)
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
@method_decorator(login_required, name='dispatch')
class PostDelete(PermissionRequiredMixin,DeleteView):
    template_name = 'flatpages/delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

    permission_required = ('portal.delete_post',)
