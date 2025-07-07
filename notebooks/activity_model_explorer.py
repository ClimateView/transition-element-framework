import marimo

__generated_with = "0.10.19"
app = marimo.App(width="medium")


@app.cell
def _(__file__):
    import marimo as mo
    import yaml
    import os
    import sys
    from collections import OrderedDict
    from pathlib import Path
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from typing import Dict, List, Optional, Any

    # Add the src directory to the Python path to import our existing modules
    project_root = Path(__file__).parent.parent
    src_path = project_root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))

    mo.md("""
    # Activity Model Explorer 🌍

    This interactive notebook explores the Transition Element Framework's activity models, 
    showing how operations translate to work, resources, and ultimately emissions.

    **Data Flow**: Operations → Work → Resources → Emissions

    **Educational Purpose**: Understand parameter sensitivity and calculation methodology
    """)
    return (
        Any,
        Dict,
        List,
        Optional,
        OrderedDict,
        Path,
        go,
        mo,
        os,
        pd,
        project_root,
        px,
        src_path,
        sys,
        yaml,
    )


@app.cell
def _(mo):
    mo.md(
        """
        ## 🎓 How to Use This Notebook

        1. **Select an Activity Model**: Choose from transport, industry, buildings, etc.
        2. **Explore Parameters**: Understand what parameters the model uses
        3. **Calculate Emissions**: Modify parameter values and see how emissions calculations are calculated
        4. **Understand the Flow**: Follow how operations → work → resources → emissions

        This tool demonstrates the practical application of the Transition Element Framework's 
        activity models and helps understand how parameter choices affect emission calculations.
        """
    )
    return


@app.cell
def _(mo, os, project_root, yaml):
    def load_activity_models():
        """Load all activity model files from the models directory."""
        models = {}
        models_path = project_root / "models"

        for root, dirs, files in os.walk(models_path):
            for file in files:
                if file.endswith('.yaml') and '-a-' in file:  # Activity files
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            model_data = yaml.safe_load(f)
                            if model_data and 'class' in model_data and model_data['class'] == 'activity':
                                # Extract sector and subsector from path
                                rel_path = os.path.relpath(file_path, models_path)
                                path_parts = rel_path.split(os.sep)
                                sector = path_parts[0] if len(path_parts) > 0 else 'unknown'

                                model_id = model_data.get('id', file.replace('.yaml', ''))
                                models[model_id] = {
                                    'data': model_data,
                                    'file_path': file_path,
                                    'sector': sector,
                                    'file_name': file
                                }
                    except Exception as e:
                        print(f"Error loading {file_path}: {e}")

        return models

    def load_parameter_files():
        """Load all parameter files from the parameters directory."""
        parameters = {}
        params_path = project_root / "models" / "parameters"

        for file in os.listdir(params_path):
            if file.endswith('.yaml'):
                file_path = params_path / file
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        param_data = yaml.safe_load(f)
                        if param_data and 'type' in param_data and param_data['type'] == 'parameter':
                            param_id = param_data.get('id', file.replace('.yaml', ''))
                            parameters[param_id] = param_data
                except Exception as e:
                    print(f"Error loading parameter {file_path}: {e}")

        return parameters

    # Load the data
    activity_models = load_activity_models()
    parameters = load_parameter_files()

    mo.md(f"""
    ## Data Loaded Successfully! ✅

    - **Activity Models**: {len(activity_models)} models loaded
    - **Parameters**: {len(parameters)} parameter definitions loaded

    """)
    return (
        activity_models,
        load_activity_models,
        load_parameter_files,
        parameters,
    )


@app.cell
def _(OrderedDict, activity_models, mo):
    def _create_model_selector():
        mo.md("## 🔍 Select an Activity Model to Explore")

        if not activity_models:
            mo.md("⚠️ No activity models found. Please check that the models directory contains activity files.")
            return None
        else:
            # Create dropdown options as a dictionary
            dropdown_options = OrderedDict({"Select a model...": ""})

            for model_id, model_info in sorted(activity_models.items(), key=lambda activity: activity[1]['data']['title']):
                title = model_info['data'].get('title', model_id)
                dropdown_options[title] = model_id

            return mo.ui.dropdown(
                options=dropdown_options,
                label="Choose an activity model:",
                value="Select a model..."
            )

    mo.output.append(mo.md(f"""
    ## Select activity

    """))
    selected_model = _create_model_selector()
    mo.output.append(selected_model)
    selected_model
    return (selected_model,)


