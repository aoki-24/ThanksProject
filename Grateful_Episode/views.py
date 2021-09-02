from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic
from django.contrib.auth import get_user_model
from Grateful_Episode.models import Episode
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

User = get_user_model()

class home(generic.ListView):
    model = Episode
    template_name = 'Grateful_Episode/home.html'
    def get(self,request,*args, **kwargs):
        episode_list = Episode.objects.order_by('episode_id').reverse()
        paginator = Paginator(episode_list, 10) 
        p = request.GET.get('p') 
        episode_list = paginator.get_page(p) 
        if not episode_list:
            episode_count=0
        else:
            episode_count = episode_list[0].episode_id 
        return render(request,self.template_name,{
            'episode_list' : episode_list,
            'episode_count' : episode_count
        })
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            get_episode_id=request.POST['be_grateful_count']
            if Episode.objects.filter(episode_id = get_episode_id):
                episode_object = Episode.objects.get(episode_id = get_episode_id)
                episode_object.be_grateful_count+=1
                episode_object.save()
                user=self.request.user
                User.objects.filter(thanks_id__exact=episode_object.contributor)
                if user.is_authenticated:
                    user.grateful_to_count+=1
                    user.save()
                if User.objects.filter(thanks_id__exact=episode_object.contributor):
                    be_user=User.objects.get(thanks_id=episode_object.contributor)
                    be_user.be_grateful_count+=1
                    be_user.save()
                return HttpResponse(episode_object.be_grateful_count)
            else:
                return HttpResponse()
        post_contributor = request.POST['contributor']
        post_episode = request.POST['episode']
        post_id=Episode.objects.all().count()
        if not (User.objects.filter(thanks_id__exact=post_contributor)):
            User.objects.create(thanks_id=post_contributor)
        Episode.objects.create(episode_id=post_id,contributor=get_object_or_404(User,thanks_id=post_contributor),episode=post_episode,contribute_date=timezone.now().date(),be_grateful_count=0,public=True)
        
        episode_list = Episode.objects.order_by('episode_id').reverse()
        paginator = Paginator(episode_list, 10) 
        p = request.GET.get('p') 
        episode_list = paginator.get_page(p) 
        
        if not episode_list:
            episode_count=0
        else:
            episode_count = episode_list[0].episode_id 
        return render(request,self.template_name,{
            'episode_list' : episode_list,
            'episode_count' : episode_count
        })




    