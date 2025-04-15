import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_repr_basic(self):
        node = HTMLNode("h1", "test", None, None)
        self.assertEqual(
            "HTMLNode(tag='h1', value='test', children=None, props=None)",
            repr(node)
        )

    def test_to_html_not_implemented(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        with self.assertRaises(NotImplementedError):
            node.to_html()
        

    def test_repr_with_child(self):
        child = HTMLNode("h2", "heading 2!")
        node = HTMLNode("h1", "title", [child], None)
        self.assertEqual(
            "HTMLNode(tag='h1', value='title', children=[HTMLNode(tag='h2', value='heading 2!', children=None, props=None)], props=None)",
            repr(node)
        )

    def test_repr_with_props(self):
        node = HTMLNode("div", None, None, {"class": "container", "id": "main"})
        self.assertEqual(
            "HTMLNode(tag='div', value=None, children=None, props={'class': 'container', 'id': 'main'})",
            repr(node)
        )

    def test_repr_with_all_attributes(self):
        child = HTMLNode("span", "inner")
        node = HTMLNode("p", "paragraph", [child], {"style": "font-size: 16px"})
        self.assertEqual(
            "HTMLNode(tag='p', value='paragraph', children=[HTMLNode(tag='span', value='inner', children=None, props=None)], props={'style': 'font-size: 16px'})",
            repr(node)
        )

    def test_repr_with_multiple_children(self):
        child1 = HTMLNode("li", "Item 1")
        child2 = HTMLNode("li", "Item 2")
        child3 = HTMLNode("li", "Item 3")
        node = HTMLNode("ul", "list", [child1, child2, child3], {"class": "items"})
        self.assertEqual(
            "HTMLNode(tag='ul', value='list', children=[HTMLNode(tag='li', value='Item 1', children=None, props=None), HTMLNode(tag='li', value='Item 2', children=None, props=None), HTMLNode(tag='li', value='Item 3', children=None, props=None)], props={'class': 'items'})",
            repr(node)
        )

if __name__ == "__main__":
    unittest.main()