from src.textnode import TextNode, TextType


# TODO: nested stuff TextNode as a ParentNode or smth
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        string = ""
        stack = []
        i = 0
        while i < len(node.text):
            # print("---------")
            # print(new_nodes)
            # print(string)
            # print(node.text[i])
            # print(i)
            if node.text[i] != delimiter:
                string += node.text[i]
            elif len(stack) == 0:
                if len(string) != 0:
                    new_nodes.append(TextNode(string, TextType.TEXT))
                string = ""
                if delimiter == "*":
                    i += 1
                stack += node.text[i]
            else:
                if len(string) != 0:
                    new_nodes.append(TextNode(string, text_type))
                string = ""
                if delimiter == "*":
                    i += 1
                if stack[-1] == node.text[i]:
                    stack = stack[:-1]
                else:  # TODO: this is supposed to be for nesting but idk later
                    stack += node.text[i]

            i += 1
        if len(stack) != 0:
            raise Exception("invalid markdown")

        if len(string) != 0:
            new_nodes.append(TextNode(string, TextType.TEXT))
    # print(new_nodes)
    return new_nodes


def get_delimiter_indices(string, delimiter):
    return [index for index, char in enumerate(string) if char == delimiter]
