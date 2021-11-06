# Django
from django import forms


#models
from posts.models import Post

class PostForm(forms.ModelForm):
	#post model form
	class Meta:
		#form setting
		model = Post
		fields = ('user', 'profile', 'title', 'photo')
