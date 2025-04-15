from textnode import TextNode, TextType
from htmlnode import HTMLNode
def main():
    test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test)

    testhtml = HTMLNode("test", "value", None, None)
    testhtml2 = HTMLNode("test", "value", testhtml, None)
    print(testhtml2)

main()