from django.test import TestCase

from .models import Area
from userapp.models import Applicant
from mixer.backend.django import mixer



class TestViews(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.area_queryset = mixer.cycle(10).blend(Area)
        self.are_test = Area(name = 'Екатеринбург',ind_hh=3,ind_zarp=3,ind_super=33)

    def  test_index(self):
        res = self.client.get(reverse('hh:index'))
        self.assertEqual(res.status_code, 200)

    def  test_area(self):
        res = self.client.get(reverse('hh:area_list'))
        self.assertEqual(res.status_code, 200)
    def  test_area_create(self):
        area = Area(name = 'Екатеринбург',ind_hh=3,ind_zarp=3,ind_super=33)
        self.assertEqual(self.are_test, area)

    def  test_area_cr(self):
        res = self.client.post(reverse('hh:area_create'),{'name' :'Екатеринбург'})
        self.assertEqual(res.status_code, 200)

        Applicant.objects.create_user(username='test_user',email='1@mail.ru',password='t123232')
        self.client.login(username='test_user',password='t123232')

        res = self.client.post(reverse('hh:area_create'),{'name' :'Екатеринбург'})
        ar = Area.objects.get(name = 'Екатеринбург')
        self.assertEqual(self.are_test,ar)
