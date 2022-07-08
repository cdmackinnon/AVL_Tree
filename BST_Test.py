import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):

    def setUp(self):
        self.tester = Binary_Search_Tree()

    #empty
    def test_empty_tree_string(self):
        self.assertEqual('[ ]', str(self.tester))
    
    def test_empty_tree_in_order(self):
        self.assertEqual('[ ]', self.tester.in_order())

    def test_empty_tree_post_order(self):
        self.assertEqual('[ ]', self.tester.post_order())

    def test_empty_tree_pre_order(self):
        self.assertEqual('[ ]', self.tester.pre_order())

    def test_empty_height(self):
        self.assertEqual(0,self.tester.get_height())

    def test_remove_empty(self):
        try:
            self.tester.remove_element(1)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
        else:
            self.fail('No value error raised')

    #one value 
    def one_value_string(self):
        self.tester.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.tester))

    def test_insert_one_value_in_order(self):
        self.tester.insert_element(1)
        self.assertEqual('[ 1 ]', self.tester.in_order())

    def test_insert_one_value_post_order(self):
        self.tester.insert_element(1)
        self.assertEqual('[ 1 ]', self.tester.post_order())

    def test_insert_one_value_pre_order(self):
        self.tester.insert_element(1)
        self.assertEqual('[ 1 ]', self.tester.pre_order())

    def test_insert_one_value_height(self):
        self.tester.insert_element(1)
        self.assertEqual(1, self.tester.get_height())

    #two values
    def test_insert_two_value_in_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.assertEqual('[ 1, 2 ]', self.tester.in_order())

    def test_insert_two_value_pre_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.assertEqual('[ 1, 2 ]', self.tester.pre_order())

    def test_insert_two_value_post_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.assertEqual('[ 2, 1 ]', self.tester.post_order())

    def test_insert_two_value_height(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.assertEqual(2, self.tester.get_height())

    def test_insert_two_value_same(self):
        try:
            self.tester.insert_element(1)
            self.tester.insert_element(1)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
        else:
            self.fail('No value error raised')

    #three values
    def test_insert_full_tree_in_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(0)
        self.assertEqual('[ 0, 1, 2 ]', self.tester.in_order())

    def test_insert_full_tree_height(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(0)
        self.assertEqual(2, self.tester.get_height())

    def test_insert_full_tree_post_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(0)
        self.assertEqual('[ 0, 2, 1 ]', self.tester.post_order())

    def test_insert_full_tree_pre_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(0)
        self.assertEqual('[ 1, 0, 2 ]', self.tester.pre_order())

    def test_insert_full_tree_rotation_left_in_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.assertEqual('[ 1, 2, 3 ]', self.tester.in_order())
        
    def test_insert_full_tree_rotation_left_post_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.assertEqual('[ 1, 3, 2 ]', self.tester.post_order())

    def test_insert_full_tree_rotation_left_pre_order(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.assertEqual('[ 2, 1, 3 ]', self.tester.pre_order())

    def test_insert_full_tree_rotation_left_height(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.assertEqual(2, self.tester.get_height())

    def test_insert_full_tree_rotation_right_in_order(self):
        self.tester.insert_element(3)
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.assertEqual('[ 1, 2, 3 ]', self.tester.in_order())

    def test_insert_full_tree_rotation_right_post_order(self):
        self.tester.insert_element(3)
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.assertEqual('[ 1, 3, 2 ]', self.tester.post_order())

    def test_insert_full_tree_rotation_right_pre_order(self):
        self.tester.insert_element(3)
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.assertEqual('[ 2, 1, 3 ]', self.tester.pre_order())

    def test_insert_full_tree_rotation_right_height(self):
        self.tester.insert_element(3)
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.assertEqual(2, self.tester.get_height())

    #double rotations
    def test_insert_right_then_left_rotation_in_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(5)
        self.tester.insert_element(4)
        self.tester.insert_element(3)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]', self.tester.in_order())

    def test_insert_right_then_left_rotation_post_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(5)
        self.tester.insert_element(4)
        self.tester.insert_element(3)
        self.assertEqual('[ 1, 3, 5, 4, 2 ]', self.tester.post_order())

    def test_insert_right_then_left_rotation_pre_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(5)
        self.tester.insert_element(4)
        self.tester.insert_element(3)
        self.assertEqual('[ 2, 1, 4, 3, 5 ]', self.tester.pre_order())

    def test_insert_right_then_left_rotation_height(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(5)
        self.tester.insert_element(4)
        self.tester.insert_element(3)
        self.assertEqual(3, self.tester.get_height())

    def test_insertion_scaling(self):
        self.tester.insert_element(1)
        self.tester.insert_element(2)
        self.tester.insert_element(-3)
        self.tester.insert_element(4)
        self.tester.insert_element(-5)
        self.tester.insert_element(6)
        self.tester.insert_element(10)
        self.tester.insert_element(13)
        self.tester.insert_element(-22)
        self.tester.insert_element(-40)
        self.tester.insert_element(85)
        self.tester.insert_element(0)
        self.assertEqual('[ -40, -22, -5, -3, 0, 1, 2, 4, 6, 10, 13, 85 ]', str(self.tester))

    #removal
    def test_removal_single_node_in_order(self):
        self.tester.insert_element(1)
        self.tester.remove_element(1)
        self.assertEqual('[ ]', self.tester.in_order())

    def test_removal_single_node_height(self):
        self.tester.insert_element(1)
        self.tester.remove_element(1)
        self.assertEqual(0, self.tester.get_height())

    def test_removal_single_node_post_order(self):
        self.tester.insert_element(1)
        self.tester.remove_element(1)
        self.assertEqual('[ ]', self.tester.post_order())

    def test_removal_single_node_pre_order(self):
        self.tester.insert_element(1)
        self.tester.remove_element(1)
        self.assertEqual('[ ]', self.tester.pre_order())

    def test_removal_one_of_3_in_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(3)
        self.tester.remove_element(3)
        self.assertEqual('[ 1, 2 ]', self.tester.in_order())

    def test_removal_one_of_3_post_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(3)
        self.tester.remove_element(3)
        self.assertEqual('[ 1, 2 ]', self.tester.post_order())

    def test_removal_one_of_3_pre_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(3)
        self.tester.remove_element(3)
        self.assertEqual('[ 2, 1 ]', self.tester.pre_order())

    def test_removal_one_of_3_height(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(3)
        self.tester.remove_element(3)
        self.assertEqual(2, self.tester.get_height())

    def test_removal_root_in_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(1)
        self.tester.remove_element(2)
        self.assertEqual('[ 1, 3 ]', self.tester.in_order())

    def test_removal_root_pre_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(1)
        self.tester.remove_element(2)
        self.assertEqual('[ 3, 1 ]', self.tester.pre_order())

    def test_removal_root_post_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(1)
        self.tester.remove_element(2)
        self.assertEqual('[ 1, 3 ]', self.tester.post_order())

    def test_removal_root_in_order_height(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(1)
        self.tester.remove_element(2)
        self.assertEqual(2, self.tester.get_height())

    def test_removal_root_right_leaf_in_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(5)
        self.tester.insert_element(4)
        self.tester.remove_element(2)
        self.assertEqual('[ 1, 4, 5 ]', self.tester.in_order())

    def test_removal_root_right_leaf_pre_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(5)
        self.tester.insert_element(4)
        self.tester.remove_element(2)
        self.assertEqual('[ 4, 1, 5 ]', self.tester.pre_order())   

    def test_removal_root_right_leaf_post_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(1)
        self.tester.insert_element(5)
        self.tester.insert_element(4)
        self.tester.remove_element(2)
        self.assertEqual('[ 1, 5, 4 ]', self.tester.post_order())

    def test_removal_root_left_leaf_in_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-3)
        self.tester.insert_element(0)
        self.tester.remove_element(2)
        self.assertEqual('[ -3, 0, 3 ]', self.tester.in_order())

    def test_removal_root_left_leaf_post_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-3)
        self.tester.insert_element(0)
        self.tester.remove_element(2)
        self.assertEqual('[ -3, 3, 0 ]', self.tester.post_order())

    def test_removal_root_left_leaf_pre_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-3)
        self.tester.insert_element(0)
        self.tester.remove_element(2)
        self.assertEqual('[ 0, -3, 3 ]', self.tester.pre_order())

    def test_removal_root_left_leaf_height(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-3)
        self.tester.insert_element(0)
        self.tester.remove_element(2)
        self.assertEqual(2, self.tester.get_height())
        
    #removal unbalanced other side
    def test_removal_root_left_unbalance_in_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-3)
        self.tester.insert_element(-4)
        self.tester.remove_element(3)
        self.assertEqual('[ -4, -3, 2 ]', self.tester.in_order())

    def test_removal_root_left_unbalance_pre_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-3)
        self.tester.insert_element(-4)
        self.tester.remove_element(3)
        self.assertEqual('[ -3, -4, 2 ]', self.tester.pre_order())

    def test_removal_root_left_unbalance_post_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-3)
        self.tester.insert_element(-4)
        self.tester.remove_element(3)
        self.assertEqual('[ -4, 2, -3 ]', self.tester.post_order())

    def test_removal_root_right_unbalance_in_order(self):
        self.tester.insert_element(3)
        self.tester.insert_element(2)
        self.tester.insert_element(4)
        self.tester.insert_element(5)
        self.tester.remove_element(2)
        self.assertEqual('[ 3, 4, 5 ]', self.tester.in_order())

    def test_removal_root_right_unbalance_pre_order(self):
        self.tester.insert_element(3)
        self.tester.insert_element(2)
        self.tester.insert_element(4)
        self.tester.insert_element(5)
        self.tester.remove_element(2)
        self.assertEqual('[ 4, 3, 5 ]', self.tester.pre_order())

    def test_removal_root_right_unbalance_post_order(self):
        self.tester.insert_element(3)
        self.tester.insert_element(2)
        self.tester.insert_element(4)
        self.tester.insert_element(5)
        self.tester.remove_element(2)
        self.assertEqual('[ 3, 5, 4 ]', self.tester.post_order())

    def test_removal_double_rotation_left_side_in_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-4)
        self.tester.insert_element(-2)
        self.tester.remove_element(3)
        self.assertEqual('[ -4, -2, 2 ]', self.tester.in_order())

    def test_removal_double_rotation_left_side_pre_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-4)
        self.tester.insert_element(-2)
        self.tester.remove_element(3)
        self.assertEqual('[ -2, -4, 2 ]', self.tester.pre_order())

    def test_removal_double_rotation_left_side_post_order(self):
        self.tester.insert_element(2)
        self.tester.insert_element(3)
        self.tester.insert_element(-4)
        self.tester.insert_element(-2)
        self.tester.remove_element(3)
        self.assertEqual('[ -4, 2, -2 ]', self.tester.post_order())

    def test_multi_rotation_insertion_in_order(self):
        self.tester.insert_element(0)
        self.tester.insert_element(15)
        self.tester.insert_element(14)
        self.tester.insert_element(13)
        self.tester.insert_element(12)
        self.tester.insert_element(11)
        self.tester.insert_element(10)
        self.assertEqual('[ 0, 10, 11, 12, 13, 14, 15 ]', self.tester.in_order())

    def test_multi_rotation_insertion_post_order(self):
        self.tester.insert_element(0)
        self.tester.insert_element(15)
        self.tester.insert_element(14)
        self.tester.insert_element(13)
        self.tester.insert_element(12)
        self.tester.insert_element(11)
        self.tester.insert_element(10)
        self.assertEqual('[ 0, 11, 10, 13, 15, 14, 12 ]', self.tester.post_order())

    def test_multi_rotation_insertion_pre_order(self):
        self.tester.insert_element(0)
        self.tester.insert_element(15)
        self.tester.insert_element(14)
        self.tester.insert_element(13)
        self.tester.insert_element(12)
        self.tester.insert_element(11)
        self.tester.insert_element(10)
        self.assertEqual('[ 12, 10, 0, 11, 14, 13, 15 ]', self.tester.pre_order())
    
    #hybrid
    def test_multi_rotation_insertion_height(self):
        self.tester.insert_element(0)
        self.tester.insert_element(15)
        self.tester.insert_element(14)
        self.tester.insert_element(13)
        self.tester.insert_element(12)
        self.tester.insert_element(11)
        self.tester.insert_element(10)
        self.assertEqual(3, self.tester.get_height())

    #multiple rotation tree (fibonacci)
    def test_fibonacci_removal_balance_in_order(self):
        self.tester.insert_element(21)
        self.tester.insert_element(13)
        self.tester.insert_element(29)
        self.tester.insert_element(8)
        self.tester.insert_element(18)
        self.tester.insert_element(26)
        self.tester.insert_element(32)
        self.tester.insert_element(5)
        self.tester.insert_element(11)
        self.tester.insert_element(16)
        self.tester.insert_element(20)
        self.tester.insert_element(24)
        self.tester.insert_element(28)
        self.tester.insert_element(31)
        self.tester.insert_element(33)
        self.tester.insert_element(3)
        self.tester.insert_element(7)
        self.tester.insert_element(10)
        self.tester.insert_element(12)
        self.tester.insert_element(15)
        self.tester.insert_element(17)
        self.tester.insert_element(19)
        self.tester.insert_element(23)
        self.tester.insert_element(25)
        self.tester.insert_element(27)
        self.tester.insert_element(30)
        self.tester.insert_element(2)
        self.tester.insert_element(4)
        self.tester.insert_element(6)
        self.tester.insert_element(9)
        self.tester.insert_element(14)
        self.tester.insert_element(22)
        self.tester.insert_element(1)

        self.tester.remove_element(32)
        self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33 ]', self.tester.in_order())

    def test_fibonacci_removal_balance_post_order(self):
        self.tester.insert_element(21)
        self.tester.insert_element(13)
        self.tester.insert_element(29)
        self.tester.insert_element(8)
        self.tester.insert_element(18)
        self.tester.insert_element(26)
        self.tester.insert_element(32)
        self.tester.insert_element(5)
        self.tester.insert_element(11)
        self.tester.insert_element(16)
        self.tester.insert_element(20)
        self.tester.insert_element(24)
        self.tester.insert_element(28)
        self.tester.insert_element(31)
        self.tester.insert_element(33)
        self.tester.insert_element(3)
        self.tester.insert_element(7)
        self.tester.insert_element(10)
        self.tester.insert_element(12)
        self.tester.insert_element(15)
        self.tester.insert_element(17)
        self.tester.insert_element(19)
        self.tester.insert_element(23)
        self.tester.insert_element(25)
        self.tester.insert_element(27)
        self.tester.insert_element(30)
        self.tester.insert_element(2)
        self.tester.insert_element(4)
        self.tester.insert_element(6)
        self.tester.insert_element(9)
        self.tester.insert_element(14)
        self.tester.insert_element(22)
        self.tester.insert_element(1)

        self.tester.remove_element(32)
        self.assertEqual('[ 1, 2, 4, 3, 6, 7, 5, 9, 10, 12, 11, 8, 14, 15, 17, 16, 19, 20, 18, 13, 22, 23, 25, 24, 27, 28, 26, 30, 31, 33, 29, 21 ]', self.tester.post_order())

    def test_fibonacci_removal_balance_pre_order(self):
        self.tester.insert_element(21)
        self.tester.insert_element(13)
        self.tester.insert_element(29)
        self.tester.insert_element(8)
        self.tester.insert_element(18)
        self.tester.insert_element(26)
        self.tester.insert_element(32)
        self.tester.insert_element(5)
        self.tester.insert_element(11)
        self.tester.insert_element(16)
        self.tester.insert_element(20)
        self.tester.insert_element(24)
        self.tester.insert_element(28)
        self.tester.insert_element(31)
        self.tester.insert_element(33)
        self.tester.insert_element(3)
        self.tester.insert_element(7)
        self.tester.insert_element(10)
        self.tester.insert_element(12)
        self.tester.insert_element(15)
        self.tester.insert_element(17)
        self.tester.insert_element(19)
        self.tester.insert_element(23)
        self.tester.insert_element(25)
        self.tester.insert_element(27)
        self.tester.insert_element(30)
        self.tester.insert_element(2)
        self.tester.insert_element(4)
        self.tester.insert_element(6)
        self.tester.insert_element(9)
        self.tester.insert_element(14)
        self.tester.insert_element(22)
        self.tester.insert_element(1)

        self.tester.remove_element(32)
        self.assertEqual('[ 21, 13, 8, 5, 3, 2, 1, 4, 7, 6, 11, 10, 9, 12, 18, 16, 15, 14, 17, 20, 19, 29, 26, 24, 23, 22, 25, 28, 27, 33, 31, 30 ]', self.tester.pre_order())
    
    #multi insert+remove
    def test_multi_insert_remove_in_order(self):
        self.tester.insert_element(0)
        self.tester.insert_element(-1)
        self.tester.insert_element(1)
        self.tester.insert_element(-2)
        self.tester.remove_element(1)
        self.tester.remove_element(-1)
        self.assertEqual('[ -2, 0 ]', self.tester.in_order())

    def test_multi_insert_remove_post_order(self):
        self.tester.insert_element(0)
        self.tester.insert_element(-1)
        self.tester.insert_element(1)
        self.tester.insert_element(-2)
        self.tester.remove_element(1)
        self.tester.remove_element(-1)
        self.assertEqual('[ -2, 0 ]', self.tester.post_order())

    def test_multi_insert_remove_pre_order(self):
        self.tester.insert_element(0)
        self.tester.insert_element(-1)
        self.tester.insert_element(1)
        self.tester.insert_element(-2)
        self.tester.remove_element(1)
        self.tester.remove_element(-1)
        self.assertEqual('[ 0, -2 ]', self.tester.pre_order())

   
if __name__ == '__main__':
  unittest.main()