#!/usr/bin/env python3
""" Parameterizing the unit test, Mock HTTP calls, Parameterizing and patching """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ TESTCASE """
    """ testing function for  inputs """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """ testing the method to return expected results """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    """  test that the KeyError is raised for inputs """
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ method to test a KeyError is properly raised """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ TESTCASE """
    """ testing function for inputs """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test utils.get_json will return expected result """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ TESTCASE """
    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result is
            returned but a_method is only called once using assert_called_once
        """
        class TestClass:
            """ class """
            def a_method(self):
                """ method  """
                return 42

            @memoize
            def a_property(self):
                """ the property """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
