import os
import frontmatter

from . import terminology
from . import util


TE_SEARCH_PATH = f"{util.markdown_base}/3-transition-elements"
parameter_path = f"{util.markdown_base}/5-resources/1-data/definitions/parameters"

def define_env(env):

    @env.macro
    def ipcc_mitigation_link(default=None):
        ipcc_code = env.page.meta.get("ipccMitigationMethod", default)
        if ipcc_code is None or ipcc_code == "":
            return ""
        title = "Unknown"
        ipcc_path = "unknown"
        search_path = f"{util.markdown_base}/2-ipcc-mitigation-options/"
        rel_base = util.convert_to_relative_base(env.page.url, default!=None)
        for root, dirs, files in os.walk(search_path):
            for file in files:
                if file.endswith(".md") and "ipcc-2019-emissions" not in root:
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
    def get_te_description_table():
        rel_base = util.convert_to_relative_base(env.page.url)
        shift = "TBD"
        activity = "TBD"
        operations = "TBD"
        atoc = "TBD"
        t = env.page.meta.get("type", None)
        shift = terminology.activity_shift_mapping[t]
        activity = env.page.meta.get("unitOfMeasure", "TBD")
        atoc_variables = []
        if "shiftFrom" in env.page.meta:
            chain = env.page.meta["shiftFrom"]["chains"][0]["chain"]
            (fullpath, data) = find_activity(chain)
            operations = data.get("work",[])
            if len(operations) > 0:
                operations = operations[0].get("operationToWork").get("unitOfMeasure")
            atoc = env.page.meta["shiftFrom"]["atoc"]["expression"]
            atoc_variables = env.page.meta["shiftFrom"]["atoc"].get("variables",[])
        elif "carbonCausalChains" in env.page.meta:
            chain = env.page.meta["carbonCausalChains"]["chains"][0]["chain"]
            (fullpath, data) = find_activity(chain)
            operations = data.get("work",[])
            if len(operations) > 0:
                operations = operations[0].get("operationToWork").get("unitOfMeasure")
            atoc = env.page.meta["carbonCausalChains"]["atoc"]["expression"]
            atoc_variables = env.page.meta["carbonCausalChains"]["atoc"].get("variables",[])
        if "/" in operations:
            operations = operations.split("/")[1]
        for i in range(len(atoc_variables)):
            atoc = atoc.replace(f"%[{i}]", atoc_variables[i])

        md = ""
        md += "\n\n"
        md += """| &#8288 {:style="min-width:10rem;"} | &#8288 {: width=100%} |\n"""
        md += """| --: | -- |\n"""
        md += f"| Shift type:          | [{shift}]({rel_base}5-resources/4-reference/4-shift-types.md) |\n"
        md += f"| Operations:          | {operations} |\n"
        md += f"| Activity measure:    | {activity} |\n"
        md += f"| Activity conversion: | {atoc} |\n"
        return md
    
    @env.macro
    def get_te_shift_type():
        t = env.page.meta.get("type", None)
        return terminology.activity_shift_mapping[t]

    def find_activity(search_id):
        for root, dirs, files in os.walk(TE_SEARCH_PATH):
            for file in files:
                if file.endswith(".md") and file != "index.md":
                    fullpath = os.path.join(root, file)
                    with open(fullpath, "r") as f:
                        data = frontmatter.load(f)
                        if "id" in data:
                            id = data["id"].strip()
                        else:
                            id = file.replace(".md", "")
                        if id == search_id:
                            return (fullpath, data)
        return (None,None)


    def get_traffic_light(sustainability, rel_base):
        if sustainability == "green":
            return f"<img src=\"{rel_base}images/traffic_green_zoom.svg\" style='min-height:20px;min-width:20px' alt='Sustainability category: Green' />"
        elif sustainability == "amber":
            return f"<img src=\"{rel_base}images/traffic_amber_zoom.svg\" style='min-height:20px;min-width:20px' alt='Sustainability category: Amber' />"
        elif sustainability == "red":
            return f"<img src=\"{rel_base}images/traffic_red_zoom.svg\" style='min-height:20px;min-width:20px' alt='Sustainability category: Red' />"
        return ""

    
    @env.macro
    def get_te_activities():
        md = ""
        rel_base = util.convert_to_relative_base(env.page.url)
        rel_base_svg = util.convert_to_relative_base(env.page.url, True)
        alt = ""
        if "shiftFrom" in env.page.meta:
            md += "\n\n"
            md += """| &#8288 {:style="min-width:2rem;"} | Shift from: {: width=100%} |\n"""
            md += """| -- | -- |\n"""

            # Build a list of tuples: (chain, fullpath, title)
            activities = []
            for a in env.page.meta["shiftFrom"]["chains"]:
                chain = a["chain"]
                (fullpath, data) = find_activity(chain)
                sustainability = data.get("sustainability", "Unknown") if data else "Unknown"
                if fullpath is not None:
                    title = data["title"]
                else:
                    title = chain  # Fallback if not found
                activities.append((chain, fullpath, title, sustainability))
            # Sort alphabetically by title (case-insensitive)
            activities.sort(key=lambda x: x[2].lower())
            for chain, fullpath, title, sustainability in activities:
                icon = get_traffic_light(sustainability, rel_base_svg)
                if fullpath is not None:
                    mp = util.clean_markdown_path(fullpath, rel_base)
                    md += f"| {icon} | [{title}]({mp}) |\n"
                else:
                    md += f"| {icon} | {chain} |\n"
        md += "\n\n"
        if "shiftTo" in env.page.meta:
            md += "\n\n"
            md += """| &#8288 {:style="min-width:2rem;"} | Shift to: {: width=100%} |\n"""
            md += """| -- | -- |\n"""
            activities = []
            for a in env.page.meta["shiftTo"]["chains"]:
                chain = a["chain"]
                (fullpath, data) = find_activity(chain)
                sustainability = data.get("sustainability", "Unknown") if data else "Unknown"
                if fullpath is not None:
                    title = data["title"]
                else:
                    title = chain
                activities.append((chain, fullpath, title, sustainability))
            activities.sort(key=lambda x: x[2].lower())
            for chain, fullpath, title, sustainability in activities:
                icon = get_traffic_light(sustainability, rel_base_svg)
                if fullpath is not None:
                    mp = util.clean_markdown_path(fullpath, rel_base)
                    md += f"| {icon} | [{title}]({mp}) |\n"
                else:
                    md += f"| {icon} | {chain} |\n"
        md += "\n\n"
        if "carbonCausalChains" in env.page.meta:
            md += "\n\n"
            md += """| &#8288 {:style="min-width:2rem;"} | Improves: {: width=100%} |\n"""
            md += """| -- | -- |\n"""
            activities = []
            for a in env.page.meta["carbonCausalChains"]["chains"]:
                chain = a["chain"]
                (fullpath, data) = find_activity(chain)
                sustainability = data.get("sustainability", "Unknown") if data else "Unknown"
                if fullpath is not None:
                    title = data["title"]
                else:
                    title = chain
                activities.append((chain, fullpath, title, sustainability))
            activities.sort(key=lambda x: x[2].lower())
            for chain, fullpath, title, sustainability in activities:
                icon = get_traffic_light(sustainability, rel_base_svg)
                if fullpath is not None:
                    mp = util.clean_markdown_path(fullpath, rel_base)
                    md += f"| {icon} | [{title}]({mp}) |\n"
                else:
                    md += f"| {icon} | {chain} | \n"

        return md


    @env.macro
    def generate_te_index(coordinate=""):
        rel_base = util.convert_to_relative_base(env.page.url, True)
        file = env.page.file
        src = os.path.join(file.src_dir, file.src_uri)
        src = src.replace("index.md", "")
        #print("generate_te_index(): file:", file)
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
                    index += f"\n\n{hash} [{title}]({owner}/index.md)\n\n"
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
                            sustainability = data.get("sustainability", "Unknown")
                            lhs = title.split(" - ")[0]
                            rhs = title.split(" - ")[1]                            
                            id = data.get("id", "Unknown")
                            mitigation = data.get("ipccMitigationMethod", "")
                            mitigation_link = ipcc_mitigation_link(mitigation)
                            classtype = data.get("class", "Unknown")
                            if coordinate+"-" in title and classtype == "transition":
                                if sustainability != "Unknown":
                                    alt = ""
                                    if sustainability == "green":
                                        alt = "Sustainability category: Green"
                                    elif sustainability == "amber":
                                        alt = "Sustainability category: Amber"
                                    elif sustainability == "red":
                                        alt = "Sustainability category: Red"                                    
                                    icon = f"<img src=\"{rel_base}images/traffic_{sustainability}_zoom.svg\" style='height:20px; width:20px' alt='{alt}' />"
                                else:
                                    icon = ""
                                if not started:
                                    index += "\n\n| &#8288 {:style=\"min-width:2rem;\"} | &#8288 {:style=\"min-width:3rem;\"} | Index {: width=10%} | Transition Element {: width=50%} | IPCC Mitigation Option {: width=40%} | \n"
                                    # index += "\n\n| &#8288 {:style=\"min-width:3rem;\"} | Transition Element {: width=50%} | Index {: width=10%} | IPCC Mitigation Option {: width=40%} |\n"
                                    index += " | ---- | ---- | ---- | ---- | ---- |\n"
                                    started = True
                                filep = os.path.join(owner, file)
                                # hash = " " * (depth*4) + "-"
                                # index += f"- [{title}]({filep})\n"
                                index += f"| {icon} | <img src=\"{rel_base}images/icons/{id}.svg\"> | {lhs} |  [{rhs}]({filename}.md) | {mitigation_link} | \n"
                                # index += f"| <img alt=\"images/icons/{id}.svg\" src=\"/images/icons/{id}.svg\"> | <a href='{filename}'>{rhs}</a> | {lhs} |  {mitigation_link} |\n"

        #print(index)
        return index
    



    @env.macro
    def generate_transition_table():
        # Go through the entire markdown directory "3-transition-elements" and build up a table of transition elements
        rel_base = util.convert_to_relative_base(env.page.url, True)
        file = env.page.file
        src = TE_SEARCH_PATH
        index = ""
        for root, dirs, files in os.walk(src):
            dirs.sort()
            files.sort()
            if root != src:
                owner = root.replace(src, "")
                depth = len(owner.split("/"))-2
                hash = "#" * depth  # * 4 + "-"
                with open(os.path.join(root, "index.md"), "r") as f:
                    data = frontmatter.load(f)
                    title = data.get("title", "Unknown")
                    sector = data.get("sector", "Unknown")
                if depth == 0:
                    index += f"""??? {sector} "{title}"\n"""
                else: 
                    index += f"\n    {hash} {title} {{.cv-ml-{depth}}}\n"
            else:
                depth = 0
                owner = ""
            dirs.sort()
            files.sort()
            if len(dirs) == 0:
                base_path = root.replace(TE_SEARCH_PATH+"/", "")
                started = False
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
                            description = data.get("description", "")
                            if sustainability != "Unknown":
                                alt = ""
                                if sustainability == "green":
                                    alt = "Sustainability category: Green"
                                elif sustainability == "amber":
                                    alt = "Sustainability category: Amber"
                                elif sustainability == "red":
                                    alt = "Sustainability category: Red"                                    
                                icon = f"<img src=\"{rel_base}images/traffic_{sustainability}_zoom.svg\" style='min-height:30px; min-width:30px' alt='{alt}' />"
                            else:
                                icon = ""
                            if classtype == "transition":
                                if not started:
                                    index += f"""
    | &#8288 {{: style="min-width:3rem;"}} | Index {{: width=8%}} | Transition Element {{: width=37%}} | Description {{: width=55%}} | &#8288 {{:style="min-width:2rem;"}} |
    | ---- | ---- | ----  | ---- | ---- |
"""
                                    started = True
                                filep = os.path.join(owner, file)
                                index += f"    | <img src=\"{rel_base}images/icons/{id}.svg\"> | {lhs} | [{rhs}]({base_path}/{filename}.md) | {description} | {icon} |\n"

        return index


