from django.test import TestCase
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.

class TestView(TestCase):
    def test_create_post(self):
        # 로그인 한 사람만 글을 작성할 수 있도록!


        response = self.client.get('/notice/create_post/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual('Create Post - Notice', soup.title.text)
        main_area = soup.find('div', id='main-area')
        self.assertIn('Create New Post', main_area.text)

        self.client.post(
            '/notice/create_post/',
            {
                'title' : 'Post Form 만들기',
                'content': "Post Form 페이지를 만듭시다",
            }


        )
        self.assertEqual(Post.objects.count(), 4)
        last_post = Post.objects.last()
        self.assertEqual(last_post.title, "Post Form 만들기")
        self.assertEqual(last_post.author.username,'trump')

