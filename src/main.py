from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.LINK:
            return LeafNode("a", '', {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid text type")
            
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