from django.test import TestCase
from django.contrib.auth import get_user_model


class NewUserManagerTest(TestCase):
    def test_create(self):
        # test user creation
        User = get_user_model
        user = User.objects.create(
            email = 'uuiui334@gmail.com',
            password = 'shghw3435'
        )
        
        # assert that the email is correct
        self.assertEqual(
            user.email, 
            'uuiui334@gmail.com'
        )
        # assert that user is active
        self.assertTrue(user.is_active)
        # assert that user is bnot a superuser or staff
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        
        # raise type error is no data is passed
        with self.assertRaises(TypeError):
            User.objects.create()

        # raise type error is email is empty
        with self.assertRaises(TypeError):
            User.objects.create(email = '')
            
        # raise value error if email is wrong
        with self.assertRaises(ValueError):
            User.objects.create(email = '', password = 'shghw3435')
        
    
    def test_create_superuser(self):
        # test user creation
        User = get_user_model
        admin = User.objects.create(
            email = 'admin34@gmail.com',
            password = 'sitegod22'
        )
        
        # assert that the email is correct
        self.assertEqual(
            admin.email, 
            'admin34@gmail.com'
        )
        # assert that user is active, a superuser and staff
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
        
        # # raise type error is no data is passed
        # with self.assertRaises(TypeError):
        #     User.objects.create()

        # # raise type error is email is empty
        # with self.assertRaises(TypeError):
        #     User.objects.create(email = '')
            
        # # raise value error if email is wrong
        # with self.assertRaises(ValueError):
        #     User.objects.create(email = '', password = 'sitegod22')
        
        
        
        from django.test import TestCase
from django.contrib.auth import get_user_model


# class NewUserManagerTest(TestCase):
#     def test_create(self):
#         # test user creation
#         User = get_user_model
#         user = User.objects.create(
#             email = 'uuiui334@gmail.com',
#             password = 'shghw3435'
#         )

#         # assert that the email is correct
#         self.assertEqual(
#             user.email, 
#             'uuiui334@gmail.com'
#         )
#         # assert that user is active
#         self.assertTrue(user.is_active)
#         # assert that user is bnot a superuser or staff
#         self.assertFalse(user.is_superuser)
#         self.assertFalse(user.is_staff)

#         self._extracted_from_test_create_superuser_21(User, 'shghw3435')
        
    
#     def test_create_superuser(self):
#         # test user creation
#         User = get_user_model
#         admin = User.objects.create(
#             email = 'admin34@gmail.com',
#             password = 'sitegod22'
#         )

#         # assert that the email is correct
#         self.assertEqual(
#             admin.email, 
#             'admin34@gmail.com'
#         )
#         # assert that user is active, a superuser and staff
#         self.assertTrue(admin.is_active)
#         self.assertTrue(admin.is_superuser)
#         self.assertTrue(admin.is_staff)

#         self._extracted_from_test_create_superuser_21(User, 'sitegod22')

#     # TODO Rename this here and in `test_create` and `test_create_superuser`
#     def _extracted_from_test_create_superuser_21(self, User, password):
#         with self.assertRaises(TypeError):
#             User.objects.create()
#         with self.assertRaises(TypeError):
#             User.objects.create(email='')
#         with self.assertRaises(ValueError):
#             User.objects.create(email='', password=password)
        