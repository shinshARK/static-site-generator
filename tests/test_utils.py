import unittest

from src.utils import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)
from src.textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_multiple_bold(self):
        node = TextNode(
            "This is a text with **multiple** bold **usages** yep", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is a text with ", TextType.TEXT),
            TextNode("multiple", TextType.BOLD),
            TextNode(" bold ", TextType.TEXT),
            TextNode("usages", TextType.BOLD),
            TextNode(" yep", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_consecutive_italics(self):
        node = TextNode("Testing consecutive _italics__italics2_ asdf", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("Testing consecutive ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode("italics2", TextType.ITALIC),
            TextNode(" asdf", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_multinode(self):
        node1 = TextNode("Testing `print('hello 1')` testing 1", TextType.TEXT)
        node2 = TextNode("Testing `print('hello 2')` testing 2", TextType.TEXT)
        node3 = TextNode("Testing `print('hello 3')` testing 3", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        expected_nodes = [
            TextNode("Testing ", TextType.TEXT),
            TextNode("print('hello 1')", TextType.CODE),
            TextNode(" testing 1", TextType.TEXT),
            TextNode("Testing ", TextType.TEXT),
            TextNode("print('hello 2')", TextType.CODE),
            TextNode(" testing 2", TextType.TEXT),
            TextNode("Testing ", TextType.TEXT),
            TextNode("print('hello 3')", TextType.CODE),
            TextNode(" testing 3", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_no_closing_delimiter(self):
        node = TextNode("Testing `print('hello world') testing", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.ITALIC)

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()
