from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from kanban_app.models import Board, Category
from rest_framework.test import APIRequestFactory
from kanban_app.serializer import CategorySerializer


class TestSetUp(APITestCase):
    fake = Faker()
    Faker.seed(0)

    def setUp(self):
        self.factory = APIRequestFactory()

        # Board urls
        self.board_all_url = reverse('board_list')
        self.board_detail_correct_url = reverse('board_detail', args='1')
        self.board_detail_not_correct_url = reverse('board_detail', args='9')

        # Category urls
        self.category_all_correct_url = reverse('category_list', args='1')
        self.category_detail_correct_url = reverse('category_detail', args='1')
        self.category_detail_not_correct_url = reverse('category_detail', args='9')

        # setup data models
        self.board_data = Board.objects.create(
            id = 1,
            name = 'Testing Board',
            description = self.fake.sentence(nb_words=10)
        )

        self.category_data = Category.objects.create(
            id = 1,
            name = self.fake.name(),
            color = 'green',
            board = self.board_data
        )

        # Post method
        self.post_catagory_data = {
            'id': 12,
            'name': self.fake.name(),
            'color': 'blue',
            'board': self.board_data
        }

        self.category = Category.objects.create(**self.post_catagory_data)
        self.serializer = CategorySerializer(instance=self.category)

        return super().setUp()


    def tearDown(self):
        return super().tearDown()