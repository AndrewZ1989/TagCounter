import unittest
from tagParsing.storage import TagsStorage


class MyTestCase(unittest.TestCase):
    def test_usage_of_storage_without_context(self):
        st = TagsStorage()
        with self.assertRaises(AttributeError):
            st.saveTagsFor('testSite', {"a": 1, "div": 5})

    def test_save_in_storage(self):
        with TagsStorage() as st:
            original = {"a": 1, "div": 5}
            st.saveTagsFor("address", original)
            actual = st.getTagsFor("address")
            self.assertEqual(original, actual)


if __name__ == '__main__':
    unittest.main()
