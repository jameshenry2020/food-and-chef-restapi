from rest_framework.test import APITestCase
from authentications.models import User
from rest_framework.authtoken.models import Token


class TestSetUp(APITestCase):

    def setUp(self):
        self.signup_url='/api/auth/users/'
        self.auth_url='/api/auth/users/me/'
       

        self.user_data={
            'email':'testuser22@gmail.com',
            'username':'testnewUser2',
            'first_name':'peter',
            'last_name':'solomon',
            'password':'test4321',
            're_password':'test4321'
        }

        self.user=User.objects.create_user(email='anotheruser@gmail.com',username='testuser4',first_name='sammy', last_name='rita',password=self.user_data['password'])
        self.token=Token.objects.create(user=self.user)
        self.api_authorization()

    def api_authorization(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
        return super().setUp()

    def tearDown(self):

        return super().tearDown()