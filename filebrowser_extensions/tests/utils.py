"""
Tests for :class:`filebrowser_extensions.utils`
"""
from django.test import TestCase
from filebrowser_extensions.utils import is_extend_value


class FBEIsExtendValueCase(TestCase):
    """
    Check if :func:`is_extend_value` return correct values depends
    on different settings
    """

    def test_true_extend_value(self):
        """
        Give string that should be recognized as extended value
        """
        self.assertTrue(is_extend_value('app_label.model_name:pk'))

    def test_link_value(self):
        """
        Give string with link as example youtube that
        Shouldn't be recognized as extended value
        """
        self.assertFalse(is_extend_value(
            'https://www.youtube.com/watch?v=CGyEd0aKWZE'))

    def test_file_path(self):
        self.assertFalse(is_extend_value(
            '/upload_to/folder/file.jpg'
        ))

        self.assertFalse(is_extend_value(
            'upload_to/folder/file.jpg'
        ))

    def test_wrong_extend_value_format(self):
        self.assertFalse(is_extend_value('app_labelmodel_namepk'))
        self.assertFalse(is_extend_value('app_label.model_name'))
        self.assertFalse(is_extend_value('app_labelmodel_name:pk'))
        self.assertFalse(is_extend_value('app_labelmodel_name:'))
        self.assertFalse(is_extend_value(':pk'))
        self.assertFalse(is_extend_value('.:'))
        self.assertFalse(is_extend_value(':'))
        self.assertFalse(is_extend_value('.'))
