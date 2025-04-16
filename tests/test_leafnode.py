import unittest

from src.htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(), "Click me!")

    def test_values(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.tag,
            "a",
        )
        self.assertEqual(
            node.value,
            "Click me!",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            {"href": "https://www.google.com"},
        )

    def test_leaf_to_html_missing_value(self):
        with self.assertRaises(ValueError):
            LeafNode(None, None, None).to_html()

    def test_repr_no_props(self):
        node = LeafNode("span", "Text content")
        self.assertEqual(
            repr(node), "LeafNode(tag='span', value='Text content', props=None)"
        )

    def test_repr_with_props(self):
        node = LeafNode(
            "img", "Image description", {"src": "image.png", "alt": "Image"}
        )
        self.assertEqual(
            repr(node),
            "LeafNode(tag='img', value='Image description', props={'src': 'image.png', 'alt': 'Image'})",
        )

    def test_repr_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(
            repr(node), "LeafNode(tag=None, value='Just text', props=None)"
        )


if __name__ == "__main__":
    unittest.main()
