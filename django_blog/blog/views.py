from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PostForm

# Home View
def home(request):
    return render(request, 'blog/base.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# User Profile (Requires Login)
@login_required
def profile(request):
    return render(request, 'blog/profile.html')

# User Logout
def custom_logout(request):
    logout(request)
    return redirect('login')

# Profile Update (Requires Login)
@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'blog/profile_update.html', context)


### Blog Post CRUD Views ###

# List View - Displays all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'  
    context_object_name = 'posts'
    ordering = ['-published_date']  # Newest posts first

# Detail View - Displays a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  

# Create View - Allows authenticated users to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update View - Allows authors to edit their own posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # Reuse same template as create

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete View - Allows authors to delete their own posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  
    success_url = '/'  # Redirect to home after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
