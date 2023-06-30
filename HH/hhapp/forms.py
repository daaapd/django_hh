from django import forms
from .models import Area, Schedule

class ReqForm(forms.Form):
    vacancy = forms.CharField(label='Строка поиска ')
    where = forms.ChoiceField(label='Где искать ', choices=[('all', "Везде"),
                                                            ('company', 'В названии компании'),
                                                            ('name', 'В названии вакансии')])
    pages = forms.IntegerField(label='Количество анализируемых страниц ', initial=3)

class UserReqForm(forms.Form):
    vacancy = forms.CharField(label='Строка поиска ')
    where = forms.ChoiceField(label='Где искать ', choices=[('all', "Везде"),
                                                            ('company', 'В названии компании'),
                                                            ('name', 'В названии вакансии')])
    pages = forms.IntegerField(label='Количество анализируемых страниц ', initial=3)

class UserReqForm(UserReqForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all(),
                                           widget=forms.CheckboxSelectMultiple(
                                               attrs={'class':'forms-check-inline'}
                                           ),label='Регион')
    schedules = forms.ModelMultipleChoiceField(queryset=Schedule.objects.all(),
                                           widget=forms.CheckboxSelectMultiple(
                                               attrs={'class':'forms-check-inline'}
                                           ),label='Занятость')

    vacancy = forms.CharField(label='Строка поиска ')
    where = forms.ChoiceField(label='Где искать ', choices=[('all', "Везде"),
                                                            ('company', 'В названии компании'),
                                                            ('name', 'В названии вакансии')])
    pages = forms.IntegerField(label='Количество анализируемых страниц ', initial=3)