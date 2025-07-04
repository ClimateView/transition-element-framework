import pytest
import difflib

from unittest.mock import MagicMock, patch
import os
import shutil
from types import MethodType
from macros.transitionelement import define_env

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


def setup_transition_element_folder(tmp_path, advanced=False):
    clear_directory(tmp_path)
    test_dir = tmp_path / "markdown" / te_stub
    test_dir.mkdir(parents=True)
    (test_dir / "index.md").write_text("---\ntitle: Transition Elements\nsector: transport\nclass: node\n---\n\nTest index\n")

    transition_dir = test_dir / "1-transport"
    transition_dir.mkdir()
    (transition_dir / "index.md").write_text("---\ntitle: T-1 - Transport\nsector: transport\nclass: node\n---\n\nTest index\n")

    transition2_dir = transition_dir / "1a-mobility"
    transition2_dir.mkdir()
    (transition2_dir / "index.md").write_text("---\ntitle: T-1A - Mobility\nsector: transport\nclass: node\n---\n\nTest index\n")

    transition3_dir = transition2_dir / "1a1-road"
    transition3_dir.mkdir()
    (transition3_dir / "index.md").write_text("---\ntitle: T-1A1 - Road\nsector: transport\nclass: node\n---\n\nTest index\n")

    transition4_dir = transition3_dir / "1a1a-light-duty-vehicles"
    transition4_dir.mkdir()
    (transition4_dir / "index.md").write_text("---\ntitle: T-1A1a - Light Duty Vehicles\nsector: transport\nclass: node\n---\n\nTest index\n")
    (transition4_dir / "1a1a-te-01-test-te-1.md").write_text("---\nid: test-te-1\ntitle: T-1A1a-TE-1 - Test TE 1\nclass: transition\ndescription: Descriptive text\n---\n\nUses test-activity-1")
    (transition4_dir / "1a1a-te-02-test-te-2.md").write_text("---\nid: test-te-2\ntitle: T-1A1a-TE-2 - Test TE 2\nclass: transition\ndescription: Another descriptive text\n---\n\nUses test-activity-2")

    if advanced:
        transition5_dir = transition3_dir / "1a1b-2-3-wheel-vehicles"
        transition5_dir.mkdir()
        (transition5_dir / "index.md").write_text("---\ntitle: T-1A1b - 2/3 Wheel Vehicles\nsector: transport\nclass: node\n---\n\nTest index\n")
        (transition5_dir / "1a1b-te-01-test-te-3.md").write_text("---\nid: test-te-3\ntitle: T-1A1a-TE-1 - Test TE 3\nclass: transition\ndescription: Descriptive text\n---\n\nUses test-activity-3")
        (transition5_dir / "1a1b-te-02-test-te-4.md").write_text("---\nid: test-te-4\ntitle: T-1A1a-TE-2 - Test TE 4\nclass: transition\ndescription: Another descriptive text\n---\n\nUses test-activity-4")
    
    return test_dir


def setup_transition_env():
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


def test_transition_table(tmp_path):
    # Simple two TE test:
    test_dir = setup_transition_element_folder(tmp_path)
    with patch("macros.transitionelement.TE_SEARCH_PATH", str(test_dir)):
        env = setup_transition_env()

        received = env.macros.generate_transition_table()
        expected = f"""??? transport "T-1 - Transport"

    # T-1A - Mobility {{.cv-ml-1}}

    ## T-1A1 - Road {{.cv-ml-2}}

    ### T-1A1a - Light Duty Vehicles {{.cv-ml-3}}

    | &#8288 {{: style="min-width:3rem;"}} | Index {{: width=8%}} | Transition Element {{: width=37%}} | Description {{: width=55%}} | &#8288 {{:style="min-width:2rem;"}} |
    | ---- | ---- | ----  | ---- | ---- |
    | <img src="../../images/icons/test-te-1.svg"> | T-1A1a-TE-1 | [Test TE 1](1-transport/1a-mobility/1a1-road/1a1a-light-duty-vehicles/1a1a-te-01-test-te-1.md) | Descriptive text |  |
    | <img src="../../images/icons/test-te-2.svg"> | T-1A1a-TE-2 | [Test TE 2](1-transport/1a-mobility/1a1-road/1a1a-light-duty-vehicles/1a1a-te-02-test-te-2.md) | Another descriptive text |  |
"""
        assert expected == received
    #  [{rhs}]({filename}.md)

    # Test with advanced setup
    test_dir = setup_transition_element_folder(tmp_path, advanced=True)
    with patch("macros.transitionelement.TE_SEARCH_PATH", str(test_dir)):
        env = setup_transition_env()
        
        received = env.macros.generate_transition_table()
        expected = f"""??? transport "T-1 - Transport"

    # T-1A - Mobility {{.cv-ml-1}}

    ## T-1A1 - Road {{.cv-ml-2}}

    ### T-1A1a - Light Duty Vehicles {{.cv-ml-3}}

    | &#8288 {{: style="min-width:3rem;"}} | Index {{: width=8%}} | Transition Element {{: width=37%}} | Description {{: width=55%}} | &#8288 {{:style="min-width:2rem;"}} |
    | ---- | ---- | ----  | ---- | ---- |
    | <img src="../../images/icons/test-te-1.svg"> | T-1A1a-TE-1 | [Test TE 1](1-transport/1a-mobility/1a1-road/1a1a-light-duty-vehicles/1a1a-te-01-test-te-1.md) | Descriptive text |  |
    | <img src="../../images/icons/test-te-2.svg"> | T-1A1a-TE-2 | [Test TE 2](1-transport/1a-mobility/1a1-road/1a1a-light-duty-vehicles/1a1a-te-02-test-te-2.md) | Another descriptive text |  |

    ### T-1A1b - 2/3 Wheel Vehicles {{.cv-ml-3}}

    | &#8288 {{: style="min-width:3rem;"}} | Index {{: width=8%}} | Transition Element {{: width=37%}} | Description {{: width=55%}} | &#8288 {{:style="min-width:2rem;"}} |
    | ---- | ---- | ----  | ---- | ---- |
    | <img src="../../images/icons/test-te-3.svg"> | T-1A1a-TE-1 | [Test TE 3](1-transport/1a-mobility/1a1-road/1a1b-2-3-wheel-vehicles/1a1b-te-01-test-te-3.md) | Descriptive text |  |
    | <img src="../../images/icons/test-te-4.svg"> | T-1A1a-TE-2 | [Test TE 4](1-transport/1a-mobility/1a1-road/1a1b-2-3-wheel-vehicles/1a1b-te-02-test-te-4.md) | Another descriptive text |  |
"""
        assert expected == received
