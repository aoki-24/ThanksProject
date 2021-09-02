from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin
from Grateful_Episode.models import Episode
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
User = get_user_model()

class mypage(generic.ListView):
    template_name = 'Grateful_User/mypage.html'
    def get(self,request):
        episodes=Episode.objects.filter(contributor__exact=request.user.thanks_id)
        episodes_count=episodes.count()
        paginator = Paginator(episodes, 10) 
        p = request.GET.get('p') 
        episodes = paginator.get_page(p) 
        return render(request,self.template_name,{
            'my_episode':episodes
            ,'episode_count':episodes_count
        })

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserDetail(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'Grateful_Episode/user_detail.html'