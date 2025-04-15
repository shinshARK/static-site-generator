from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode

def main():
    # test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # print(test)

    # testhtml = HTMLNode("test", "value", None, None)
    # testhtml2 = HTMLNode("test", "value", testhtml, None)
    # print(testhtml2)

    # print(LeafNode("p", "This is a paragraph of text.").to_html())
    # print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])

    print(parent_node.to_html())

main()