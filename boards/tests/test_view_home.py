from django.test import TestCase
from django.urls import reverse,resolve
from .views import home,board_topics
from .models import Board,User,Topic

# Create your tests here.
class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code,200)

	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func,home)

	def test_home_view_status_code(self):
		self.assertEquals(self.response.status_code, 200)
	def test_home_view_contains_link_to_topics_page(self):
        	board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        	self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))




