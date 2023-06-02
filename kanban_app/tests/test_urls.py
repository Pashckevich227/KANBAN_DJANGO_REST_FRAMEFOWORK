import json
from .test_setup import TestSetUp
from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from kanban_app.models import Board
from kanban_app.views import (BoardAllViewSet,
                    BoardDetailViewSet,
                    CategoryAllViewSet,
                    CategoryDetailViewSet,
                    )


class TestUrls(TestSetUp):

    def test_check_correct_all_boards_url(self):
        response = self.client.get(self.board_all_url)
        return self.assertEqual(response.status_code, 200)

    def test_check_correct_detail_board_url(self):
        response = self.client.get(self.board_detail_correct_url)
        return self.assertEqual(response.status_code, 200)

    def test_check_not_correct_detail_board_url(self):
        response = self.client.get(self.board_detail_not_correct_url)
        return self.assertEqual(response.status_code, 404)

    def test_check_correct_all_category_url(self):
        response = self.client.get(self.category_all_correct_url)
        return self.assertEqual(response.status_code, 200)

    def test_check_correct_detail_category_url(self):
        response = self.client.get(self.category_detail_correct_url)
        return self.assertEqual(response.status_code, 200)

    def test_check_not_correct_detail_category_url(self):
        response = self.client.get(self.category_detail_not_correct_url)
        return self.assertEqual(response.status_code, 404)


class TestCreate(TestSetUp, APITestCase):

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'color', 'board']))

