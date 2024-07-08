import unittest
from htmlnode import HTMLNode

def test_props_to_html():
    node = HTMLNode(tag = "a", value = "Example", props={"href": "https://www.example.com", "target": "_blank"})
    result = node.props_to_html()
    expected_result = ' href="https://www.example.com" target="_blank"'
    assert result == expected_result, f'Expected: {expected_result}, but got: {result}'

def test_repr():
    child1 = HTMLNode(tag = "p", value = "This is a paragraph.")
    child2 = HTMLNode(tag = "a", value = "Click here", props = {"href": "https://www.example.com"})
    parent = HTMLNode(tag = "div", children = [child1, child2], props = {"class": "container"})
    result = repr(parent)
    expected_result = ("tag: div\nvalue: None\nchildren: [HTMLNode(tag=p, value=This is a paragraph., "
                       "children=[], props={}), HTMLNode(tag=a, value=Click here, "
                       "children=[], props={'href': 'https://www.example.com'})]\nprops: {'class': 'container'}")
    assert result == expected_result, f'Expected: {expected_result}, but got: {result}'

if __name__ == "main":
    unittest.main()