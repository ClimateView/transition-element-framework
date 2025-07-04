#!/usr/bin/env python3
"""
Extract YAML frontmatter from markdown files and create corresponding YAML model files.

This script traverses the markdown/3-transition-elements/ directory, extracts YAML frontmatter 
from all markdown files (excluding index.md), and creates corresponding YAML files in the 
models/ directory with the same hierarchical folder structure.

Usage:
    python src/scripts/extract_frontmatter_to_models.py
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
    
    markdown_root = project_root / "markdown" / "3-transition-elements"
    models_root = project_root / "models"
    
    if not markdown_root.exists():
        raise FileNotFoundError(f"Markdown directory not found: {markdown_root}")
    
    # Create models directory if it doesn't exist
    models_root.mkdir(exist_ok=True)
    
    return markdown_root, models_root

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
        # Create parent directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(yaml_content, f, default_flow_style=False, sort_keys=False, 
                     allow_unicode=True, indent=2)
        
        logger.debug(f"Created YAML file: {output_path}")
        
    except Exception as e:
        logger.error(f"Error creating YAML file {output_path}: {e}")

def get_relative_path(file_path, base_path):
    """
    Get the relative path of a file from a base directory.
    
    Args:
        file_path (Path): The full path to the file
        base_path (Path): The base directory path
        
    Returns:
        Path: The relative path
    """
    return file_path.relative_to(base_path)

def process_markdown_files(markdown_root, models_root):
    """
    Process all markdown files in the transition-elements directory.
    
    Args:
        markdown_root (Path): Root path of the markdown files
        models_root (Path): Root path for the output YAML files
        
    Returns:
        tuple: (processed_count, error_count)
    """
    processed_count = 0
    error_count = 0
    
    logger.info(f"Starting to process markdown files from: {markdown_root}")
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(markdown_root):
        root_path = Path(root)
        
        for file in files:
            # Skip index.md files and non-markdown files
            if file == "index.md" or not file.endswith(".md"):
                continue
                
            markdown_file_path = root_path / file
            
            # Calculate relative path from markdown root
            relative_path = get_relative_path(root_path, markdown_root)
            
            # Create corresponding path in models directory
            models_dir = models_root / relative_path
            
            # Change file extension from .md to .yaml
            yaml_filename = file.replace('.md', '.yaml')
            yaml_file_path = models_dir / yaml_filename
            
            # Extract frontmatter
            frontmatter_data = extract_frontmatter(markdown_file_path)
            
            if frontmatter_data is None:
                logger.warning(f"No frontmatter found in: {markdown_file_path}")
                error_count += 1
                continue
            
            if not frontmatter_data:
                logger.warning(f"Empty frontmatter in: {markdown_file_path}")
                error_count += 1
                continue
            
            # Create YAML file
            create_yaml_file(frontmatter_data, yaml_file_path)
            processed_count += 1
            
            if processed_count % 50 == 0:
                logger.info(f"Processed {processed_count} files...")
    
    return processed_count, error_count

def main():
    """Main function to orchestrate the frontmatter extraction process."""
    try:
        logger.info("Starting frontmatter extraction to models")
        
        # Setup paths
        markdown_root, models_root = setup_paths()
        logger.info(f"Markdown source: {markdown_root}")
        logger.info(f"Models destination: {models_root}")
        
        # Process all markdown files
        processed_count, error_count = process_markdown_files(markdown_root, models_root)
        
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