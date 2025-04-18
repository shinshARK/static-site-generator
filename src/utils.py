from src.textnode import TextNode, TextType
import re


# TODO: maybe shouldnt do an utils.py file?


# TODO: nested stuff TextNode as a ParentNode or smth
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split = node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(split)):
            if split[i] == "":
                continue  # skipping '' generated when formatted sections are right next to eachother (e.g. "_italics__italics_")
            if i % 2 == 0:
                new_nodes.append(TextNode(split[i], node.text_type))
            else:
                new_nodes.append(TextNode(split[i], text_type))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
