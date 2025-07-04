import pytest
from unittest.mock import MagicMock, patch
import os
import shutil
from types import MethodType
from macros.activity import define_env, get_variables

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



def setup_activity_env():
    # Create a mock env object
    env = MagicMock()

    # Mock the page and its meta
    env.page = MagicMock()
    env.page.meta = {"ipccEmissionSource": None}
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


def test_ipcc_emission_link(tmp_path):
    test_dir = setup_ipcc_emission_link_folder(tmp_path)
    env = setup_activity_env()
    
    with patch("macros.activity.ipcc_search_path", str(test_dir)):    
        # Test that the link is found
        env.page.meta["ipccEmissionSource"] = "test-ipcc-ref"
        assert env.macros.ipcc_emission_link() == f"[Test Title](../{ipcc_stub}/ipcc-test.md)"

        # Test that the link is not found
        env.page.meta["ipccEmissionSource"] = "test-missing-ipcc-ref"
        assert env.macros.ipcc_emission_link() == f"[Unknown](unknown)"

        # Test that the link is found even with whitespace
        env.page.meta["ipccEmissionSource"] = " test-ipcc-ref  "
        assert env.macros.ipcc_emission_link() == f"[Test Title](../{ipcc_stub}/ipcc-test.md)"

        # Test that the link is not found even when target file is missing id
        #   (test of fallback to filename)
        env.page.meta["ipccEmissionSource"] = "ipcc-test-missing-id"
        assert env.macros.ipcc_emission_link() == f"[Test Missing ID Title](../{ipcc_stub}/ipcc-test-missing-id.md)"


def test_transition_element_list(tmp_path):
    test_dir = setup_transition_element_folder(tmp_path)
    env = setup_activity_env()
    with patch("macros.activity.transition_elements_path", str(test_dir)):
        # Test that the list is generated correctly
        env.page.meta["id"] = "test-activity-1"
        assert env.macros.transition_element_list() == "\n- [Test TE 1](../3-transition-elements/test-te-1.md)"

        # Test that the list is generated correctly for a different activity
        env.page.meta["id"] = "test-activity-2"
        assert env.macros.transition_element_list() == "\n- [Test TE 2](../3-transition-elements/test-te-2.md)"

        # Test an activity that does not have any transition elements
        env.page.meta["id"] = "test-activity-0"
        assert env.macros.transition_element_list() == ""

        # Test handling of an activity page that has no id - should return an empty list
        env.page.meta["id"] = None
        assert env.macros.transition_element_list() == ""

        # Test that the link gets the correct relative base
        env.page.meta["id"] = "test-activity-1"
        env.page.url = "3-transition-elements/url/with/many/subfolders/"
        assert env.macros.transition_element_list() == "\n- [Test TE 1](../../../../3-transition-elements/test-te-1.md)"

        env.page.meta["id"] = "test-activity-1"
        env.page.url = ""
        assert env.macros.transition_element_list() == "\n- [Test TE 1](3-transition-elements/test-te-1.md)"

        env.page.url = "some/url"

        # Test handling of TE with no title
        env.page.meta["id"] = "test-activity-3"
        assert env.macros.transition_element_list() == "\n- [Unknown](../3-transition-elements/test-te-3-no-title.md)"

        # Test handling of TE with no title
        env.page.meta["id"] = "test-activity-4"
        assert env.macros.transition_element_list() == "\n- [Test TE 4](../3-transition-elements/test-te-4-no-id.md)"
        


def test_get_variables(tmp_path):
    # Test that the function returns the correct variables with a simple dictionary
    data = {"variable": "test", "resourceProportion": "test2"}
    assert get_variables(data) == ["test", "test2"]

    # Test that the function returns the correct variables with a nested dictionary
    data = {"variable": "test", "resourceProportion": "test2", "nested": {"variable": "test3"}}
    assert get_variables(data) == ["test", "test2", "test3"]

    # Test that the function returns the correct variables with a list
    data = [{"variable": "test", "resourceProportion": "test2"}, {"variable": "test3"}]
    assert get_variables(data) == ["test", "test2", "test3"]
    
    # Test that the function returns the correct variables with a nested list
    data = [{"variable": "test", "resourceProportion": "test2"}, {"variable": "test3", "nested": [{"variable": "test4"}]}]
    assert get_variables(data) == ["test", "test2", "test3", "test4"]

    # Test that the function returns the correct variables with lists inside dictionaries
    data = {"variable": "test", "resourceProportion": "test2", "nested": [{"variable": "test3"}]}
    assert get_variables(data) == ["test", "test2", "test3"]

    # Test that the function returns the correct variables with dictionaries inside lists inside dictionaries
    data = [{"variable": "test", "resourceProportion": "test2", "nested": [{"list": [{ "variable": "test3"}]}]}]
    assert get_variables(data) == ["test", "test2", "test3"]


