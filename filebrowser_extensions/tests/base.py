"""
Tests for :class:`filebrowser_extensions.base.FBExtensionObject`
"""
from django.core.management import call_command
from django.test import TestCase, modify_settings

from filebrowser_extensions.base import FBExtensionObject
from filebrowser_extensions.exceptions import FBExtensionObjectException


class FBEInitTestCase(TestCase):
    """
    Test cases for initialise FBExtensionObject
    """

    def test_value_init(self):
        """
        Test around initialize FBExtensionObject using different values like
        int floats and badly formatted strings.
        """

        self.assertRaises(AssertionError, FBExtensionObject, value=1)
        self.assertRaises(AssertionError, FBExtensionObject, value=1.1)

        self.assertRaises(
            FBExtensionObjectException,
            FBExtensionObject,
            value='somestring'
        )

        self.assertRaises(
            FBExtensionObjectException,
            FBExtensionObject,
            value='model_name:1'
        )

        self.assertRaises(
            FBExtensionObjectException,
            FBExtensionObject,
            value='model_name:1'
        )

        self.assertRaises(
            FBExtensionObjectException,
            FBExtensionObject,
            value=':'
        )

        self.assertRaises(
            FBExtensionObjectException,
            FBExtensionObject,
            value=':1'
        )

        self.assertRaises(
            FBExtensionObjectException,
            FBExtensionObject,
            value='app_label.model_name'
        )

        self.assertRaises(
            FBExtensionObjectException,
            FBExtensionObject,
            value='app_label.model_name:'
        )

        FBExtensionObject(value='app_label.model_name:pk')

    def test_versions(self):
        """
        tests initialize FBExtensionObject with different version
        """
        self.assertRaises(
            AssertionError,
            FBExtensionObject,
            value='app_label.model_name:pk',
            version_suffix='this_one_doeas_not_exists!!!!'
        )

        FBExtensionObject(
            value='app_label.model_name:pk',
            version_suffix='admin_thumbnail'
        )


class FBEContentObjectTestCase(TestCase):
    """
    Test if content object is handling correctly depends on delivered
    value
    """

    @modify_settings(INSTALLED_APPS={
        'append': 'filebrowser_extensions.tests.fbe_testing_app',
    })
    def test_getting_content_object(self):
        """Test if content object is get correctly if delivered value is ok"""

        from .fbe_testing_app.models import TestExtension
        call_command('migrate', noinput=True)

        te_instnace = TestExtension.objects.create(
            name='TestName', code='TestCode')

        fbe = FBExtensionObject(value='fbe_testing_app.testextension:1')
        self.assertEqual(fbe.content_object, te_instnace)

    @modify_settings(INSTALLED_APPS={
        'append': 'filebrowser_extensions.tests.fbe_testing_app',
    })
    def test_wrong_id(self):
        """
        Make sure that content object will not be returned if
        if object of given id not exists. (For example it was deleted).
        """

        from .fbe_testing_app.models import TestExtension
        call_command('migrate', noinput=True)

        # create one object with id=1 in value for FBExtensionObject we will
        # put id=2 so we shouldn't be able to get any content object up there
        TestExtension.objects.create(
            name='TestName', code='TestCode'
        )

        fbe = FBExtensionObject(value='fbe_testing_app.testextension:2')
        self.assertEqual(fbe.content_object, None)


class FBEExistsTestCase(TestCase):
    """
    Check if content object actually exists or not
    """

    @modify_settings(INSTALLED_APPS={
        'append': 'filebrowser_extensions.tests.fbe_testing_app',
    })
    def test_object_exists(self):
        """
        exists should return True if object actually exists
        """
        from .fbe_testing_app.models import TestExtension
        call_command('migrate', noinput=True)

        TestExtension.objects.create(
            name='TestName', code='TestCode')

        fbe = FBExtensionObject(value='fbe_testing_app.testextension:1')
        self.assertTrue(fbe.exists)

    @modify_settings(INSTALLED_APPS={
        'append': 'filebrowser_extensions.tests.fbe_testing_app',
    })
    def test_object_not_exists(self):
        """
        exists should return True if object actually exists
        """
        from .fbe_testing_app.models import TestExtension
        call_command('migrate', noinput=True)

        TestExtension.objects.create(
            name='TestName', code='TestCode')

        fbe = FBExtensionObject(value='fbe_testing_app.testextension:2')
        self.assertFalse(fbe.exists)
