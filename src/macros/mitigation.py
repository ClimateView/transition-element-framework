import os
import frontmatter
# import OrderedDict
from collections import OrderedDict

from . import terminology
from . import util



def get_reference_link(ref):
    """
    Generate a formatted reference link based on the reference string.
    @param ref: Reference string formatted with an identifier (e.g. "AR6", "AR5") followed by details.
    @return: A markdown-formatted link if valid, or an error message.
    """

    # Return early if the reference is an empty string
    if ref == "":
        return ""
    
    # Split the reference into identifier and details only once.
    try:
        identifier, details = ref.split(" ", 1)
    except ValueError:
        return "Invalid reference"
    
    if identifier == "AR6":
        if "Table" in details:
            # Split once using a maximum split to avoid repeating the same split.
            table_parts = details.split(" Table ", 1)
            section = table_parts[0]
            chapter = section.split(".")[0]
            title = f"{identifier} Table {table_parts[1]}"
        elif "Box" in details:
            detail_parts = details.split(" ", 2)
            if len(detail_parts) >= 2:
                section = detail_parts[1]
                chapter = section.split(".")[0]
                # Prepend 'box-' to the section identifier
                section = "box-" + section
                title = ref
            else:
                return "Invalid reference"
        else:
            chapter = details.split(".")[0]
            section = details
            title = ref
        return f"[{title}](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-{chapter}/#{section}){{target=\"_blank\"}}"
    elif identifier == "AR5":
        return ref
    else:
        return "Invalid reference"


TE_SEARCH_PATH = f"{util.markdown_base}/3-transition-elements"
def get_te_references(mitigation_id):
    """
    Return a sorted list of relative markdown file paths from TE_SEARCH_PATH whose frontmatter's
    "ipccMitigationMethod" matches the provided mitigation_id.
    @param mitigation_id: A string identifier for the mitigation.
    @return: A list of relative file paths.
    """
    # Get the TE references for the mitigation
    references = []
    for root, dirs, files in os.walk(TE_SEARCH_PATH):
        dirs.sort()
        files.sort()
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r") as f:
                    data = frontmatter.load(f)
                    ipcc_link = data.get("ipccMitigationMethod", "")
                    if ipcc_link == mitigation_id:
                        relative_dir = os.path.relpath(root, TE_SEARCH_PATH)
                        link = os.path.join(relative_dir, file)
                        references.append(link)
    return references

def group_te_references(references):
    """
    Group transition element references by their parent directory.

    Given a list of file path strings, this function groups them by the directory 
    path (i.e. the portion of the path before the final file name). The function 
    returns an OrderedDict where each key is a directory path and its value is a list 
    of references (file paths) contained within that directory.

    Parameters:
        references (list of str): List of relative file paths for transition elements.

    Returns:
        OrderedDict: An ordered mapping of parent directory paths to lists of references.
    """
    groups = OrderedDict()
    for ref in references:
        group = "/".join(ref.split("/")[:-1])
        groups.setdefault(group, []).append(ref)
    return groups


def get_te_subector_link(te_path):
    """
    Retrieve the title and index link for a transition element's subsector.

    Given a relative file path to a transition element markdown file,
    this function locates the corresponding index file in its parent directory,
    extracts the title from the file's frontmatter, and returns a tuple containing
    the title and the relative path to that index.

    Parameters:
        te_path (str): Relative path to a transition element markdown file.

    Returns:
        tuple: A tuple (title, index_link). If te_path is empty, returns ("", "").
    """
    if not te_path:
        return ("", "")
    paths = te_path.split("/")
    index_path = "/".join(paths[:-1])
    index_file = os.path.join(TE_SEARCH_PATH, index_path, "index.md")
    with open(index_file, "r") as f:
        data = frontmatter.load(f)
    title = data.get("title", "Unknown")
    return (title, f"{index_path}/index.md")


def get_te_link(te_path):
    """
    Retrieve the title and link for a transition element markdown file.

    Constructs the absolute file path from the given relative path,
    reads the file's frontmatter to extract the title, and returns the title
    along with the original relative path.

    Parameters:
        te_path (str): Relative file path to a transition element markdown file.

    Returns:
        tuple: (title, te_path), where title is extracted from the file's frontmatter 
               or defaults to "Unknown" if not provided.
    """
    full_path = os.path.join(TE_SEARCH_PATH, te_path)
    with open(full_path, "r") as f:
        data = frontmatter.load(f)
    title = data.get("title", "Unknown")
    return (title, te_path)


