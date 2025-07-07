# Activity Model Explorer Notebook

This directory contains interactive Marimo notebooks for exploring the Transition Element Framework models.

## Getting Started

1. **Install dependencies** (if not already done):
   ```bash
   uv sync
   ```

2. **Run the notebook**:
   ```bash
   uv run marimo edit notebooks/activity_model_explorer.py
   ```

3. **Or run in view mode** (read-only):
   ```bash
   uv run marimo run notebooks/activity_model_explorer.py
   ```

## About the Activity Model Explorer

This interactive notebook provides an educational interface for understanding how the Transition Element Framework's activity models work:

### Features

- **📋 Model Browser**: Explore activity models organized by sector
- **🔧 Parameter Explorer**: View parameter definitions and their values across countries
- **🌍 Global Comparison**: Compare parameter values between different countries
- **🧮 Emission Calculator**: Calculate emissions step-by-step using real model data
- **📊 Visualizations**: Interactive charts showing parameter variations

### Educational Flow

1. **Select an Activity Model**: Choose from transport, industry, buildings, etc.
2. **Explore Parameters**: Understand what parameters the model uses
3. **Calculate Emissions**: Modify parameter values and see how emissions calculations are calculated

### Model Structure Explained

Activity models follow this structure:

```
Operations (stock/growth) 
    ↓
Work (energy processes)
    ↓
Resources (fuels/electricity with emission factors)
    ↓
Emissions (final CO2e calculations)
```

## File Structure

- `activity_model_explorer.py`: Main interactive notebook
- `README.md`: This documentation file

## Requirements

- Python 3.10+
- All dependencies from pyproject.toml (installed via `uv sync`)
- Access to the models/ directory with activity and parameter files
