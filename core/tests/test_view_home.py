from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEquals(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        """Must contain 1 form, 1 input, 2 selects, 1 button submit and 6 anchors of 'View Details'"""
        tags = [('<form', 1),
                ('<input', 1),
                ('<select', 2),
                ('type="submit"', 1),
                ('<a class="btn btn-default"', 6)]

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
