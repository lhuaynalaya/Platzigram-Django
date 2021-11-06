# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
#form
from posts.forms import PostForm

#models
from posts.models import Post

# posts = [
#   {
#     'title': 'Mont Blanc',
#     'user': {
#         'name': 'Yasica Cortas',
#         'picture': 'https://picsum.photos/60/60/?image=1027'
#     },
#     'timestamp': datetime.now().strftime('%b %dth, %Y'),
#     'photo': 'https://picsum.photos/800/600?image=1036',
#   },
#   {
#     'title': 'Via Lactea',
#     'user': {
#         'name': 'Christian Van der Henst',
#         'picture': 'https://picsum.photos/60/60/?image=1005'
#     },
#     'timestamp': datetime.now().strftime('%b %dth, %Y'),
#     'photo': 'https://picsum.photos/800/800/?image=903',
#   },
#   {
#     'title': 'Nuevo auditorio',
#     'user': {
#         'name': 'Uriel (thespianartist)',
#         'picture': 'https://picsum.photos/60/60/?image=883'
#     },
#     'timestamp': datetime.now().strftime('%b %dth, %Y'),
#     'photo': 'https://picsum.photos/500/700/?image=1076',
#   }
# ]

@login_required

def list_posts(request):
	#render  => una funcion que toma un request

	# content = []
	# for post in posts:
	# 	content.append(""" 
	# 		<p><strong>{name}</strong><p>
	# 		<p><small>{user} - <i>{timestamp}</i></small><p>
	# 		<figure><img src="{picture}"/><figure>
	# 	""".format(**post))
	# return HttpResponse('<br>'.join(content))
  posts = Post.objects.all().order_by('-created')
  return render(request, 'posts/feed.html', { 'posts': posts})

@login_required
def create_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('feed')
  else:
    form = PostForm

  return render(
    request=request,
    template_name='posts/new.html',
    context={
      'profile': request.user.profile,
      'user': request.user,
      'form': form
    }
  )