def test_generate_parameter_table(tmp_path):
    def setup_parameter_folder(tmp_path):
        clear_directory(tmp_path)
        test_dir = tmp_path / "parameters"
        test_dir.mkdir(parents=True)
        test_file = test_dir / "test-param-1.md"
        test_file.write_text("---\nid: test-param-1\ntitle: Test Param 1\n---\n\n")
        test_file = test_dir / "test-param-2.md"
        test_file.write_text("---\nid: test-param-2\ntitle: Test Param 2\nunit: test-unit\n---\n\n")
        test_file = test_dir / "test-param-3.md"
        test_file.write_text("---\nid: test-param-3\n---\n\n")
        return test_dir

    env = setup_activity_env()

    # Test that the function returns the correct table with simple mocked variable list and no matching files
    env.page.meta = {"variables": ["test", "test2"]}
    assert env.macros.generate_parameter_table() == "| Parameter | Unit | Description |\n| --- |  --- | --- |\n| test | unknown | unknown |\n| test2 | unknown | unknown |\n"

    # Test that the function returns the correct table with simple mocked variable list and matching files
    test_dir = setup_parameter_folder(tmp_path)
    with patch("macros.activity.parameter_path", str(test_dir)):
        env.page.meta = {"variables": ["test-param-2"]}
        dir = str(test_dir).lower()
        assert env.macros.generate_parameter_table() == f"| Parameter | Unit | Description |\n| --- |  --- | --- |\n| [test-param-2]({dir}/test-param-2) | test-unit | Test Param 2 |\n"
    

def test_generate_work_link(tmp_path):
    def setup_work_folder(tmp_path):
        clear_directory(tmp_path)
        test_dir = tmp_path / "work"
        test_dir.mkdir(parents=True)
        test_file = test_dir / "work-types.md"
        test_file.write_text("""
---
title: Work Types
---

# Group 1
Lipsum ipsum.

## Subgroup 1.1
Lipsum ipsum.

## Subgroup 1.2
Lipsum ipsum.

# Group 2
Lipsum ipsum.

## Subgroup 2.1
Lipsum ipsum.

## Subgroup 2.2
Lipsum ipsum.
""")
        return test_dir

    env = setup_activity_env()
    test_dir = setup_work_folder(tmp_path)
    with patch("macros.activity.workfile_path", str(test_dir / "work-types.md")):
        # Test unknown work type
        env.page.meta = {"work": [{"name": "test-work"}]}
        assert env.macros.generate_work_link() == f"Unknown work type"

        # Test known work type 
        env.page.meta = {"work": [{"name": "subgroup-1-2"}]}
        assert env.macros.generate_work_link() == f"[Subgroup 1.2](../5-resources/5-about/work-types.md#subgroup-1-2)"
        

        
def test_generate_activity_index(tmp_path):
    def setup_te_folder(tmp_path, empty=True):
        clear_directory(tmp_path)
        test_dir = tmp_path / "transition-elemements/1-transport/1a-road"
        test_dir.mkdir(parents=True)
        test_file = test_dir / "index.md"
        test_file.write_text("---\ntitle: 1 - Test Index\n---\n\n")
        test_file = test_dir / "activity-1.md"
        test_file.write_text("---\ntitle: 2-1 - Test Activity 1\n---\n\n")
        if not empty:
            test_file = test_dir / "activity-2.md"
            test_file.write_text("---\ntitle: 1-1 - Test Activity 2\nclass: activity\n---\n\n")
            test_file = test_dir / "te-2.md"
            test_file.write_text("---\ntitle: 1-1 - Test TE 2\nclass: transition\n---\n\n")
        return test_dir

    env = setup_activity_env()
    test_dir = setup_te_folder(tmp_path)
    env.page.file = MagicMock()
    env.page.file.src_dir = str(test_dir)
    env.page.file.src_uri = "index.md"

    # test empty index
    assert env.macros.generate_activity_index("9") == ""

    # test index with one activity
    test_dir = setup_te_folder(tmp_path, empty=False)
    assert env.macros.generate_activity_index("1") == "\n\n| &#8288 {:style=\"min-width:2rem;\"} | &#8288 {:style=\"min-width:3rem;\"} | Index {: width=10%} | Activity {: width=50%} | &#8288 {: width=40%} | \n | ---- | ---- | ---- | ---- | ---- |\n|  |  | 1-1 | [Test Activity 2](activity-2.md) |  | \n"