def define_env(env):

    @env.macro
    def generate_mitigation_te_list(coordinate="", base_folder="markdown"):
        """
        Generate a markdown list for Transition Elements related to a mitigation item.
        Parameters:
          coordinate (str): A coordinate substring for filtering titles.
          base_folder (str): The base folder (default "markdown") containing content.
        Returns:
          str: A markdown formatted list with links.
        """
        current_file = env.page.file
        src = os.path.join(base_folder, current_file.src_uri)
        mitigation_id = env.page.meta.get("id", "")
        te_references = get_te_references(mitigation_id)
        te_grouped_references = group_te_references(te_references)
        list = ""
        # No transition element groups found; add a simple row for this file.
        if len(te_grouped_references) == 0:
            list = "This mitigation option is not currently modelled with any Transition Elements.\n"
        else:
            if len(te_references) > 1:
                list += "This mitigation option has been modelled with the following Transition Elements:\n\n"
            else:
                list += "This mitigation option has been modelled with the following Transition Element:\n\n"
                
            # Prepare a base prefix for transition element links.
            prefix = util.convert_to_relative_base(current_file.src_uri) + "3-transition-elements/"
            # Loop through each sub-sector group with its associated TE references.
            for i, (group, group_refs) in enumerate(te_grouped_references.items()):
                # Get title and path for the sub-sector from the first reference in the group.
                (ss_lhs, ss_rhs) = get_te_subector_link(group_refs[0])
                ss_rhs_full = prefix + ss_rhs
                list += f"- {ss_lhs}\n"
                # Build the TE links for the current group.
                te_links = []
                for te in group_refs:
                    (te_title_full, te_path) = get_te_link(te)
                    # Safely split the TE title into label and detailed title.
                    te_parts = te_title_full.split(" - ", 1)
                    if len(te_parts) == 2:
                        te_lhs, te_title = te_parts
                    else:
                        te_lhs = te_title_full
                        te_title = "Unknown"
                    te_path_full = prefix + te_path
                    list += f"    - [{te_title_full}]({te_path_full} \"{te_title}\")\n"

        
        return list
    

    
    @env.macro
    def generate_mitigation_index(coordinate="", base_folder="markdown"):
        """
        Generate a markdown index table for mitigation items.
        Parameters:
          coordinate (str): A coordinate substring for filtering titles.
          base_folder (str): The base folder (default "markdown") containing content.
        Returns:
          str: A markdown formatted table with links and metadata.
        """
        current_file = env.page.file
        src = os.path.join(base_folder, current_file.src_uri)
        src = src.replace("index.md", "")
        index = ""
        for root, dirs, files in os.walk(src):
            # print(files)  # Debug line removed.
            if root != src:
                # Get the relative folder path from the source directory
                owner = os.path.relpath(root, src)
                # Count the number of subdirectories to determine header depth
                depth = len(owner.split(os.sep))
                # Determine markdown header level based on directory depth
                header_prefix = "#" * depth
                # Build full path to the directory's index file and load its title from frontmatter
                index_path = os.path.join(root, "index.md")
                if os.path.exists(index_path):
                    with open(index_path, "r") as f:
                        index_data = frontmatter.load(f)
                        title = index_data.get("title", "Unknown")
                else:
                    title = "Unknown"
                # Only include headings for directories with a depth less than 3
                if depth < 3:
                    index += f"\n\n{header_prefix} [{title}]({owner}/index.md)\n\n"
            else:
                depth = 0
                owner = ""
            dirs.sort()
            files.sort()
            started = False
            if depth < 1:
                for file in files:
                    if file.endswith(".md") and file != "index.md":
                        with open(os.path.join(root, file), "r") as f:
                            filename = file.replace(".md", "")
                            data = frontmatter.load(f)
                            title = data.get("title", "Unknown")
                            parts = title.split(" - ", 1)
                            if len(parts) == 2:
                                lhs, rhs = parts
                            else:
                                lhs = title
                                rhs = "Unknown"                            
                            id = data.get("id", "Unknown")
                            classtype = data.get("class", "Unknown")
                            references = data.get("ipccReferences", [])
                            if coordinate+"-" in title.lower() and classtype == "mitigation":
                                if not started:
                                    index += """| Index {: width=5%}   | Title {:width=35%}    | Section(s) {: width=15%}  | Sub-sector(s) {: width=30%}  | TE(s) {: width=15%}   |
| ---- | ---- | ---- | ---- | ---- |
"""
                                    started = True
                                reference_links = "  <br>".join([get_reference_link(ref) for ref in references])
                                te_references = get_te_references(id)
                                te_grouped_references = group_te_references(te_references)
                                # No transition element groups found; add a simple row for this file.
                                if len(te_grouped_references) == 0:
                                    index += f"| {lhs} | [{rhs}]({filename}.md) | {reference_links} |  |  |\n"
                                else:
                                    # Prepare a base prefix for transition element links.
                                    prefix = util.convert_to_relative_base(current_file.src_uri) + "3-transition-elements/"
                                    # Determine how many groups to calculate the rowspan.
                                    rowspan = len(te_grouped_references)
                                    # Loop through each sub-sector group with its associated TE references.
                                    for i, (group, group_refs) in enumerate(te_grouped_references.items()):
                                        # Get title and path for the sub-sector from the first reference in the group.
                                        (ss_lhs, ss_rhs) = get_te_subector_link(group_refs[0])
                                        ss_rhs_full = prefix + ss_rhs
                                            
                                        # Build the TE links for the current group.
                                        te_links = []
                                        for te in group_refs:
                                            (te_title_full, te_path) = get_te_link(te)
                                            # Safely split the TE title into label and detailed title.
                                            te_parts = te_title_full.split(" - ", 1)
                                            if len(te_parts) == 2:
                                                te_lhs, te_title = te_parts
                                            else:
                                                te_lhs = te_title_full
                                                te_title = "Unknown"
                                            te_path_full = prefix + te_path
                                            te_links.append(f"[{te_lhs}]({te_path_full} \"{te_title}\")")
                                            
                                        # Join all TE links with a line break.
                                        telinks = " <br> ".join(te_links)
                                            
                                        # On the first group row, include mitigation-level data along with the sub-sector.
                                        if i == 0:
                                            index += f"| {lhs} {{: rowspan={rowspan} }} | [{rhs}]({filename}.md) {{: rowspan={rowspan} }} | {reference_links} {{: rowspan={rowspan} }} | [{ss_lhs}]({ss_rhs_full}) | {telinks} |\n"
                                        else:
                                            # For subsequent rows, show only sub-sector and TE link info.
                                            index += f"| [{ss_lhs}]({ss_rhs_full}) | {telinks} | &#8288 {{: style=\"padding:0\"}} | &#8288 {{: style=\"padding:0\"}} | &#8288 {{: style=\"padding:0\"}} |\n"

        
        return index
    




    @env.macro
    def generate_mitigation_node_headings(coordinate="", base_folder="markdown"):
        """
        Generate a list of markdown headings for childrennodes.
        Parameters:
          coordinate (str): A coordinate substring for filtering titles.
          base_folder (str): The base folder (default "markdown") containing content.
        Returns:
          str: A markdown formatted set of linked headings.
        """
        current_file = env.page.file
        src = os.path.join(base_folder, current_file.src_uri)
        src = src.replace("index.md", "")
        index = ""
        for root, dirs, files in os.walk(src):
            # print(files)  # Debug line removed.
            if root != src:
                # Get the relative folder path from the source directory
                owner = os.path.relpath(root, src)
                # Count the number of subdirectories to determine header depth
                depth = len(owner.split(os.sep)) + 1
                # Determine markdown header level based on directory depth
                header_prefix = "#" * depth
                # Build full path to the directory's index file and load its title from frontmatter
                index_path = os.path.join(root, "index.md")
                if os.path.exists(index_path):
                    with open(index_path, "r") as f:
                        index_data = frontmatter.load(f)
                        title = index_data.get("title", "Unknown")
                else:
                    title = "Unknown"
                # Only include headings for directories with a depth less than 3
                if depth < 3:
                    index += f"\n\n{header_prefix} [{title}]({owner}/index.md)\n\n"
            else:
                depth = 0
                owner = ""
            dirs.sort()
            files.sort()
            started = False
        
        return index
    
    
