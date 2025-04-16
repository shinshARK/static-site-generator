import unittest

from src.htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_plain_child(self):
        child_node = LeafNode(None, "Hello")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div>Hello</div>")

    def test_to_html_list(self):
        li_1 = LeafNode("li", "First")
        li_2 = LeafNode("li", "Second")
        li_3 = LeafNode("li", "Third")
        ul = ParentNode("ul", [li_1, li_2, li_3])
        self.assertEqual(
            ul.to_html(), "<ul><li>First</li><li>Second</li><li>Third</li></ul>"
        )

    def test_missing_tag_raises_error(self):
        node = ParentNode(None, [LeafNode("p", "text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_missing_children_raises_error(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_with_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_parent_with_props(self):
        child = LeafNode("span", "text")
        node = ParentNode("div", [child], {"id": "main", "class": "container"})
        self.assertEqual(
            node.to_html(), '<div id="main" class="container"><span>text</span></div>'
        )

    def test_complex_nesting(self):
        text1 = LeafNode(None, "Hello ")
        bold = LeafNode("b", "bold")
        text2 = LeafNode(None, " world")
        paragraph = ParentNode("p", [text1, bold, text2])

        link = ParentNode("a", [LeafNode(None, "Click me")], {"href": "#"})
        div = ParentNode("div", [paragraph, link])

        self.assertEqual(
            div.to_html(),
            '<div><p>Hello <b>bold</b> world</p><a href="#">Click me</a></div>',
        )

    def test_repr_no_children_no_props(self):
        node = ParentNode("div", [])
        self.assertEqual(repr(node), "ParentNode(tag='div', children=[], props=None)")

    def test_repr_with_children_no_props(self):
        child = LeafNode("span", "child")
        node = ParentNode("p", [child])
        self.assertEqual(
            repr(node),
            "ParentNode(tag='p', children=[LeafNode(tag='span', value='child', props=None)], props=None)",
        )

    def test_repr_no_children_with_props(self):
        node = ParentNode("a", [], {"href": "#"})
        self.assertEqual(
            repr(node), "ParentNode(tag='a', children=[], props={'href': '#'})"
        )

    def test_repr_with_children_with_props(self):
        child = LeafNode("b", "bold")
        node = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(
            repr(node),
            "ParentNode(tag='div', children=[LeafNode(tag='b', value='bold', props=None)], props={'class': 'container'})",
        )

    def test_repr_with_multiple_children(self):
        child1 = LeafNode("li", "item1")
        child2 = LeafNode("li", "item2")
        node = ParentNode("ul", [child1, child2])
        self.assertEqual(
            repr(node),
            "ParentNode(tag='ul', children=[LeafNode(tag='li', value='item1', props=None), LeafNode(tag='li', value='item2', props=None)], props=None)",
        )

    def test_repr_with_nested_parent_node(self):
        nested_child = ParentNode("span", [LeafNode(None, "inner")])
        node = ParentNode("div", [nested_child])
        self.assertEqual(
            repr(node),
            "ParentNode(tag='div', children=[ParentNode(tag='span', children=[LeafNode(tag=None, value='inner', props=None)], props=None)], props=None)",
        )

    def test_repr_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "text")])
        self.assertEqual(
            repr(node),
            "ParentNode(tag=None, children=[LeafNode(tag='p', value='text', props=None)], props=None)",
        )

    def test_repr_empty_props(self):
        node = ParentNode("div", [LeafNode("span", "text")], {})
        self.assertEqual(
            repr(node),
            "ParentNode(tag='div', children=[LeafNode(tag='span', value='text', props=None)], props={})",
        )


if __name__ == "__main__":
    unittest.main()
