import pytest
from unittest.mock import MagicMock, patch
import os
import shutil
from types import MethodType
from macros.mitigation import define_env, get_reference_link, get_te_references, get_te_subector_link

ipcc_stub = "2-ipcc-mitigation-options/ipcc-2019-emissions"
te_stub = "3-transition-elements"
ldv_stub = "1-transport/1a-road/1a1-light-duty-vehicles"
wv_stub = "1-transport/1a-road/1a2-2-3-wheel-vehicles"


# Mock utilities
class MockUtil:
    @staticmethod
    def convert_to_relative_base(url):
        return "../"

    @staticmethod
    def clean_markdown_path(fullpath, rel_base):
        return fullpath.replace("markdown", rel_base)



def clear_directory(directory):
    # Remove and recreate the directory
    shutil.rmtree(directory)
    directory.mkdir(parents=True)

## Test the IPCC emission link macro

def setup_ipcc_emission_link_folder(tmp_path):
    clear_directory(tmp_path)
    test_dir = tmp_path / "markdown" / ipcc_stub
    test_dir.mkdir(parents=True)
    test_file = test_dir / "ipcc-test.md"
    test_file.write_text("---\nid: test-ipcc-ref\ntitle: Test Title\n---")
    test_file = test_dir / "ipcc-test2.md"
    test_file.write_text("---\nid: test-alternative-ipcc-ref\ntitle: Test Alternative Title\n---")
    test_file = test_dir / "ipcc-test-missing-id.md"
    test_file.write_text("---\ntitle: Test Missing ID Title\n---")
    return test_dir


def setup_transition_element_folder(tmp_path):
    clear_directory(tmp_path)
    test_dir = tmp_path / "markdown" / te_stub
    test_dir.mkdir(parents=True)
    test_file = test_dir / "test-te-1.md"
    test_file.write_text("---\nid: test-te-1\ntitle: Test TE 1\n---\n\nUses test-activity-1")
    test_file = test_dir / "test-te-2.md"
    test_file.write_text("---\nid: test-te-2\ntitle: Test TE 2\n---\n\nUses test-activity-2")
    test_file = test_dir / "test-te-3-no-title.md"
    test_file.write_text("---\nid: test-te-2\n---\n\nUses test-activity-3")
    test_file = test_dir / "test-te-4-no-id.md"
    test_file.write_text("---\ntitle: Test TE 4\n---\n\nUses test-activity-4")
    return test_dir



def setup_mitigation_env():
    # Create a mock env object
    env = MagicMock()

    # Mock the page and its meta
    env.page = MagicMock()
    env.page.meta = {"ipccMitigationMethod": None}
    env.page.url = "some/url"

    # Mock macro utility functions
    env.macros = MagicMock()
    def add_macro(func):
        setattr(env.macros, func.__name__, func)
        #env.macros[f.__name__] = f
    env.macro = add_macro

    # Define the macro in the mock environment
    define_env(env)
    return env




def test_get_reference_link():
    env = setup_mitigation_env()
    assert get_reference_link("AR6 10.3.2") == "[AR6 10.3.2](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-10/#10.3.2){target=\"_blank\"}"
    assert get_reference_link("AR6 7.1.1") == "[AR6 7.1.1](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-7/#7.1.1){target=\"_blank\"}"
    # AR6 Table 10.3
    assert get_reference_link("AR6 10.2 Table 10.3") == "[AR6 Table 10.3](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-10/#10.2){target=\"_blank\"}"
    # AR6 Box 10.3
    assert get_reference_link("AR6 Box 10.3") == "[AR6 Box 10.3](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-10/#box-10.3){target=\"_blank\"}"