@app.cell
def _(activity_models, selected_model):
    def get_variables(data):
        """
        Recursively extract all variable references from a model data structure.

        Args:
            data: Model data dictionary or list

        Returns:
            List of variable names found in the model
        """
        # Search for all parameter references in model dictionary:
        variable_set = ["variable", "resourceProportion"]
        val = []

        try:
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == "variables" and isinstance(value, list):
                        val.extend(value)
                    elif key in variable_set and isinstance(value, str):
                        val.append(value)
                    else:
                        val.extend(get_variables(value))
            elif isinstance(data, list):
                for item in data:
                    val.extend(get_variables(item))
        except Exception as e:
            print(f"Error extracting variables: {e}")

        return val

    # Initialize variables to avoid undefined variable errors
    model_data = {}
    model_variables = []

    if selected_model.value and selected_model.value in activity_models:
        # Extract variables used in this model
        model_data = activity_models[selected_model.value]['data']
        model_variables = get_variables(model_data)
    return get_variables, model_data, model_variables


@app.cell
def _(mo, model_variables, parameters, selected_model):
    def _create_parameter_table():
        if (selected_model is not None and selected_model.value and 
            selected_model.value != "Select a model..." and model_variables):

            # Create table of parameters with their values
            param_rows = []
            missing_params = []
            param_values = {}

            for var_name in sorted(set(model_variables)):
                if var_name in parameters:
                    param = parameters[var_name]

                    # Extract global default value
                    global_value = None
                    country_values = {}
                    for value_entry in param.get('values', []):
                        if value_entry.get('global', False):
                            global_value = value_entry.get('value')
                        elif 'country' in value_entry:
                            country = value_entry['country']
                            country_values[country] = value_entry.get('value')
                    unit = param.get('unit', 'Unknown')
                    param_values[var_name] = mo.ui.number(0, value=global_value, label=f"({unit})",)
                else:
                    missing_params.append(var_name)

            if param_values:
                param_dict = mo.ui.dictionary(param_values)
                mo.output.append( mo.md(f"## 📋 Model Parameters:"))
                mo.output.append(param_dict)
            else:
                mo.output.append(mo.md("*No parameters found for this model.*"))

            if missing_params:
                mo.output.append(mo.md(f"""
                **⚠️ Missing Parameters**: {len(missing_params)} parameters are referenced but not found:
                {', '.join(missing_params)}
                """))
        else:
            param_values = {}
            param_dict = None
            missing_params = []
            param_df = None
        return missing_params, param_values, param_dict


    missing_params, param_values, param_dict = _create_parameter_table()
    return missing_params, param_dict, param_values


@app.cell
def _(param_dict):
    def calculate_expression(expression, variables):
        """
        Safely evaluate mathematical expressions with parameter substitution.

        Args:
            expression: Mathematical expression string with %[n] placeholders
            variables: List of variable names to substitute

        Returns:
            Evaluated expression result
        """
        import re
        import operator

        # Validate expression contains only safe characters
        if not re.match(r'^[0-9+\-*/.() %\[\]]+$', expression):
            raise ValueError(f"Expression contains unsafe characters: {expression}")

        # Replace parameter placeholders with actual values
        result_expr = expression
        for i, var in enumerate(variables):
            if var in param_dict.value:
                value = param_dict.value[var]
                result_expr = result_expr.replace(f"%[{i}]", str(value))
            else:
                raise ValueError(f"Variable {var} not found in parameters")

        # Safe evaluation using ast.literal_eval for simple expressions
        try:
            # For simple arithmetic, use a safer approach
            allowed_names = {"__builtins__": {}}
            allowed_ops = {
                '+': operator.add, '-': operator.sub, '*': operator.mul, 
                '/': operator.truediv, '//': operator.floordiv,
                '**': operator.pow, '%': operator.mod
            }

            # For now, use eval but with restricted globals - TODO: implement proper expression parser
            return eval(result_expr, {"__builtins__": {}}, {})
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{result_expr}': {e}")

    return (calculate_expression,)


