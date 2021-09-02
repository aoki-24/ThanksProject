from django.contrib import admin
from django.db.models import fields

# Register your models here.
"""
Customizations for the Django administration interface.
"""
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from Grateful_User.models import User
from Grateful_Episode.models import Episode

#管理者サイトに関連するもの
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('thanks_id',)

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('thanks_id' ,'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('thanks_id' ,'password1', 'password2','is_staff',),
        }),
    )
    
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ( 'thanks_id' ,'is_staff','is_superuser',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('thanks_id' , 'is_staff', 'is_superuser', 'is_active',)
    ordering = ('thanks_id',)

class EpisodeAdmin(admin.ModelAdmin):
    class Meta:
        model=Episode
    list_display = ('episode_id','contributor','episode','contribute_date','be_grateful_count')
    ordering = ('episode_id','contribute_date','be_grateful_count',)
    search_fields = ('episode_id','contribute_date',)  

admin.site.register(Episode,EpisodeAdmin)
admin.site.register(User, MyUserAdmin)



