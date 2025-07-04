#!/usr/bin/env python3
"""
Extract YAML frontmatter from parameter markdown files and create corresponding YAML model files.

This script processes all markdown files (excluding index.md) in the 
markdown/5-resources/1-data/definitions/parameters/ directory, extracts YAML frontmatter 
from each file, and creates corresponding YAML files in the models/parameters/ directory.

Usage:
    python src/scripts/extract_parameters_to_models.py
"""

import os
import sys
import frontmatter
import yaml
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_paths():
    """Setup and validate required paths."""
    # Get the project root directory (assuming script is in src/scripts/ subdirectory)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    parameters_root = project_root / "markdown" / "5-resources" / "1-data" / "definitions" / "parameters"
    models_parameters_root = project_root / "models" / "parameters"
    
    if not parameters_root.exists():
        raise FileNotFoundError(f"Parameters directory not found: {parameters_root}")
    
    # Create models/parameters directory if it doesn't exist
    models_parameters_root.mkdir(parents=True, exist_ok=True)
    
    return parameters_root, models_parameters_root

def extract_frontmatter(markdown_file_path):
    """
    Extract YAML frontmatter from a markdown file.
    
    Args:
        markdown_file_path (Path): Path to the markdown file
        
    Returns:
        dict: The frontmatter metadata, or None if no frontmatter found
    """
    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            return post.metadata
    except Exception as e:
        logger.error(f"Error reading frontmatter from {markdown_file_path}: {e}")
        return None

def create_yaml_file(yaml_content, output_path):
    """
    Create a YAML file with the given content.
    
    Args:
        yaml_content (dict): The content to write as YAML
        output_path (Path): Path where the YAML file should be created
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(yaml_content, f, default_flow_style=False, sort_keys=False, 
                     allow_unicode=True, indent=2)
        
        logger.debug(f"Created YAML file: {output_path}")
        
    except Exception as e:
        logger.error(f"Error creating YAML file {output_path}: {e}")

def process_parameter_files(parameters_root, models_parameters_root):
    """
    Process all parameter markdown files in the parameters directory.
    
    Args:
        parameters_root (Path): Root path of the parameter markdown files
        models_parameters_root (Path): Root path for the output YAML files
        
    Returns:
        tuple: (processed_count, error_count)
    """
    processed_count = 0
    error_count = 0
    
    logger.info(f"Starting to process parameter files from: {parameters_root}")
    
    # Get all markdown files in the parameters directory (flat structure)
    for file_path in parameters_root.glob("*.md"):
        # Skip index.md files
        if file_path.name == "index.md":
            continue
        
        # Change file extension from .md to .yaml
        yaml_filename = file_path.stem + '.yaml'
        yaml_file_path = models_parameters_root / yaml_filename
        
        # Extract frontmatter
        frontmatter_data = extract_frontmatter(file_path)
        
        if frontmatter_data is None:
            logger.warning(f"No frontmatter found in: {file_path}")
            error_count += 1
            continue
        
        if not frontmatter_data:
            logger.warning(f"Empty frontmatter in: {file_path}")
            error_count += 1
            continue
        
        # Create YAML file
        create_yaml_file(frontmatter_data, yaml_file_path)
        processed_count += 1
        
        if processed_count % 100 == 0:
            logger.info(f"Processed {processed_count} files...")
    
    return processed_count, error_count

def main():
    """Main function to orchestrate the parameter frontmatter extraction process."""
    try:
        logger.info("Starting parameter frontmatter extraction to models")
        
        # Setup paths
        parameters_root, models_parameters_root = setup_paths()
        logger.info(f"Parameters source: {parameters_root}")
        logger.info(f"Models destination: {models_parameters_root}")
        
        # Process all parameter files
        processed_count, error_count = process_parameter_files(parameters_root, models_parameters_root)
        
        # Report results
        logger.info(f"Processing complete!")
        logger.info(f"Successfully processed: {processed_count} files")
        if error_count > 0:
            logger.warning(f"Errors encountered: {error_count} files")
        
        return 0 if error_count == 0 else 1
        
    except Exception as e:
        logger.error(f"Script failed with error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())