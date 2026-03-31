from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            
            if len(parts) % 2 == 0:
                raise Exception("Invalid Markdown syntax")

            else:
                for i, part in enumerate(parts):
                    if part == "":
                        continue

                    if i % 2 == 0:
                        new_nodes.append(TextNode(part, TextType.TEXT))

                    else:
                        new_nodes.append(TextNode(part, text_type))

    return new_nodes


def extract_markdown_images(text):
    return text

text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]    