def test_get_te_subsector(tmp_path):
    def setup_te_folder(tmp_path, empty=True):
        clear_directory(tmp_path)
        # Create some TEs
        te_dir = tmp_path / te_stub
        transport_dir = te_dir / ldv_stub 
        te_dir.mkdir(parents=True)
        transport_dir.mkdir(parents=True)        
        (transport_dir / "1a1-01-test-te-1.md").write_text("---\nid: 1a1-01-test-te-1\ntitle: T-1A1-T-1 - TE1\nipccMitigationMethod: 1a-01-mitigation1\n---\n\nThis is a test TE\n")
        (transport_dir / "index.md").write_text("---\ntitle: T-1A1 - Light Duty Vehicles\nsector: transport\nclass: node\n---\n\nTest index\n")


        return te_dir

    env = setup_mitigation_env()
    te_dir = setup_te_folder(tmp_path, empty=True)

    with patch("macros.mitigation.TE_SEARCH_PATH", str(te_dir)):
        assert get_te_subector_link("") == ("","")
        assert get_te_subector_link(f"{ldv_stub}/1a1-01-test-te-1.md") == ("T-1A1 - Light Duty Vehicles",f"{ldv_stub}/index.md")

    
        
def test_generate_mitigation_index(tmp_path):
    mitigation_frontmatter_template="""---
title: %s
progress: 80
id: %s
class: mitigation
sector: transport
ipccReferences:
%s
---
"""
    def setup_te_folder(tmp_path, empty=False, te_count=0):
        clear_directory(tmp_path)
        # Create some TEs
        te_dir = tmp_path / te_stub
        transport_dir = te_dir / ldv_stub
        transport_wv_dir = te_dir / wv_stub
        te_dir.mkdir(parents=True)
        transport_dir.mkdir(parents=True)
        transport_wv_dir.mkdir(parents=True)

        if te_count > 0:
            (transport_dir / "index.md").write_text("---\ntitle: T-1A1 - Light Duty Vehicles\nsector: transport\nclass: node\n---\n\nTest index\n")
            (transport_dir / "1a1-01-test-te-1.md").write_text("---\nid: 1a1-01-test-te-1\ntitle: T-1A1-T-1 - TE1\nipccMitigationMethod: 1a-01-mitigation1\n---\n\nThis is a test TE\n")
        if te_count > 1:
            (transport_dir / "1a1-02-test-te-2.md").write_text("---\nid: 1a1-02-test-te-2\ntitle: T-1A1-T-2 - TE2\nipccMitigationMethod: 1a-01-mitigation1\n---\n\nThis is a test TE\n")
        if te_count > 2:
            (transport_wv_dir / "index.md").write_text("---\ntitle: T-1A2 - 2/3 Wheel Vehicles\nsector: transport\nclass: node\n---\n\nTest index\n")
            (transport_wv_dir / "1a2-01-test-te-3.md").write_text("---\nid: 1a2-01-test-te-3\ntitle: T-1A2-T-1 - TE3\nipccMitigationMethod: 1a-01-mitigation1\n---\n\nThis is a test TE\n")
        if te_count > 3:
            (transport_wv_dir / "1a2-02-test-te-4.md").write_text("---\nid: 1a2-01-test-te-4\ntitle: T-1A2-T-2 - TE4\nipccMitigationMethod: 1a-01-mitigation1\n---\n\nThis is a test TE\n")

        # Create some mitigation options
        test_dir = tmp_path / "2-ipcc-mitigation-options/1-transport/1a-land-based-transport"
        test_dir.mkdir(parents=True)
        test_file = test_dir / "index.md"
        test_file.write_text("---\ntitle: 1 - Test Mitigation Index\n---\n\n")
        if not empty:
            test_file = test_dir / "1a-01-mitigation1.md"
            test_file.write_text( mitigation_frontmatter_template % ("M-1A-1 - Test Mitigation 1", "1a-01-mitigation1", "- AR6 10.2.1"))
            #test_file = test_dir / "activity-2.md"
            #test_file.write_text("---\ntitle: 1-1 - Test Activity 2\nclass: activity\n---\n\n")
            #test_file = test_dir / "te-2.md"
            #test_file.write_text("---\ntitle: 1-1 - Test TE 2\nclass: transition\n---\n\n")
        return (test_dir,te_dir)

    env = setup_mitigation_env()
    (test_dir,te_dir) = setup_te_folder(tmp_path, empty=True)
    env.page.file = MagicMock()
    env.page.file.src_dir = str(test_dir).replace(str(tmp_path),"")
    env.page.file.src_uri = str(test_dir).replace(str(tmp_path),"")[1:]+"/index.md"

    # test empty index
    assert env.macros.generate_mitigation_index("9", str(tmp_path)) == ""

    table_header = """| Index {: width=5%}   | Title {:width=35%}    | Section(s) {: width=15%}  | Sub-sector(s) {: width=30%}  | TE(s) {: width=15%}   |"""
    
    # test index with one mitigation option and one te reference
    (test_dir,te_dir) = setup_te_folder(tmp_path, empty=False, te_count=1)
    with patch("macros.mitigation.TE_SEARCH_PATH", str(te_dir)):
        assert env.macros.generate_mitigation_index("1a",str(tmp_path)) == f"""{table_header}
| ---- | ---- | ---- | ---- | ---- |
| M-1A-1 {{: rowspan=1 }} | [Test Mitigation 1](1a-01-mitigation1.md) {{: rowspan=1 }} | [AR6 10.2.1](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-10/#10.2.1){{target="_blank"}} {{: rowspan=1 }} | [T-1A1 - Light Duty Vehicles](../../../{te_stub}/{ldv_stub}/index.md) | [T-1A1-T-1](../../../{te_stub}/{ldv_stub}/1a1-01-test-te-1.md "TE1") |
"""

    # test index with two mitigation options and two te references, but single subsector
    (test_dir,te_dir) = setup_te_folder(tmp_path, empty=False, te_count=2)
    with patch("macros.mitigation.TE_SEARCH_PATH", str(te_dir)):
        assert env.macros.generate_mitigation_index("1a",str(tmp_path)) == f"""{table_header}
| ---- | ---- | ---- | ---- | ---- |
| M-1A-1 {{: rowspan=1 }} | [Test Mitigation 1](1a-01-mitigation1.md) {{: rowspan=1 }} | [AR6 10.2.1](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-10/#10.2.1){{target="_blank"}} {{: rowspan=1 }} | [T-1A1 - Light Duty Vehicles](../../../{te_stub}/{ldv_stub}/index.md) | [T-1A1-T-1](../../../{te_stub}/{ldv_stub}/1a1-01-test-te-1.md "TE1") <br> [T-1A1-T-2](../../../{te_stub}/{ldv_stub}/1a1-02-test-te-2.md "TE2") |
"""

    # test index with four mitigation options and four te references in two subsectors
    (test_dir,te_dir) = setup_te_folder(tmp_path, empty=False, te_count=4)
    with patch("macros.mitigation.TE_SEARCH_PATH", str(te_dir)):
        assert env.macros.generate_mitigation_index("1a",str(tmp_path)) == f"""{table_header}
| ---- | ---- | ---- | ---- | ---- |
| M-1A-1 {{: rowspan=2 }} | [Test Mitigation 1](1a-01-mitigation1.md) {{: rowspan=2 }} | [AR6 10.2.1](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-10/#10.2.1){{target="_blank"}} {{: rowspan=2 }} | [T-1A1 - Light Duty Vehicles](../../../{te_stub}/{ldv_stub}/index.md) | [T-1A1-T-1](../../../{te_stub}/{ldv_stub}/1a1-01-test-te-1.md "TE1") <br> [T-1A1-T-2](../../../{te_stub}/{ldv_stub}/1a1-02-test-te-2.md "TE2") |
| [T-1A2 - 2/3 Wheel Vehicles](../../../{te_stub}/{wv_stub}/index.md) | [T-1A2-T-1](../../../{te_stub}/{wv_stub}/1a2-01-test-te-3.md "TE3") <br> [T-1A2-T-2](../../../{te_stub}/{wv_stub}/1a2-02-test-te-4.md "TE4") | &#8288 {{: style="padding:0"}} | &#8288 {{: style="padding:0"}} | &#8288 {{: style="padding:0"}} |
"""

