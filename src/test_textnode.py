import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_init(self):
        # Testing Default Values
        default_node = TextNode()
        self.assertEqual(default_node.text, "")
        self.assertEqual(default_node.text_type, TextType.NORMAL)
        self.assertEqual(default_node.url, None)
    
        # Testing Node with Non-Default Args
        param_node = TextNode("This is a text node", TextType.ITALIC, "https://www.test.com")
        self.assertEqual(param_node.text, "This is a text node")
        self.assertEqual(param_node.text_type, TextType.ITALIC)
        self.assertEqual(param_node.url, "https://www.test.com")

    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is not a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.BOLD, "Non-Default url")

        self.assertEqual(node1, node2)    # Should be equal
        self.assertNotEqual(node1, node3) # Unequal text
        self.assertNotEqual(node1, node4) # Unequal text_type
        self.assertNotEqual(node1, node5) # Unequal url

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        expected_repr = "TextNode(This is a text node, <TextType.BOLD: 'bold'>, https://www.test.com)"
        self.assertEqual(repr(node), expected_repr)

        # Other test cases for __repr__
        node2 = TextNode("Another text", TextType.LINK, "https://example.com")
        expected_repr2 = "TextNode(Another text, <TextType.LINK: 'link'>, https://example.com)"
        self.assertEqual(repr(node2), expected_repr2)

        # Test without URL
        node3 = TextNode("No URL", TextType.NORMAL)
        expected_repr3 = "TextNode(No URL, <TextType.NORMAL: 'normal'>, None)"
        self.assertEqual(repr(node3), expected_repr3)

if __name__ == "__main__":
    unittest.main()