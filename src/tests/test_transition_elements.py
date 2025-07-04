import pytest
import pathlib

from setup import YAML_LANGUAGE, get_parsed


class TestTransitionElements:

    @pytest.mark.parametrize('src', pathlib.Path("./markdown").glob("**/*.md"), ids=str)
    def test_transition_nodes(self, src):
        (md_parse_tree, md_content, yaml_parse_tree, content) = get_parsed(src)
        if "3-transition-elements" in src.parts:
            typeclass = self.has_valid_class(src, yaml_parse_tree)
            if typeclass in ["transition", "activity"]:
                self.has_correct_id(src, yaml_parse_tree)
            self.is_correct_folder(src, yaml_parse_tree)
            self.is_unique(src, yaml_parse_tree)
            self.title_matches_filename(src, yaml_parse_tree)
            if typeclass == "activity":
                self.activities_have_correct_attributes(src, yaml_parse_tree)

    def get_frontmatter_item(self, parse_tree, key, require_top_level=False):
        if require_top_level:
            pair_query = YAML_LANGUAGE.query("""
               (document (block_node (block_mapping (block_mapping_pair key:(_) @key value:(_) @value))))
            """)
        else:
            pair_query = YAML_LANGUAGE.query("""
               (block_mapping_pair key:(_) @key value:(flow_node) @value)
    """)
        matches = pair_query.matches(parse_tree.root_node)
        for m in matches:
            k = m[1]["key"][0].text
            v = m[1]["value"][0].text
            if k and v and k.decode('utf-8') == key:
                return v.decode('utf-8')

        return None
    
    def has_valid_class(self, src, parse_tree):
        valid_classes = ["transition", "activity", "node"]
        # Get class type from front-matter
        typeclass = self.get_frontmatter_item(parse_tree, "class")

        # assertions
        assert typeclass, f"{src}: Transition node must have a valid class.\n"
        assert typeclass in valid_classes, f"{src}: Transition node has invalid class type: {typeclass}"
        if typeclass == "transition":
            assert "-te-" in src.name, f"{src}: Transition element must have -te- in the filename"
        if typeclass == "activity":
            assert "-a-" in src.name, f"{src}: Activity element must have -a- in the filename"
        if typeclass == "node":
            assert "index.md" in src.name, f"{src}: Transition node must have index.md in the filename"
        return typeclass
            
    def has_correct_id(self, src, parse_tree):
        id = self.get_frontmatter_item(parse_tree, "id")
        assert id, f"{src}: Transition node has no ID"
        sset = src.name.split("-")
        filename_id = sset[-1].replace(".md", "")
        assert id == filename_id, f"{src}: Transition node ID {id} does not match filename {filename_id}"

    def is_correct_folder(self, src, parse_tree):
        sset = src.name.split("-")
        sparent = src.parent.name.split("-")
        if src.name != "index.md":
            assert sset[0] == sparent[0], f"{src}: Transition node coordinate {sset[0]} does not match folder {sparent[0]}"
            
    def is_unique(self, src, parse_tree):
        sset = src.name.split("-")
        for root, dirs, files in src.parent.walk():
            for file in files:
                if file != src.name and file != "index.md":
                    fset = file.split("-")
                    if sset[0] == fset[0] and sset[1] == fset[1]:
                        assert sset[2] != fset[2], f"{src}: Transition node is not unique: {src.name} conflicts with {file}"

    def title_matches_filename(self, src, parse_tree):
        if src.name == "index.md":
            pass
        else:
            sset = src.name.split("-")
            title = self.get_frontmatter_item(parse_tree, "title")
            assert title, f"{src}: Transition node has no title"
            try:
                (lhs,_) = str(title).split(" - ", 1)
            except:
                pytest.fail(f"{src}: Transition node title ({title}) does not match basic format 'A - B'")
            stitle = lhs.split("-")
            assert len(stitle) == 4, f"{src}: Transition node title ({title}) does not match basic format 'T-x-x-x'"
            assert stitle[0] == "T", f"{src}: Transition node title ({title}) does not start with T"
            assert stitle[1].lower() == sset[0], f"{src}: Transition node title ({title}) does not match filename ({sset[0]})"
            assert stitle[2] in ["A","TE"], f"{src}: Transition node title ({title}) does not have A or TE type"
            assert int(stitle[3]) == int(sset[2]), f"{src}: Transition node title index ({title}) does not match filename"
            
    def activities_have_correct_attributes(self, src, parse_tree):
        # Also check that these attributes have values using tree-sitter
        version = self.get_frontmatter_item(parse_tree, "version", True)
        assert version, f"{src}: Activity node has empty value for required attribute: version"

        operation = self.get_frontmatter_item(parse_tree, "operation", True)
        assert operation, f"{src}: Activity node has empty value for required attribute: operation"

        work = self.get_frontmatter_item(parse_tree, "work", True)
        assert work, f"{src}: Activity node has empty value for required attribute: work"


# Test TODO items:
# - Validate a progress value on all files (can we even estimate correctness? e.g. progress 1 but lots of activities is wrong)
