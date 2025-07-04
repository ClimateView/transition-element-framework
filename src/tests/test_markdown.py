import pytest
import pathlib

from setup import YAML_LANGUAGE, get_parsed


class TestMarkdown:

    @pytest.mark.parametrize('src', pathlib.Path("./markdown").glob("**/*.md"), ids=str)
    def test_correct_markdown(self, src):
        """ TEF01: Markdown file should not be empty """
        (md_parse_tree, md_content, yaml_parse_tree, content) = get_parsed(src)

        self.check_not_empty(md_parse_tree)
        self.check_has_valid_front_matter(md_parse_tree, yaml_parse_tree)

    def check_not_empty(self, md_parse_tree):
        assert len(md_parse_tree.root_node.children) > 0, "Markdown is empty"

    def check_has_valid_front_matter(self, md_parse_tree, yaml_parse_tree):
        first_child = md_parse_tree.root_node.children[0]
        assert first_child.type == "minus_metadata", f"Markdown does not contain YAML front-matter"
        assert not yaml_parse_tree.root_node.has_error, f"Markdown contains invalid YAML front-matter"



