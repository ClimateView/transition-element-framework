
# Transition Element Framework

Welcome to the open-source repository for the **Transition Element Framework (TEF)** - a standardized, accessible framework that transforms IPCC climate mitigation strategies into practical building blocks for climate action.

![Transition Element Periodic Table](/markdown/images/periodic_table.svg "The Transition Element Framework")


🌐 **Live Website**: [transitionelements.org](https://transitionelements.org)

## About the Project

The Transition Element Framework converts complex IPCC knowledge into a practical platform that provides a shared language and transparent methodology for planning and measuring climate action. Developed by ClimateView in collaboration with Swedish agencies and cities worldwide, the TEF helps organizations move beyond pledges to implement actionable, collaborative mitigation strategies.

## Repository Structure

This repository is organized into three main directories:

### 📊 `models/`
Contains YAML model files that define the core framework:
- **Sector-based organization**: Transport, industry, buildings, energy, waste, and AFOLU (Agriculture, Forestry and Other Land Use)
- **Activity definitions**: Specific climate actions and mitigation strategies
- **Parameters**: Emission factors, energy intensities, and other quantitative data used in calculations
- **Hierarchical structure**: Organized to match IPCC categorization standards

### 📝 `markdown/`
Contains the documentation content that generates the website:
- **Generated from models**: Content is automatically derived from the YAML model files
- **Website structure**: Organized to match the final website navigation
- **Markdown format**: Standard markdown files with some extensions for enhanced functionality

### 🛠️ `src/`
Contains all Python code and build tools:
- **Generation scripts**: Python code that transforms models into markdown documentation
- **MkDocs configuration**: Static site generation using Material for MkDocs
- **Build tools**: Scripts for processing, validation, and deployment
- **Templates**: HTML templates for customizing the website appearance

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). This means you can share and adapt the material for non-commercial purposes, provided you give appropriate credit and distribute any derivatives under the same license.

## Contributing

Contributions are welcome from the scientific and climate action communities. Content contributors can edit markdown files directly, while developers can enhance the build system and model processing.

## Developer Setup

For developers wanting to work on the build system or run the site locally:

### Requirements
- Python 3.10 or higher
- Recommended: [uv](https://docs.astral.sh/uv/) for fast Python package and project management

### Setup
1. Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Create and activate your Python environment: `uv venv --python 3.10`
3. Install dependencies: `uv pip install -r src/requirements.txt`

### Development Server
Run the development server from the `src` directory:
```bash
cd src
uv run mkdocs serve --dirtyreload
```
Navigate to <http://localhost:8000/> to view the site.

*Note: `--dirtyreload` enables faster reloading but may show navigation titles as 'None'*

## Technical Details

- **Static Site Generator**: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **Configuration**: `src/mkdocs.yml`
- **HTML Overrides**: Custom templates in `src/overrides/`
- **Bibliography**: Managed in Zotero, exported to `markdown/5-resources/references.bib`
- **Citation Style**: Chicago Manual of Style 17th edition (author-date)

## Deployment

The website is hosted as an Azure Static Web App with automated deployment via GitHub Actions. Configuration files:
- `src/staticwebapp.config.json` - Azure Static Web App configuration
- `.github/workflows/azure-static-web-apps-gentle-bay-0e0a82503.yml` - Deployment workflow

---

*The Transition Element Framework is a work in progress, developed collaboratively to support global climate action initiatives.*

