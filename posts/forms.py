from django import forms

from posts.models import Post, Tag


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
    rate = forms.IntegerField()
    category = forms.CharField()
    language = forms.CharField()
    field = forms.CharField()

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        title = cleaned_data.get('title')
        if title == "python":
            raise forms.ValidationError("Please enter your post title.")
        return cleaned_data


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'language', 'field', 'image')
        widgets = {
            'title': forms.TextInput
            (attrs={
                'class': 'form-control',
                'placeholder': 'Enter your post title',
                'row': 3,
                'cols': 30,
            }),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'field': forms.Select(attrs={'class': 'form-control'}),

        }

class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search',
                'class': 'form-control',
            }))
    tag = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    orderings = (
        ('title', 'category'),
        ('-title', 'category in reverse order'),
        ('rate', 'rate'),
        ('-rate', 'rate in reverse order'),
        ('created_at', 'created_at'),
        ('-created_at', 'created_at in reverse order')
    )
    orderings = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'placeholder': 'Ordering', 'class': 'form-control'})
    )
