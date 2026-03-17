import unittest

from nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestNodesDelimiter(unittest.TestCase):
    
    def test_no_delimiter(self):
        
        node = TextNode("just plain text", TextType.TEXT) 
        
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result, [TextNode("just plain text", TextType.TEXT)])


    def test_simple_code_delimiter(self):

        node = TextNode("this is `code` text", TextType.TEXT)

        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result, [TextNode("this is ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text", TextType.TEXT)])

    def test_bold_delimiter(self):

        node = TextNode("this is **bold** text", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(result, [TextNode("this is ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)])

    def test_italic_delimiter(self):

        node = TextNode("this is _italic_ text", TextType.TEXT)

        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(result, [TextNode("this is ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" text", TextType.TEXT)])
   
    def test_unmatched_delimiter(self):

        node = TextNode("this is _broken text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_non_text_delimiter(self):

        node = TextNode("already bold", TextType.BOLD)

        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result, [TextNode("already bold", TextType.BOLD)])


    def test_multi_nodes_delimiter(self):

        node = TextNode("a `code` bit", TextType.TEXT)
        node2 = TextNode("already bold", TextType.BOLD)
        node3 = TextNode("plain ending", TextType.TEXT)

        result = split_nodes_delimiter([node, node2, node3], "`", TextType.CODE)

        self.assertEqual(result, [TextNode("a ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" bit", TextType.TEXT), TextNode("already bold", TextType.BOLD), TextNode("plain ending", TextType.TEXT)])
