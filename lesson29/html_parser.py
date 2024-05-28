from bs4 import BeautifulSoup

class Node:
    # Class representing a node in the tree.
    def __init__(self, tag, text=None):
        # Initialize a new node with a given tag and text.
        self.tag = tag
        self.text = text
        self.children = []

    def __repr__(self):
        # Return a string representing the node.
        return f"<Node: {self.tag}>"

def parse_html(html_content):
    # Parse HTML and create the DOM tree.
    soup = BeautifulSoup(html_content, 'html.parser')
    root = Node(tag=soup.name)

    def parse_node(parent, element):
        # Recursively add nodes to the tree from HTML elements.
        for child in element.children:
            if child.name:
                new_node = Node(tag=child.name, text=child.string)
                parent.children.append(new_node)
                parse_node(new_node, child)
            elif child.string.strip():  # If there is text (not an empty string)
                parent.children.append(Node(tag=None, text=child.string.strip()))

    parse_node(root, soup)
    return root

def search_text_by_tag(root, target_tag):
    # Search for text by a given tag in the DOM tree.
    result = []

    def dfs(node):
        # Recursively traverse the tree and search for text by tag.
        if node.tag == target_tag and node.text:
            result.append(node.text)
        for child in node.children:
            dfs(child)

    dfs(root)
    return result

if __name__ == "__main__":
    # Example input data (HTML document)
    html_content = """
    <html>
    <head>
        <title>Sample HTML</title>
    </head>
    <body>
        <h1>Heading 1</h1>
        <p>This is a paragraph.</p>
        <div>
            <p>This is another paragraph.</p>
            <p>This is a <b>bold</b> text.</p>
        </div>
    </body>
    </html>
    """

    # Parse HTML and create the DOM tree
    dom_tree = parse_html(html_content)

    # Search for text by tag
    target_tag = 'p'
    text_found = search_text_by_tag(dom_tree, target_tag)

    if text_found:
        print(f"Text found under tag '{target_tag}':")
        for text in text_found:
            print(text)
    else:
        print(f"No text found under tag '{target_tag}'.")
