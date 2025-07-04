# Custom linting for TEF Markdown files
import os
import functools
from tree_sitter import Language, Parser
import tree_sitter_markdown
import tree_sitter_yaml

src_dir = "markdown"

MD_LANGUAGE = Language(tree_sitter_markdown.language())
YAML_LANGUAGE = Language(tree_sitter_yaml.language())
md_parser = Parser(MD_LANGUAGE)
yaml_parser = Parser(YAML_LANGUAGE)

#markdown_mapping = {}
#frontmatter_mapping = {}

def extract_parsed_front_matter(md_parse_tree, content):
    if len(md_parse_tree.root_node.children) > 0:
        first_child = md_parse_tree.root_node.children[0]
        if first_child.type == "minus_metadata":
            yaml_content = content[first_child.start_byte:first_child.end_byte]
            yaml_parse_tree = yaml_parser.parse(yaml_content)
            return (yaml_parse_tree, yaml_content)
    return (None, "")

# for root, dirs, files in os.walk(src_dir):
#     dirs.sort()
#     files.sort()
#     for file in files:
#         if file.endswith(".md"):
#             src = os.path.join(root, file)
#             with open(src, "r") as f:
#                 content = f.read().encode()
#                 md_parse_tree = md_parser.parse(content)
#                 markdown_mapping[src] = (md_parse_tree, content)
#                 (yaml_parse_tree, yaml_content) = extract_parsed_front_matter(md_parse_tree, content)
#                 frontmatter_mapping[src] = (yaml_parse_tree, yaml_content)

@functools.lru_cache(maxsize=None)                
def get_parsed(src):
    with open(src, "r") as f:
        content = f.read().encode()
        md_parse_tree = md_parser.parse(content)
        # markdown_mapping[src] = (md_parse_tree, content)
        (yaml_parse_tree, yaml_content) = extract_parsed_front_matter(md_parse_tree, content)
        return (md_parse_tree, content, yaml_parse_tree, yaml_content)
    
                
# Recursive function to traverse and print the tree
# def print_tree(node, text, depth=0):
#     indent = "  " * depth
#     # Print the current node's type and text range
#     node_text = text[node.start_byte:node.end_byte].decode("utf-8")
#     node_text = node_text[:50].replace("\n", "\\n") + "..."
#     print(f"{indent}{node.type} [{node.start_byte}-{node.end_byte}]: '{node_text}'")
#     # Recursively print children
#     for child in node.children:
#         print_tree(child, text, depth + 1)

