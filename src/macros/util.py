import yaml

markdown_base = "../markdown"

bibfile = f"{markdown_base}/5-resources/references.bib"

def convert_to_relative_base(url, fromfolder=False):
    # Remove trailing slash if present
    url = url.rstrip('/')

    # Split the path into parts by '/'
    parts = url.split('/')

    depth = len(parts)
    if not fromfolder:
        # Ignore the first empty part (from leading slash) and the last folder
        depth -= 1

    # Construct the relative URL base
    relative_url_base = '../' * depth

    return relative_url_base


def clean_markdown_path(path, base="/"):
    if ".md" not in path:
        print("*** clean_markdown_path: ", path, base)
    # strip everything before markdown/
    marker = "markdown/"
    p = path.find(marker)
    if p != -1:
        path = path[p+len(marker):]
    clean = path.replace(".md", "")
    if not clean.startswith("/"):
        clean = base + clean + ".md"
    return clean


def define_env(env):
    "Hook function"

    @env.macro
    def json_to_yaml():
        # TODO: refactor naming of this function - no longer JSON to YAML
        #       instead this function returns cleaned YAML metadata from the page
        def make_plain(model):
            """Recursively convert custom objects to plain Python types."""
            if isinstance(model, dict):
                return {key: make_plain(value) for key, value in model.items()}
            elif isinstance(model, list):
                return [make_plain(item) for item in model]
            elif hasattr(model, "__dict__"):  # For custom objects with attributes
                return make_plain(vars(model))

            return model  # Return the data as-is for other types

        strip_keys = ["progress", "class", "ipccMitigationMethod", "sector", "id", "name", "title"]
        # make deep copy of the metadata
        metadata = env.page.meta.copy()
        
        for key in strip_keys:
            if key in metadata:
                metadata.pop(key)
        return yaml.safe_dump(make_plain(metadata),
                              allow_unicode=True,
                              default_flow_style=False,
                              sort_keys=False)

    @env.macro
    def full_bibliography_list():
        global bibfile
        from pybtex.database import parse_file
        bib_data = parse_file(bibfile)

        titles = []
        for entry in bib_data.entries:
            title = bib_data.entries[entry].fields.get("title", "Unknown")
            titles.append(title)

        titles.sort()
        mdlist = ""
        for title in titles:
            for entry in bib_data.entries:
                if title == bib_data.entries[entry].fields.get("title", "Unknown"):
                    mdlist += f"- {title} [@{entry}]\n"            

        return mdlist
