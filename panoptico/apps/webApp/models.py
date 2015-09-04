# coding=utf8

from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.utils import timezone
from django.conf import settings



''' panóptico user '''
class PanopticoUser(AbstractBaseUser):
    #id = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True, max_length=40);
    create_time = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    username = models.TextField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_admin  = models.BooleanField(default=False)
    is_staff  = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    class Meta:
        db_table = u'panoptico_user'
    
        

''' panóptico camera '''
class Camera(models.Model):
    creation_date = models.DateField()
    
    class Meta:
        db_table = u'panoptico_camera'

    
''' comentários nas cameras '''
class CameraComment(models.Model):
    camera = models.ForeignKey(Camera)
    submission_date = models.DateField()
    
    class Meta:
        db_table = u'panoptico_camera_comment'


''' post '''
class Post(models.Model): 
    title = models.CharField(max_length=200, verbose_name=_("title"))
    slug = models.SlugField()
    bodytext = models.TextField(verbose_name=_("message"))
    post_date = models.DateTimeField(
    auto_now_add=True, verbose_name=_("post date"))
    modified = models.DateTimeField(null=True, verbose_name=_("modified"))
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("posted by"))    
    allow_comments = models.BooleanField(default=True, verbose_name=_("allow comments"))
    comment_count = models.IntegerField(blank=True, default=0, verbose_name=_('comment count'))
    
    class Meta:
        db_table = u'panoptico_post'
        


''' comentários nos posts do blog '''
class PostComment(models.Model):
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=200, verbose_name=_("title"))
    slug = models.SlugField()
    bodytext = models.TextField(verbose_name=_("message"))
    post_date = models.DateTimeField(
    auto_now_add=True, verbose_name=_("post date"))
    modified = models.DateTimeField(null=True, verbose_name=_("modified"))
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("posted by"))
    allow_comments = models.BooleanField(default=True, verbose_name=_("allow comments"))
    comment_count = models.IntegerField(blank=True, default=0, verbose_name=_('comment count'))
    
    class Meta:
        db_table = u'panoptico_post_comment'
        
    
    