#    | ![[images/icons/shift_to_electric_vehicles.svg]] | T-1A1a-TE-1 | [[3-transition-elements/1-transport/1a-mobility/1a1-road/1a1a-light-duty-vehicles/1a1a-te-01-shift_to_electric_vehicles\\|Shift to electric cars]] | Shift vehicle kilometer from petrol, diesel, LPG and gas vehicles to battery electric vehicles in vehicle kilometer to fulfill the need of mobility|
    
        
    

    
    @env.macro
    def te_sustainability():
        rel_base = util.convert_to_relative_base(env.page.url)
        text = "# Sustainability\n\n"
        category = env.page.meta.get("sustainability", "Unknown")
        if category == "green":
            return f"""## Sustainability Category: Green

![Green]({rel_base}images/traffic_green.svg){{ align=left width="50" }}

This transition element substantially contributes to climate change mitigation through significant greenhouse gas reductions, carbon sequestration, or enabling the transition to net-zero emissions. The transition element aligns with science-based pathways to limit global warming and should be prioritized for investment and expansion.
          """
        elif category == "amber":
            return f"""## Sustainability Category: Amber

![Amber]({rel_base}images/traffic_amber.svg){{ align=left width="50" }}

This transition element has only moderate climate impact but may be necessary for maintaining urban needs, with a clear pathway to decarbonization. While not aligned with net-zero targets, this transition element is actively improving the emissions profile and represents intermediate performance on the path to sustainability.
          """
        elif category == "red":
            return f"""## Sustainability Category: Red

![Red]({rel_base}images/traffic_red.svg){{ align=left width="50" }}

This transition element currently makes only insignificant contributions to climate mitigation efforts. The transition element has potential for moderate climate impact in the future given technological developments. The transition element is not recommended for investment.
              """
        return "" # else skip the sustainability section
