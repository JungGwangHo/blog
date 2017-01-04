from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#summernote
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields
class PostForm(forms.ModelForm):
    #summernote
    fields = summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
    class Meta:
        model = Post
        fields = ('title','fields','content','textonly',)
        widgets= {
             'foo' : SummernoteWidget(),
             'bar' : SummernoteInplaceWidget(),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username", "email", )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        # 각 input 태그에 placeholder를 추가함.
        self.fields['username'].widget.attrs['placeholder'] = "ID"
        self.fields['username'].widget.attrs['id'] = "username"
        self.fields['password1'].widget.attrs['placeholder'] = "비밀번호"
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['placeholder'] = "비밀번호 확인"
        self.fields['email'].widget.attrs['placeholder'] = "exampl@abc.com"
