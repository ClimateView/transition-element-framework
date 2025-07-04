import os
import frontmatter
import re

from . import util
from . import drawio


ipcc_search_path = f"{util.markdown_base}/2-ipcc-mitigation-options/ipcc-2019-emissions"
transition_elements_path = f"{util.markdown_base}/3-transition-elements"
parameter_path = f"{util.markdown_base}/5-resources/1-data/definitions/parameters"
workfile_path = f"{util.markdown_base}/5-resources/5-about/work-types.md"

def get_variables(data):
    variable_set = ["variable", "resourceProportion"]
    val = []
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "variables":
                val.extend(value)
            elif key in variable_set:
                val.append(value)
            else:
                val.extend(get_variables(value))
    elif isinstance(data, list):
        for item in data:
            val.extend(get_variables(item))
    return val



def define_env(env):
    "Hook function"

    @env.macro
    def ipcc_emission_link():
        global ipcc_search_path
        ipcc_code = env.page.meta.get("ipccEmissionSource", None)
        if ipcc_code is None:
            return "*TBD*"
        title = "Unknown"
        ipcc_path = "unknown"
        rel_base = util.convert_to_relative_base(env.page.url)
        for root, dirs, files in os.walk(ipcc_search_path):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r") as f:
                        data = frontmatter.load(f)
                        if "id" in data:
                            id = data["id"].strip()
                        else:
                            id = file.replace(".md", "")
                        if id == ipcc_code.strip():
                            title = data["title"]
                            fullpath = os.path.join(root, file)
                            ipcc_path = util.clean_markdown_path(fullpath, rel_base)
        return f"[{title}]({ipcc_path})"


    @env.macro
    def transition_element_list():
        global transition_elements_path
        # walk the directory tree
        id = env.page.meta.get("id", None)
        if id is None:
            return ""
        list = []
        rel_base = util.convert_to_relative_base(env.page.url)
        for root, dirs, files in os.walk(transition_elements_path):
            for file in files:
                if "activity-hierarchy" not in root and file != "index.md" \
                   and "-te-" in file and file.endswith(".md"):
                    with open(os.path.join(root, file), "r") as f:
                        data = f.read()
                        if id in data:
                            # TODO: should really check that id is part of a TE element in the metadata, not just string match
                            list.append(os.path.join(root, file))
        markdown = ""
        list.sort()
        for file in list:
            with open(file, "r") as f:
                data = frontmatter.load(f)
                title = data.get("title", "Unknown")
                filename = util.clean_markdown_path(file, rel_base)
                markdown += f"\n- [{title}]({filename})"
        return markdown

    @env.macro
    def generate_parameter_table():
        table = "| Parameter | Unit | Description |\n"
        table += "| --- |  --- | --- |\n"
        variables = set(get_variables(env.page.meta))
        # convert from set to list:
        variables = list(variables)
        variables.sort()
        rel_base = util.convert_to_relative_base(env.page.url)
        #         if "cost" in f or "price" in f or "purchase" in f:
        for key in variables:
            filename = f"{parameter_path}/{key}.md"
            try:
                with open(filename, "r") as f:
                    fm = frontmatter.load(f)
                    unit = fm.get("unit", "unknown")
                    description = fm.get("title", "unknown")
                plink = util.clean_markdown_path(filename, rel_base).lower()
                table += f"| [{key}]({plink}) | {unit} | {description} |\n"
            except FileNotFoundError:
                unit = "unknown"
                description = "unknown"
                table += f"| {key} | {unit} | {description} |\n"                
        return table

    @env.macro
    def generate_work_link():
        global workfile_path
        def find_heading_anchor(markdown_file, search_identifier):
            def to_snake_case(text):
                """Convert a heading to snake-case."""
                return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('_')

            with open(markdown_file, "r", encoding="utf-8") as file:
                for line in file:
                    # Match level 2 headings (lines starting with '## ')
                    match = re.match(r'^##\s+(.*)', line)
                    if match:
                        heading = match.group(1).strip()
                        identifier = to_snake_case(heading)
                        if identifier == search_identifier:
                            return (heading, identifier)

            return (None, None)
        work = env.page.meta["work"][0]["name"]
        (title, id) = find_heading_anchor(workfile_path, work)
        rel_base = util.convert_to_relative_base(env.page.url)
        if title is not None:
            return f"[{title}]({rel_base}5-resources/5-about/work-types.md#{id})"
        else:
            return "Unknown work type"

    @env.macro
    def activity_model():
        return drawio.generate(env.page.meta)

    @env.macro
    def activity_sustainability():
        text = "# Sustainability\n\n"
        category = env.page.meta.get("sustainability", "Unknown")
        rel_base = util.convert_to_relative_base(env.page.url)

        if category == "green":
            return f"""## Sustainability Category: Green

![Green]({rel_base}images/traffic_green.svg){{ align=left width="50" }}

This activity substantially contributes to climate change mitigation through significant greenhouse gas reductions, carbon sequestration, or enabling the transition to net-zero emissions. This activity aligns with science-based pathways to limit global warming and should be prioritized for investment and expansion.
          """
        elif category == "amber":
            return f"""## Sustainability Category: Amber

![Amber]({rel_base}images/traffic_amber.svg){{ align=left width="50" }}

This activity currently has moderate climate impact but may be necessary for urban functioning, with a clear pathway to decarbonization. While not yet climate-positive, this activity is actively improving the emissions profile and represents intermediate performance on the path to sustainability.
          """
        elif category == "red":
            return f"""## Sustainability Category: Red

![Red]({rel_base}images/traffic_red.svg){{ align=left width="50" }}

This activity significantly contributes to greenhouse gas emissions and undermines climate mitigation efforts. The activity should be phased out or fundamentally transformed, with financing directed toward decommissioning, replacement with sustainable alternatives, or radical decarbonization where elimination is not immediately feasible.
              """
        return "" # else skip the sustainability section

    
    @env.macro
    def generate_activity_index(coordinate=""):
        file = env.page.file
        src = os.path.join(file.src_dir, file.src_uri)
        src = src.replace("index.md", "")
        index = ""
        for root, dirs, files in os.walk(src):
            if root != src:
                owner = root.replace(src, "")
                depth = len(owner.split("/"))
                hash = "#" * depth  # (depth-1) * 4 + "-"
                with open(os.path.join(root, "index.md"), "r") as f:
                    data = frontmatter.load(f)
                    title = data.get("title", "Unknown")
                if depth < 3:
                    index += f"{hash} [{title}]({owner}/index.md)\n\n"
            else:
                depth = 0
                owner = ""
            dirs.sort()
            files.sort()
            started = False
            if depth < 2:
                for file in files:
                    if file.endswith(".md") and file != "index.md":
                        with open(os.path.join(root, file), "r") as f:
                            filename = file.replace(".md", "")
                            data = frontmatter.load(f)
                            title = data.get("title", "Unknown")
                            sustainability = data.get("sustainability", "Unknown")
                            lhs = title.split(" - ")[0]
                            rhs = title.split(" - ")[1]                            
                            id = data.get("id", "Unknown")
                            classtype = data.get("class", "Unknown")
                            if coordinate+"-" in title and classtype == "activity":
                                filep = os.path.join(owner, file)
                                # hash = " " * (depth*4) + "-"
                                # index += f"- [{title}]({filep})\n"
                                if sustainability != "Unknown":
                                    alt = ""
                                    if sustainability == "green":
                                        alt = "Sustainability category: Green"
                                    elif sustainability == "amber":
                                        alt = "Sustainability category: Amber"
                                    elif sustainability == "red":
                                        alt = "Sustainability category: Red"                                    
                                    icon = f"<img src=\"/images/traffic_{sustainability}_zoom.svg\" style='min-height:20px;min-width:20px' alt='{alt}' />"
                                else:
                                    icon = ""
                                if not started:
                                    index += "\n\n| &#8288 {:style=\"min-width:2rem;\"} | &#8288 {:style=\"min-width:3rem;\"} | Index {: width=10%} | Activity {: width=50%} | &#8288 {: width=40%} | \n"
                                    index += " | ---- | ---- | ---- | ---- | ---- |\n"
                                    # index += "\n\n| &#8288 {:style=\"min-width:3rem;\"} | Activity {: width=50%} | Index {: width=10%} | &#8288 {: width=40%} |\n"
                                    started = True
                                index += f"| {icon} |  | {lhs} | [{rhs}]({filename}.md) |  | \n"
                                # index += f"|  | <a href='{filename}'>{rhs}</a> | {lhs} |  |\n"


        return index