@app.cell
def _(calculate_expression, model_data, param_dict, selected_model):
    def calculate_activity_emissions(model_data, param_dict):
        """
        Calculate emissions for an activity model following the pedagogical flow:
        Operations → Work → Resources → Emissions

        Args:
            model_data: Activity model data structure
            param_dict: Parameter values dictionary

        Returns:
            Structured emissions data or error information
        """
        if not model_data or not param_dict:
            return {'error': 'Missing model data or parameters'}

        try:
            # Extract operations data
            operation_data = model_data.get('operation', {})
            operation_var = operation_data.get('variable')

            if not operation_var or operation_var not in param_dict:
                return {'error': 'Operation variable not found'}

            operation_value = param_dict[operation_var]
            operation_unit = operation_data.get('unitOfMeasure', '')

            # Initialize results structure
            results = {
                'operations': {
                    'variable': operation_var,
                    'value': operation_value,
                    'unit': operation_unit
                },
                'work_processes': [],
                'total_emissions': 0
            }

            # Process each work item
            work_processes = model_data.get('work', [])
            for work_process in work_processes:
                work_name = work_process.get('name', 'Unknown')
                work_unit = work_process.get('unitOfMeasure', 'unknown')

                # Calculate work intensity (operation → work)
                operation_to_work = work_process.get('operationToWork', {})
                intensity_value = calculate_expression(
                    operation_to_work.get('expression', '1'),
                    operation_to_work.get('variables', [])
                )
                intensity_unit = operation_to_work.get('unitOfMeasure', '')

                # Calculate total work
                work_value = intensity_value * operation_value

                # Initialize work process data
                work_data = {
                    'name': work_name,
                    'unit': work_unit,
                    'intensity': {
                        'value': intensity_value,
                        'unit': intensity_unit,
                        'expression': operation_to_work.get('expression', '1')
                    },
                    'work_value': work_value,
                    'resources': [],
                    'resource_mix_valid': True,
                    'total_emissions': 0
                }

                # Process resource inputs
                resource_proportion_sum = 0
                for resource in work_process.get('input', []):
                    resource_name = resource.get("resource")
                    resource_proportion = resource.get("resourceProportion", 100)

                    # Get resource proportion value
                    if resource_proportion != 100:
                        proportion_value = param_dict[resource_proportion]
                    else:
                        proportion_value = 100
                    resource_proportion_sum += proportion_value

                    # Calculate resource-to-work conversion
                    resource_to_work_value = calculate_expression(
                        resource.get('resourceToWork', {}).get('expression', '1'),
                        resource.get('resourceToWork', {}).get('variables', [])
                    )

                    # Calculate resource consumption
                    consumption_value = work_value * (proportion_value/100) * resource_to_work_value
                    consumption_unit = resource.get('unitOfMeasure', '')

                    # Calculate emission factor
                    emission_factor_value = calculate_expression(
                        resource.get('emissionFactor', {}).get('expression', '1'),
                        resource.get('emissionFactor', {}).get('variables', [])
                    )
                    emission_factor_unit = resource.get('emissionFactor', {}).get('unitOfMeasure', '')

                    # Calculate emissions for this resource
                    resource_emissions = consumption_value * emission_factor_value

                    # Store resource data
                    resource_data = {
                        'name': resource_name,
                        'proportion': proportion_value,
                        'consumption': {
                            'value': consumption_value,
                            'unit': consumption_unit
                        },
                        'emission_factor': {
                            'value': emission_factor_value,
                            'unit': emission_factor_unit
                        },
                        'emissions': resource_emissions
                    }

                    work_data['resources'].append(resource_data)
                    work_data['total_emissions'] += resource_emissions

                # Check if resource mix is valid (should sum to 100%)
                work_data['resource_mix_valid'] = int(resource_proportion_sum) == 100
                work_data['resource_proportion_sum'] = resource_proportion_sum

                results['work_processes'].append(work_data)
                results['total_emissions'] += work_data['total_emissions']

            return results

        except Exception as e:
            return {'error': f'Error calculating emissions: {str(e)}'}

    if (param_dict.value and selected_model is not None and 
            selected_model.value and selected_model.value != "Select a model..."):
        # Calculate emissions using structured approach
        emissions_data = calculate_activity_emissions(model_data, param_dict.value)
    else:
        emissions_data = None

    return calculate_activity_emissions, emissions_data


