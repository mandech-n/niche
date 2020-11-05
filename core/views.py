from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from core.models import User, Student, Item, Item_Detail_View, Comment
from .forms import StudentSignUpForm,TeacherSignUpForm,DonorSignUpForm,\
    PartnerSignUpForm,PublicSignUpForm, SignUpForm,CommentForm
from django.utils.decorators import method_decorator
from .decorators import student_required
from django.views.generic import ListView, DetailView, View
from django.db.models import Count, Q


def search(request):
    queryset = Item.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
    }
    return render(request, 'search_results.html', context)


def get_category_count():
    queryset = Item.objects \
        .values('category') \
        .annotate(Count('category'))

    return queryset

class IndexView(ListView):
    model = Item
    template_name = "index.html"
    category_count = get_category_count()

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    form = CommentForm(request.POST or None)
    Item_Detail_View.objects.get_or_create(user=request.user, item= item)

    if request.method == "POST":
        if form.is_valid:
            form.instance.user = user
            form.instance.item = item
            form.save()
            return redirect(reverse("item-detail", kwargs={
                'id': item.pk
            }))
    context = {'item': item,
               'form' : form
               }
    return render(request, 'item-detail.html',context)

def item_detail_create(request):
    title = 'Create'
    form = ItemForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.instace.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id

            }))

    context = {
        'title': title,
        'form': form
    }
    return render(request, "item_detail_create.html", context)


def item_detail_update(request, id):
    context = {
        'title': title,
        'form': form
    }
    return render(request, "post_create.html", context)

def item_detail_delete(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect(reverse("blog-detail"))

def contact_us(request):
    return render(request, 'contact-us.html',{})

def user_type(request):
    return render(request, 'user-type.html',{})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You account has been create you are now able to log in as {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'account/signup/sign_up_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('my-account.html')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'account/signup/sign_up_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(request, f'You account has been create you are now able to log in as {username}!')
        return redirect('my-account.html')

class DonorSignUpView(CreateView):
    model = User
    form_class = DonorSignUpForm
    template_name = 'account/signup/sign_up_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'donor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(request, f'You account has been create you are now able to log in as {username}!')
        return redirect('my-account.html')

class PublicSignUpView(CreateView):
    model = User
    form_class = PublicSignUpForm
    template_name = 'account/signup/sign_up_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'public'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('my-account.html')

class PartnerSignUpView(CreateView):
    model = User
    form_class = PartnerSignUpForm
    template_name = 'account/signup/sign_up_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'partner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(request, f'You account has been create you are now able to log in as {username}!')
        return redirect('my-account.html')

@login_required
def profile(request):
    return render(request, 'my-account.html')

