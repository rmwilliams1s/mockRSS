from django.test import TestCase
from django.urls import reverse


class FeedViewTests(TestCase):

    def test_no_feed(self):
        response = self.client.get(reverse("feed"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['feed'], None)

    def test_user_submit(self):
        response = self.client.get(reverse("feed") + "?url=http://feeds.nytimes.com/nyt/rss/HomePage")

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['feed'], None)
