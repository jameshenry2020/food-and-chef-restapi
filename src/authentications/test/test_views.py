from .test_setup import TestSetUp
from rest_framework import status
from django.urls import reverse
import json


class NewUserSignupTestCase(TestSetUp):
    def test_new_user_can_signup(self):
        response=self.client.post(self.signup_url, self.user_data, format='json')
        self.assertEqual(response.status_code, 201)


class GetAuthUserTestCase(TestSetUp):
    def test_get_authenticated_data(self):
        res=self.client.get(self.auth_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['email'], 'anotheruser@gmail.com')


    def test_authenticated_user_can_create_chef_book(self):
        data={
            'name':'mycookingstyle',
            'chef':self.user
        }
        response=self.client.post(reverse('chef-book'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_get_chef_list(self):
        self.client.force_authenticate(user=None, token=None)
        response=self.client.get(reverse('chef-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_profile_retrieve(self):
        res=self.client.get(reverse('user-profile', kwargs={'pk':1}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['user'], 'anotheruser@gmail.com')

    def test_user_can_update_his_profile(self):
        response=self.client.put(reverse('user-profile', kwargs={'pk':1}), {"bio":"testuser talk about himself", "phone":"09080886400", "country":"USA"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {"id":1, "bio":"testuser talk about himself", "image":None, "phone":"09080886400", "country":"USA", "user":"anotheruser@gmail.com"})



