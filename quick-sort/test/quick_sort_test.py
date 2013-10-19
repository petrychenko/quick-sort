'''
Created on Oct 10, 2013

@author: av
'''
import unittest
import quick_sort


class CSTest(unittest.TestCase):

    def setUp(self):
        self.collection = ['f','i','l','e','e','d','i','t']
        self.sorted_collection_asc = [1,2,4,4,4,6,8,13,22]
        self.shuffled_collection = [1,22,4,4,2,4]

    def tearDown(self):
        pass
    
    def testIsSortedAsc(self):
        self.assertTrue(quick_sort.is_sorted_asc(self.sorted_collection_asc))
        self.assertFalse(quick_sort.is_sorted_asc(self.shuffled_collection))
        self.assertFalse(self.sorted_collection_asc.reverse())
        self.assertTrue(quick_sort.is_sorted_asc([1]))
        self.assertTrue(quick_sort.is_sorted_asc([]))
        self.assertRaises(TypeError, quick_sort.is_sorted_asc, None )

    def testMyQuicksort(self):
        old_collection = self.collection
        self.collection = quick_sort.my_quick_sort( self.collection )
        self.assertTrue(quick_sort.is_sorted_asc(self.collection), 'collection is not sorted')
        self.assertCountEqual(old_collection, self.collection)

if __name__ == "__main__":
    unittest.main()