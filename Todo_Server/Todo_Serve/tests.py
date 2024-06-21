
from django.test import TestCase
from .models import Task
from .views import TaskView
from rest_framework.test import APIRequestFactory

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='Test Task', completed=False)

    def test_title_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.title}'
        self.assertEquals(expected_object_name, 'Test Task')

class TaskViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='Test Task', completed=False)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/tasks/')
        self.assertEqual(resp.status_code, 200)
