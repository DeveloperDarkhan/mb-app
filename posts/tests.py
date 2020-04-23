from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.

# class TestHomePageStatus(SimpleTestCase):

#     def test_home_page_status_code(self):

#         request =self.client.get('/')
#         self.assertEqual(request.status_code, 200)

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text = 'Test a db')

    def test_text_content(self):

        post = Post.objects.get(id=1)
        # print(dir(post))
        # for i in enumerate(dir(post), 1):
        #     print(i)
        expected_objects_name = f'{post.text}'
        self.assertEqual(expected_objects_name, 'Test a db')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text = 'This is another example')

    def test_view_url_exists_at_proper_location(self):
        request = self.client.get('/')
        print('\n' + f'{request}')
        self.assertEqual(request.status_code, 200)


    def test_view_url_by_name(self):
        request = self.client.get(reverse('home'))
        
        print('\n' + f'{request}')
        self.assertEqual(request.status_code, 200)

    def test_view_uses_correct_template(self):

        request = self.client.get(reverse('home'))
        # for i in dir(request):
        #     print(i)
        # print(request.template_name[0])
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'home.html')