@app.cell
def _(emissions_data, mo, param_dict, selected_model):
    def render_emissions_table(emissions_data):
        """
        Generate pedagogical HTML table from structured emissions data.

        Args:
            emissions_data: Structured emissions calculation results

        Returns:
            HTML string for display
        """
        if 'error' in emissions_data:
            return f'<p>Error: {emissions_data["error"]}</p>'

        # Start HTML table
        html = """
    <style>
        td, th {
          padding: 2px 20px 2px 20px;
        }
        
        table td {
          border: 1px solid #E0E0E0;
        }
        td:nth-child(2) { text-align: end; }
    </style>
    """
        html += "<table>\n"
        html += "  <tr><th>Parameter</th><th>Value</th><th>Unit</th></tr>\n"

        # Display operations
        ops = emissions_data['operations']
        html += f"  <tr><td>Operations</td><td>{ops['value']}</td><td>{ops['unit']}</td></tr>\n"

        # Display each work process
        for work_process in emissions_data['work_processes']:
            # Work intensity and total work
            intensity = work_process['intensity']
            html += f"  <tr><td style='padding-left: 2em;'>Work intensity</td><td>{intensity['value']:.0f}</td><td>{intensity['unit']}</td></tr>\n"
            html += f"  <tr><td>Work</td><td>{work_process['work_value']:.3f}</td><td>{work_process['unit']}</td></tr>\n"

            # Resource mix validation
            mix_sum = work_process['resource_proportion_sum']
            if work_process['resource_mix_valid']:
                html += f"  <tr><td>Resource mix</td><td>{mix_sum}</td><td>%</td></tr>\n"
            else:
                html += f"  <tr><td>Resource mix</td><td style='background:red'>{mix_sum}</td><td>%</td></tr>\n"

            # Resource proportions
            for resource in work_process['resources']:
                html += f"  <tr><td style='padding-left: 2em;'>{resource['name']}</td><td>{resource['proportion']:.1f}</td><td>%</td></tr>\n"

            # Total resource consumption
            if work_process['resources']:
                first_resource_unit = work_process['resources'][0]['consumption']['unit']
                total_consumption = sum(r['consumption']['value'] for r in work_process['resources'])
                html += f"  <tr><td>Total resource consumption</td><td>{total_consumption:.3f}</td><td>{first_resource_unit}</td></tr>\n"

                # Individual resource consumption
                for resource in work_process['resources']:
                    consumption = resource['consumption']
                    html += f"  <tr><td style='padding-left: 2em;'>{resource['name']}</td><td>{consumption['value']:.3f}</td><td>{consumption['unit']}</td></tr>\n"

            # Emission factors
            html += f"  <tr><td>Emission factors</td><td></td><td></td></tr>\n"
            for resource in work_process['resources']:
                ef = resource['emission_factor']
                html += f"  <tr><td style='padding-left: 2em;'>{resource['name']}</td><td>{ef['value']:.3f}</td><td>{ef['unit']}</td></tr>\n"

            # Total emissions for this work process
            html += f"  <tr><td>Total emissions</td><td>{work_process['total_emissions']:.3f}</td><td>g_co2e</td></tr>\n"

        html += "</table>"
        return html

    def _calculate_emissions():
        """
        Orchestrate emissions calculation and HTML rendering.

        Returns:
            Dict with total_emissions and html display
        """
        if (param_dict.value and selected_model is not None and 
            selected_model.value and selected_model.value != "Select a model..."):
                # Render as HTML table
                html = render_emissions_table(emissions_data)

                # Extract total emissions
                total_emissions = emissions_data.get('total_emissions', 0) if 'error' not in emissions_data else 0

                return html
        else:
            return '<p>No model selected</p>'

    calculation_results = _calculate_emissions()
    if calculation_results:
        mo.output.append(mo.md(f"## 📋 Emissions calculations:"))
        mo.output.append(mo.Html(calculation_results))
    else:
        mo.output.append(mo.md("*Select a model and set parameters to see emissions calculations.*"))
    return calculation_results, render_emissions_table


@app.cell
def _(emissions_data, mo):
    if emissions_data:
        mo.output.append(mo.md("""
    ---

    ### Raw emission data:
    """))
        mo.output.append(emissions_data)
    return


if __name__ == "__main__":
    app.run()
