from django.forms import ModelForm
from models import Solucao, SolucaoIssue, ProjetoKnowLeds
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class SolucaoForm(ModelForm):
    class Meta:
        model = Solucao
        widgets = {
            'tarefa' : forms.HiddenInput()
        }
        fields = ['tarefa' , 'descricao']


class SolucaoIssueForm(ModelForm):
    class Meta:
        model = SolucaoIssue
        widgets = {
            'issue' : forms.HiddenInput()
        }
        fields = ['issue' , 'descricao']


class ProjetoKnowLedsForm(ModelForm):
    
    nome = forms.CharField(widget=forms.TextInput(attrs={ 'required' : 'True', 'max_length' : '30', 'placeholder' : 'Nome do Projeto', 'class' : 'form-control'}), label=_("Nome Projeto"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs={'required' : 'True', 'max_length' : '30', 'placeholder' : 'Email do Projeto', 'class' : 'form-control'}))

    
    class Meta:
        model = ProjetoKnowLeds
        fields = ['nome','email']

class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs={ 'required' : 'True', 'max_length' : '30', 'placeholder' : 'Usuario', 'class' : 'form-control'}), label=_(""), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs={'required' : 'True', 'max_length' : '30', 'placeholder' : 'Email', 'class' : 'form-control'}), label=_(""))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required' : 'True', 'max_length' : '30', 'placeholder' : 'Senha', 'render_value':'False', 'class' : 'form-control'}), label=_(""))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required' : 'True', 'max_length' : '30', 'placeholder' : 'Senha (novamente)', 'render_value':'False', 'class' : 'form-control'}), label=_(""))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data




class IntegranteForm(ModelForm):
    
   class Meta:
       model = User
       fields = ['email']