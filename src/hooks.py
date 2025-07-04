from typing import List, Union

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Link, Navigation, Page, Section
from mkdocs.structure import StructureItem
import re


class SeparatorItem(StructureItem):
    def __init__(self, title):
        self.title = title

    is_separator: bool = True
    """Indicates that the navigation object is a separator object."""

    
# The following preprocessor hooks to on_nav() in MkDocs and retitles
# any index.md files to use the title contained in the metadata in the
# markdown file.
def generate_renamed_section_items(
    items: List[Union[Page, Section, Link]], *, config: MkDocsConfig
) -> List[Union[Page, Section, Link]]:
    new_items: List[Union[Page, Section, Link]] = []
    last_item = "unknown"
    for item in items:
        if isinstance(item, Section):
            new_title = item.title
            new_children = generate_renamed_section_items(item.children, config=config)
            try:
                first_child = new_children[0]
            except:
                first_child = None
            if isinstance(first_child, Page):
                if first_child.file.src_path.endswith("index.md"):
                    # Read the source so that the title is parsed and available
                    first_child.read_source(config=config)
                    new_title = first_child.title or new_title
            item.title = new_title
            item.children = new_children
            new_items.append(item)
        else:
            if "-a-" in item.file.src_path:
                if last_item != "activity":
                    new_items.append(SeparatorItem("Activities"))
                    last_item = "activity"
            elif "-te-" in item.file.src_path:
                if last_item != "transition":
                    new_items.append(SeparatorItem("Transition Elements"))
                    last_item = "transition"
            else:
                last_item = "unknown"
            if "/parameters/" in item.file.src_path and not "index"in item.file.src_path:
                pass # skip menu items for parameters as there are too many items
            else:
                new_items.append(item)
    return new_items

def on_nav(nav: Navigation, *, config: MkDocsConfig, files: Files, **kwargs):
    new_items = generate_renamed_section_items(nav.items, config=config)
    return Navigation(items=new_items, pages=nav.pages)




# This template filter will strip the "coordinate" portion of any page
# Thus e.g. "M-1A-1 - Changes in Urban Form" would become "Changes in Urban Form"
# This filter is used for making the navigation items more compact.
def strip_coordinate(value):
    if value:
        s = value.split(" - ")
        if len(s) == 2: # The nav value is part of the hierarchy coordinate system
            lhs = s[0]
            rhs = s[1]
            s = lhs.split("-")
            if len(s) == 4: # TE or Activity
                return rhs # s[3] + " - " + rhs
            elif len(s) == 3: # Mitigation method
                return rhs # s[3] + " - " + rhs                
            elif len(s) == 2: # Hierarchy node
                return rhs # s[1] + " - " + rhs
        
    return value

def on_env(env, config, files, **kwargs):
    env.filters['strip_coordinate'] = strip_coordinate
    return env

