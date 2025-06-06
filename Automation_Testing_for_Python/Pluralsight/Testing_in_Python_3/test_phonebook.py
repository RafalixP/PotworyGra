import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = Phonebook()
    
    def test_lookup_by_name(self):
        #phonebook = Phonebook()
        self.phonebook.add('Bob', '12345')

        print(phonebook.numbers)  # Debugging line

        number = phonebook.lookup('Bob')

        print(number)  # Debugging line

        self.assertEqual(number, '12345')

    #@unittest.skip('Work in progress2')
    def test_missing_name(self):
        #phonebook = Phonebook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    @unittest.skip('Work in progress3')
    def test_empty_phonebook_is_consistent(self):
        #phonebook = Phonebook()
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

if __name__ == '__main__':
    unittest.main()

