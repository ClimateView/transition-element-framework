import pytest
import pathlib

from setup import YAML_LANGUAGE, get_parsed


class TestMitigationMethods:

    @pytest.mark.parametrize('src',
                             pathlib.Path("../markdown/2-ipcc-mitigation-options").glob("**/*.md"), ids=str)
    def test_mitigation_nodes(self, src):
        (md_parse_tree, md_content, yaml_parse_tree, content) = get_parsed(src)
        if "ipcc-2019-emissions" not in src.parts:
            typeclass = self.has_valid_class(src, yaml_parse_tree)
            if typeclass in ["mitigation"]:
                self.has_correct_id(src, yaml_parse_tree)
            self.is_correct_folder(src, yaml_parse_tree)
            self.is_unique(src, yaml_parse_tree)
            self.title_matches_filename(src, yaml_parse_tree)
            if typeclass == "mitigation":
                self.mitigation_methods_have_ipcc_reference(src, yaml_parse_tree)

    def get_frontmatter_item(self, parse_tree, key):
        first_child = parse_tree.root_node.children[1]
        # Test for simple key value pairs:
        pair_query = YAML_LANGUAGE.query("""
            (block_mapping_pair key:(flow_node) @key value:(flow_node) @value)
        """)
        matches = pair_query.matches(parse_tree.root_node)
        for m in matches:
            k = m[1]["key"][0].text
            v = m[1]["value"][0].text
            if k and v and k.decode('utf-8')==key:
                return v.decode('utf-8')
        # Then test for key value pairs where the value is a list:
        pair_query = YAML_LANGUAGE.query("""
            (block_mapping_pair
                key:(flow_node) @key
                value:(block_node
                    (block_sequence
        (block_sequence_item (flow_node) @value)
                    )
                ) 
            )
""")
        matches = pair_query.matches(parse_tree.root_node)
        for m in matches:
            k = m[1]["key"][0].text
            v_nodes = m[1].get("value", [])
            if k:
                k = k.decode("utf-8")
                if k == key:
                    if v_nodes:
                        v = [node.text.decode("utf-8") for node in v_nodes]
                        return v  # Returns a list if multiple values exist
                    return None  # Or an empty list if you prefer

    
    def has_valid_class(self, src, parse_tree):
        valid_classes = ["mitigation", "node"]
        # Get class type from front-matter
        typeclass = self.get_frontmatter_item(parse_tree, "class")

        # assertions
        assert typeclass, f"{src}:1 Mitigation node must have a class definition.\n"
        assert typeclass in valid_classes, f"{src}:1 Mitigation object has invalid class type: {typeclass}"
        if typeclass == "node":
            assert "index.md" in src.name, f"{src}:1 Mitigation node must have index.md in the filename"
        return typeclass
            
    def has_correct_id(self, src, parse_tree):
        id = self.get_frontmatter_item(parse_tree, "id")
        assert id, f"{src}: Mitigation node has no ID"
        filename_id = src.name.replace(".md", "")
        assert id == filename_id, f"{src}:1 Mitigation node ID {id} does not match filename {filename_id}"

    def is_correct_folder(self, src, parse_tree):
        sset = src.name.split("-")
        sparent = src.parent.name.split("-")
        if src.name != "index.md":
            assert sset[0] == sparent[0], f"{src}:1 Mitigation node coordinate {sset[0]} does not match folder {sparent[0]}"
            
    def is_unique(self, src, parse_tree):
        sset = src.name.split("-")
        for root, dirs, files in src.parent.walk():
            for file in files:
                if file != src.name and file != "index.md":
                    fset = file.split("-")
                    if sset[0] == fset[0] and sset[1] == fset[1]:
                        assert sset[2] != fset[2], f"{src}:1 Mitigation node is not unique: {src.name} conflicts with {file}"

    def title_matches_filename(self, src, parse_tree):
        if src.name == "index.md":
            pass
        else:
            sset = src.name.split("-")
            title = self.get_frontmatter_item(parse_tree, "title")
            assert title, f"{src}:1 Mitigation node has no title"
            try:
                (lhs,_) = str(title).split(" - ", 1)
            except:
                pytest.fail(f"{src}:1 Mitigation node title ({title}) does not match basic format 'A - B'")
            stitle = lhs.split("-")
            assert len(stitle) == 3, f"{src}:1 Mitigation node title ({title}) does not match basic format 'M-x-x'"
            assert stitle[0] == "M", f"{src}:1 Mitigation node title ({title}) does not start with M"
            assert stitle[1].lower() == sset[0], f"{src}:1 Mitigation node title ({title}) does not match filename ({sset[0]})"
            assert int(stitle[2]) == int(sset[1]), f"{src}:1 Transition node title index ({title}) does not match filename"
            
    def mitigation_methods_have_ipcc_reference(self, src, parse_tree):
        ipccref = self.get_frontmatter_item(parse_tree, "ipccReferences")
        assert ipccref, f"{src}:1 Mitigation node has no ipccReferences"
        assert len(ipccref) > 0, f"{src}:1 Mitigation node has no ipccReferences"
        for ref in ipccref:
            assert ref, f"{src}:1 Mitigation node has an empty ipccReference"
            assert ref.startswith("AR6") or ref.startswith("AR5"), f"{src}:1 Mitigation node has an invalid ipccReference: {ref}"
        


# Test TODO items:
# - Validate a progress value on all files (can we even estimate correctness? e.g. progress 1 but lots of activities is wrong)
