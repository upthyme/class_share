
import unittest
import random
import Stack

class StackTests(unittest.TestCase):
    #tests the functions of the Stack

    #all test functions have to start with the word "test", otherwise they don't run
    def test_create_stack(self):
        """test to see if stack is initialized correctly, and that size is 0 and is_empty is True"""
        s = Stack.Stack()
        self.assertIsInstance(s, Stack.Stack)
        self.assertTrue(s.is_empty(),"stack should be empty, but is_empty says it isn't")
        self.assertTrue(s.size() == 0,"Size should be 0, but size() is returning something else")

    def test_empty_string(self):
        """test to make sure that the empty stack is represented as "[]" """
        s = Stack.Stack()
        self.assertEqual(str(s), "[]", "an empty stack should be represented as [] as a string")


    def test_push_1(self):
        """test to see if the push function works with one item, and that the """
        s = Stack.Stack()
        s.push(5)
        self.assertTrue(s.size() == 1, "size of an empty list should be 0")
        self.assertFalse(s.is_empty(), "a stack with no items should return True from is_empty")

    def test_string_1(self):
        """test that the string for a stack with just 5 is [5]"""
        s = Stack.Stack()
        s.push(5)
        self.assertEqual(str(s),"[5]","a stack that only contains 5 should print [5]" )

    def test_push_5(self):
        """test that pushing 5 items of various types results in the correct size, and there's no runtime errors"""
        s = Stack.Stack()
        s.push(5)
        s.push("ten")
        s.push([7,8,9])
        s.push("To be, or not to be?")
        s.push(Stack.Stack())
        self.assertEqual(s.size(),5, "after calling push() 5 times, the size of the stack should be 5")

    def test_string_5(self):
        """testing the string function, but with simpler input than the last test"""
        s = Stack.Stack()
        s.push(5)
        s.push(7)
        s.push(8)
        s.push("nine")
        s.push(10)
        self.assertEqual(str(s),"[5, 7, 8, nine, 10]", "a stack that has 5,7,8,'nine',10 pushed to it should print as: [5, 7, 8, nine, 10]")


    def test_push_lots(self):
        """make a huge stack and make sure it runs OK and that size and is_empty are returning the right values"""
        s = Stack.Stack()
        for i in range(0,10000):
            s.push(random.randint(0,10000))
        self.assertEqual(s.size(),10000,"stack should have 10000 items, but size() is returning something else")
        self.assertFalse(s.is_empty(),"stack should not be empty, but is_empty says it is")


    def test_peek_1(self):
        """test that peek with a single item in the stack returns the correct item"""
        s = Stack.Stack()
        s.push(5)
        self.assertEqual(s.peek(),5, "If the only item in the stack is 5, peek should return 5")


    def test_peek_5(self):
        """test that after pushing 5 items, peek returns the correct one"""
        #BTW, 5 has no special meaning here, it's just a number that's bigger than 1 and more interesting than 2
        s = Stack.Stack()
        s.push(5)
        s.push(7)
        s.push(8)
        s.push("nine")
        s.push(10)
        self.assertEqual(s.peek(),10, "If the last item pushed to a stack of five objects is 10, peek should return 10")

    def test_pop_1(self):
        """test that pop works after pushing 1 item to the stack. The stack should return the item added, then be empty again."""
        s = Stack.Stack()
        s.push(5)
        self.assertEqual(s.pop(),5,"stack should return 5")
        self.assertTrue(s.is_empty(),"stack should be empty after popping only item from stack")
        self.assertEqual(s.size(),0, "stack should be size 0 after popping only item from stack")


    def test_pop_5(self):
        """test that pop works after pushing 5 items to the stack. The stack should return the item added, but still have size = 4 and not be empty"""
        s = Stack.Stack()
        s.push(5)
        s.push(7)
        s.push(8)
        s.push("nine")
        s.push(10)
        self.assertEqual(s.pop(),10, "if a stack has five items and the last is 10, pop should return 10")
        self.assertFalse(s.is_empty(),"after popping an item from a stack of 4, is_empty should return False")
        self.assertEqual(s.size(),4,"after popping from a Stack of 5, size() should return 4")


    def test_pop_5_all(self):
        """test that pop works after pushing 5 items to the stack. Each item should be returned in the opposite order it was added"""
        #I probably should have put each of these in a separate test, with one assert per test, but that would be so tedious...
        s = Stack.Stack()
        s.push(5)
        s.push(7)
        s.push(8)
        s.push("nine")
        s.push(10)
        self.assertEqual(s.pop(),10,"the first item to be popped from a stack of 5,7,8,'nine',10 should be 5")
        self.assertEqual(s.pop(),"nine","the second item to be popped from a stack of 5,7,8,'nine',10 should be 5")
        self.assertEqual(s.pop(),8,"the third item to be popped from a stack of 5,7,8,'nine',10 should be 5")
        self.assertEqual(s.pop(),7,"the fourth item to be popped from a stack of 5,7,8,'nine',10 should be 5")
        self.assertEqual(s.pop(),5,"the last item to be popped from a stack of 5,7,8,'nine',10 should be 5")


    def test_pop_empty_list(self):
        """the default stack in the book will error if you pop from an empty list; we want to fix it so that it just returns None"""
        s = Stack.Stack()
        self.assertEqual(s.pop(),None, "pop should return None if you pop from an empty Stack")

    def test_peek_empty_list(self):
        """the default stack in the book will error if you peek at an empty list; we want to fix it so that it just returns None"""
        s = Stack.Stack()
        self.assertEqual(s.peek(),None,"Stack should return None if you peek at an empty Stack")

 
    def test_string_2(self):
        """test that the string for a stack with 5, 6, 7 is [5, 6, 7]"""
        s = Stack.Stack()
        s.push(5)
        s.push(6)
        s.push(7)
        self.assertEqual(str(s),"[5, 6, 7]","the string for a stack with 5, 6, 7 is [5, 6, 7]")

    def test_string_3(self):
        """test that the string for a stack with 5, "six", 7 is [5, six, 7]"""
        s = Stack.Stack()
        s.push(5)
        s.push("six")
        s.push(7)
        self.assertEqual(str(s),"[5, six, 7]","the string for a stack with 5, 'six', 7 is [5, six, 7]")

if __name__ == '__main__':
    unittest.main()
