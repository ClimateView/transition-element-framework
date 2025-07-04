import pytest
from unittest.mock import MagicMock, patch
import os
import shutil
from types import MethodType
from macros.util import define_env, convert_to_relative_base, clean_markdown_path

ipcc_stub = "2-ipcc-mitigation-options/ipcc-2019-emissions"
te_stub = "3-transition-elements"

# Mock utilities
class MockUtil:
    @staticmethod
    def convert_to_relative_base(url):
        return "../"

    @staticmethod
    def clean_markdown_path(fullpath, rel_base):
        return fullpath.replace("markdown", rel_base)


def setup_util_env():
    # Create a mock env object
    env = MagicMock()

    # Mock the page and its meta
    env.page = MagicMock()
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


def test_convert_to_relative_base():
    # test case when url is a file:
    assert convert_to_relative_base("test.md") == ""
    assert convert_to_relative_base("test/test.md") == "../"
    assert convert_to_relative_base("test/test/test.md") == "../../"
    assert convert_to_relative_base("test/test/test/test.md") == "../../../"
    assert convert_to_relative_base("test/test/test/test/test.md") == "../../../../"
    # test case when url is a folder:
    assert convert_to_relative_base("test", fromfolder=True) == "../"
    assert convert_to_relative_base("test/", fromfolder=True) == "../"
    assert convert_to_relative_base("test/test", fromfolder=True) == "../../"
    assert convert_to_relative_base("test/test/test", fromfolder=True) == "../../../"
    assert convert_to_relative_base("test/test/test/test", fromfolder=True) == "../../../../"
    assert convert_to_relative_base("test/test/test/test/test", fromfolder=True) == "../../../../../"



def test_clean_markdown_path():
    # Should take a path (relative or absolute) and strip everything before "markdown/" and ".md" from the end
    # If path is relative, should turn it into an absolute path using argument base and add .md back to the end

    # Test case where path is relative
    assert clean_markdown_path("anything/markdown/test.md") == "/test.md"
    assert clean_markdown_path("anything/markdown/test.md", "../../") == "../../test.md"

    # Test case where path is absolute
    assert clean_markdown_path("/anything/markdown/test.md") == "/test.md"
    assert clean_markdown_path("/anything/markdown/test.md", "../../") == "../../test.md"

    # Test cases without marker 
    assert clean_markdown_path("this/is/a/path/test.md") == "/this/is/a/path/test.md"
    assert clean_markdown_path("/this/is/a/path/test.md") == "/this/is/a/path/test"

    # Test edge case
    assert clean_markdown_path("a/bcdemarkdown/f/test.md") == "/f/test.md"
    



def test_json_to_yaml():
    env = setup_util_env()

    # Test simple key-value pair
    env.page.meta = { "test": "test" }
    assert env.macros.json_to_yaml() == "test: test\n"

    # Test nested dictionary
    env.page.meta = { "test": { "test": "test" } }
    assert env.macros.json_to_yaml() == "test:\n  test: test\n"

    # Test list
    env.page.meta = { "test": ["test1", "test2"] }
    assert env.macros.json_to_yaml() == "test:\n- test1\n- test2\n"
    
    # Test custom object
    class TestObject:
        def __init__(self, value):
            self.testsubkey = value
    env.page.meta = { "testkey": TestObject("testvalue") }
    assert env.macros.json_to_yaml() == "testkey:\n  testsubkey: testvalue\n"

    # Test unsorted keys
    env.page.meta = { "b": "b", "a": "a" }
    assert env.macros.json_to_yaml() == "b: b\na: a\n"

    # Test unicode
    env.page.meta = { "test": "testé" }
    assert env.macros.json_to_yaml() == "test: testé\n"

    # Test stripping of certain types of metadata keys
    env.page.meta = {
        "title": "title",
        "progress": "progress",
        "class": "class",
        "ipccMitigationMethod": "ipccMitigationMethod",
        "sector": "sector",
        "id": "id",
        "name": "name",
        "version": "version"
    }
    assert env.macros.json_to_yaml() == "version: version\n"
    # Test that it does not destroy original page metadata
    assert env.page.meta["title"] == "title"

    # Test does not strip subkeys of same name
    env.page.meta = {
        "title": "title",
        "version": "version",
        "subkey": {
            "title": "title",
            "version": "version"
        }
    }
    assert env.macros.json_to_yaml() == "version: version\nsubkey:\n  title: title\n  version: version\n"


def clear_directory(directory):
    # Remove and recreate the directory
    shutil.rmtree(directory)
    directory.mkdir(parents=True)

    
def setup_bibliograph_file(tmp_path, bibcontent):
    clear_directory(tmp_path)
    test_dir = tmp_path / "bibliography"
    test_dir.mkdir(parents=True)
    test_file = test_dir / "references.bib"
    test_file.write_text(bibcontent)
    return test_dir

# Temporarily disabled because pkg_resources being deprecated and g enerates a test error on GitHub Actions
#def test_full_bibliography_list(tmp_path):
#    # Test standard generation of bibliography list
#    clear_directory(tmp_path)
#    test_dir = setup_bibliograph_file(tmp_path, """
#@book{test-book-ref,
#    title = {Test Book Title}
#}    
#@report{test-report-ref,
#    title = {Test Report Title}
# }    
#     """)
#     with patch("macros.util.bibfile", str(test_dir / "references.bib")):
#         env = setup_util_env()
#         assert env.macros.full_bibliography_list() == "- Test Book Title [@test-book-ref]\n- Test Report Title [@test-report-ref]\n"
    
#     # Test handling of items without title
#     clear_directory(tmp_path)
#     test_dir = setup_bibliograph_file(tmp_path, """
# @book{test-book-no-title-ref }    
#     """)
#     with patch("macros.util.bibfile", str(test_dir / "references.bib")):
#         env = setup_util_env()
#         assert env.macros.full_bibliography_list() == "- Unknown [@test-book-no-title-ref]\n"
    

#     # Test sorting of bibliography list by title
#     clear_directory(tmp_path)
#     test_dir = setup_bibliograph_file(tmp_path, """
# @book{test-book-ref,
#     title = {B Test Book Title}
# }    
# @report{test-report-ref,
#     title = {A Test Report Title}
# }    
#     """)
#     with patch("macros.util.bibfile", str(test_dir / "references.bib")):
#         env = setup_util_env()
#         assert env.macros.full_bibliography_list() == "- A Test Report Title [@test-report-ref]\n- B Test Book Title [@test-book-ref]\n"
    
        
