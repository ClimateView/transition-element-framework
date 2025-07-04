# Transition Element Framework - Project Guide

This document provides key information about the Transition Element Framework project to help Claude assist with refactoring and writing new scripts.

## Project Overview

The Transition Element Framework is a markdown-based static website for climate mitigation documentation, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). The site contains structured information about transition elements, activities, and mitigation options related to climate change.

## Repository Structure

The repository is organized into three main directories:

### `/markdown/` - Content Directory
Main content directory with Markdown files structured hierarchically:
  - `/2-ipcc-mitigation-options/`: IPCC mitigation methods organized by sector
  - `/3-transition-elements/`: Transition elements organized by sector
  - `/4-whitepapers/`: Analysis and framework documents
  - `/5-resources/`: Reference materials, data, bibliography
  - `/6-examples/`: Example implementations and use cases
  - `/images/`: Static assets, icons, diagrams
  - `/downloads/`: Downloadable resources (PDFs, etc.)

### `/models/` - Parameter and Model Definitions
Contains structured data and parameter definitions:
  - `/parameters/`: YAML files with emission factors, energy intensities, and other model parameters
  - Sectoral model directories (`1-transport/`, `2-industry/`, etc.)
  - Model configuration and data files

### `/src/` - Source Code
Python source code and configuration files:
  - `/macros/`: Python modules for MkDocs macros that generate site content
    - `activity.py`: Handles activity-related macros
    - `transitionelement.py`: Handles transition element macros
    - `mitigation.py`: Handles IPCC mitigation macros
    - `terminology.py`: Terminology definitions
    - `util.py`: Utility functions
  - `/scripts/`: Utility scripts for site generation and maintenance
    - `update_md_descriptions.py`: Updates markdown file descriptions
    - Various data import and manipulation scripts
  - `/tests/`: Unit tests for the macros and functionality
    - `/macros/`: Tests for macro implementations
    - Various test files for markdown processing
  - `/overrides/`: MkDocs theme customizations
  - `/includes/`: Shared markdown content (abbreviations, etc.)
  - Configuration files: `mkdocs.yml`, `pytest.ini`

## Key Concepts

1. **Transition Elements**: Components representing shifts in energy usage or processes to reduce emissions
2. **Activities**: Actions or processes that produce emissions
3. **IPCC Mitigation Options**: Standard climate mitigation approaches defined by IPCC

## Content Structure

Each transition element follows a structured format:
- Title using a hierarchical code (e.g., "T-1A1a-TE-1 - Shift to electric vehicles")
- YAML frontmatter with metadata (id, type, description, etc.)
- Standardized sections (Background, Activities, Parameters)
- References to related IPCC mitigation methods

## Technology Stack

- **Python 3.10+**: Required for development
- **uv**: Modern Python package manager and virtual environment manager
- **MkDocs**: Static site generator
- **MkDocs Material**: Theme and extensions
- **Custom Python macros**: Generate dynamic content with mkdocs-macros-plugin
- **YAML/Frontmatter**: For structured metadata
- **Tree-sitter**: Used for parsing Markdown and YAML in the linter

## Development Workflow

1. **Setup**: Use `uv sync` to install dependencies and create virtual environment
2. **Development server**: Run `uv run mkdocs serve --dirtyreload` from the src/ directory for local testing
3. **Testing**: Run tests with `uv run pytest` from the src/ directory (configured in src/pytest.ini)
4. **Linting**: Use `uv run python src/linter.py` to validate content structure

## File Manipulation Patterns

When writing scripts for file manipulation:

1. **Markdown Processing**: 
   - Use `python-frontmatter` to parse and update frontmatter metadata
   - Follow established patterns in `src/scripts/update_md_descriptions.py`

2. **Path Handling**:
   - Content is in `/markdown/` directory
   - Transition elements are in `/markdown/3-transition-elements/[sector]/...`
   - Parameters are in `/models/parameters/`
   - Use `os.walk()` for traversing the directory structure

3. **Data Import**:
   - External data is often in JSON/YAML format
   - Parameter files are stored in `/models/parameters/` as YAML
   - See scripts in `src/scripts/` for examples of importing external data

4. **Content Generation**:
   - Templates are often defined inline in scripts
   - Follow the established hierarchical naming conventions
   - Parameter extraction scripts can generate model files in `/models/`

## Common Tasks

1. **Creating new transition elements**: See `src/scripts/` for transition element creation scripts
2. **Updating descriptions**: See `src/scripts/update_md_descriptions.py`
3. **Managing parameters**: Parameter files are in `/models/parameters/` as YAML files
4. **Testing macros**: See test files in `src/tests/macros/`
5. **Extracting parameters**: Use scripts in `src/scripts/` to extract parameters from content to models

## Naming Conventions

- **File names**: Follow patterns like `1a1a-te-01-shift_to_electric_vehicles.md`
- **IDs**: Machine-readable identifiers like `shift_to_electric_vehicles`
- **Titles**: Include hierarchical coordinates like `T-1A1a-TE-1 - Shift to electric vehicles`

## Testing

Tests are written using pytest and can be run from the src/ directory with:
```bash
cd src/
uv run pytest
```

## Best Practices

1. Maintain the hierarchical structure in filenames and content
2. Use the existing macros for content generation
3. Follow the YAML frontmatter conventions
4. Verify changes with the development server before committing
5. Run linter to check content validity