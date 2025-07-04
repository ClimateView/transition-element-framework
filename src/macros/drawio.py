from lxml import etree as ET
from io import BytesIO
import yaml
import re
import string
import json
from html import escape


drawio_template = b"""<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" version="24.7.10">
  <diagram name="Page-1" id="VEgEcEARJQQsYIdDDOoB">
    <mxGraphModel dx="1037" dy="634" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="pkKilJBz2SehiPoet6P4-21" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeWidth=0.5;strokeColor=#000000;dashed=1;dashPattern=1 4;opacity=50;textOpacity=50;" parent="1" vertex="1">
          <mxGeometry x="340" y="220" width="120" height="280" as="geometry" />
        </mxCell>
        <UserObject label="" tags="GROUP_D" id="pkKilJBz2SehiPoet6P4-16">
          <mxCell style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="iPXNtMmSq03kvJjk4ff--2" target="pkKilJBz2SehiPoet6P4-9" edge="1">
            <mxGeometry relative="1" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" tags="GROUP_E" id="pkKilJBz2SehiPoet6P4-17">
          <mxCell style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="iPXNtMmSq03kvJjk4ff--2" target="pkKilJBz2SehiPoet6P4-10" edge="1">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="500" y="440" />
                <mxPoint x="500" y="540" />
              </Array>
            </mxGeometry>
          </mxCell>
        </UserObject>
        <mxCell id="pkKilJBz2SehiPoet6P4-18" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" parent="1" source="iPXNtMmSq03kvJjk4ff--2" target="pkKilJBz2SehiPoet6P4-11" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="iPXNtMmSq03kvJjk4ff--2" value="WORK" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=7;" parent="1" vertex="1">
          <mxGeometry x="360" y="400" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="iPXNtMmSq03kvJjk4ff--8" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" parent="1" source="iPXNtMmSq03kvJjk4ff--3" target="iPXNtMmSq03kvJjk4ff--2" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="400" y="320" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="iPXNtMmSq03kvJjk4ff--3" value="OPERATIONS" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=7;" parent="1" vertex="1">
          <mxGeometry x="360" y="240" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="gUdC2CcRAoVtNzy_I1OT-12" value="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;OPERATION_EFFICIENCY&lt;/font&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
          <mxGeometry x="405" y="345" width="325" height="30" as="geometry" />
        </mxCell>
        <mxCell id="gUdC2CcRAoVtNzy_I1OT-6" value="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;OPERATIONS_PARAMETER&lt;/font&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
          <mxGeometry x="450" y="265" width="250" height="30" as="geometry" />
        </mxCell>
        <mxCell id="pkKilJBz2SehiPoet6P4-13" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" parent="1" source="pkKilJBz2SehiPoet6P4-5" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="360" y="440" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;EMISSION_FACTOR_B&lt;/font&gt;" tags="GROUP_B" id="gUdC2CcRAoVtNzy_I1OT-14">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="404" y="569" width="240" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;RESOURCE_EFFICIENCY_B&lt;/font&gt;" tags="GROUP_B" id="gUdC2CcRAoVtNzy_I1OT-35">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="160" y="534" width="129" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;RESOURCE_PROPORTION_B&lt;/font&gt;" tags="GROUP_B" id="gUdC2CcRAoVtNzy_I1OT-37">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="160" y="517" width="129" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font face=&quot;Courier New&quot; style=&quot;font-size: 6px;&quot;&gt;RESOURCE_OUT_D&lt;/font&gt;" tags="GROUP_D" id="rhaJmpulONdv8qM9c0SB-14">
          <mxCell style="text;html=1;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="502" y="417" width="129" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font face=&quot;Courier New&quot; style=&quot;font-size: 6px;&quot;&gt;RESOURCE_OUT_E&lt;/font&gt;" tags="GROUP_E" id="rhaJmpulONdv8qM9c0SB-15">
          <mxCell style="text;html=1;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;fillColor=none;gradientColor=none;" parent="1" vertex="1">
            <mxGeometry x="502" y="517" width="129" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="RESOURCE_B" tags="GROUP_B" id="pkKilJBz2SehiPoet6P4-6">
          <mxCell style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=8;" parent="1" vertex="1">
            <mxGeometry x="67" y="500" width="90" height="80" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="RESOURCE_D" tags="GROUP_D" id="pkKilJBz2SehiPoet6P4-9">
          <mxCell style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=8;" parent="1" vertex="1">
            <mxGeometry x="641" y="400" width="90" height="80" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="RESOURCE_E" tags="GROUP_E" id="pkKilJBz2SehiPoet6P4-10">
          <mxCell style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=8;" parent="1" vertex="1">
            <mxGeometry x="641" y="500" width="90" height="80" as="geometry" />
          </mxCell>
        </UserObject>
        <mxCell id="pkKilJBz2SehiPoet6P4-11" value="EMISSIONS" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=8;" parent="1" vertex="1">
          <mxGeometry x="355" y="600" width="90" height="80" as="geometry" />
        </mxCell>
        <mxCell id="pkKilJBz2SehiPoet6P4-25" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="pkKilJBz2SehiPoet6P4-22" target="iPXNtMmSq03kvJjk4ff--3" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="pkKilJBz2SehiPoet6P4-22" value="STOCK" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#f5f5f5;strokeColor=#666666;fontSize=7;fontColor=#333333;" parent="1" vertex="1">
          <mxGeometry x="72" y="240" width="80" height="80" as="geometry" />
        </mxCell>
        <UserObject label="RESOURCE_A" tags="GROUP_A" id="pkKilJBz2SehiPoet6P4-5">
          <mxCell style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=8;shadow=0;rounded=0;" parent="1" vertex="1">
            <mxGeometry x="67" y="400" width="90" height="80" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;RESOURCE_EFFICIENCY_A&lt;/font&gt;" tags="GROUP_A" id="gUdC2CcRAoVtNzy_I1OT-13">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="162" y="434" width="129" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;EMISSION_FACTOR_A&lt;/font&gt;" tags="GROUP_A" id="gUdC2CcRAoVtNzy_I1OT-25">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="404" y="554" width="240" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;RESOURCE_PROPORTION_A&lt;/font&gt;" tags="GROUP_A" id="gUdC2CcRAoVtNzy_I1OT-39">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="162" y="417" width="129" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" tags="GROUP_B" id="pkKilJBz2SehiPoet6P4-15">
          <mxCell style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="pkKilJBz2SehiPoet6P4-6" target="iPXNtMmSq03kvJjk4ff--2" edge="1">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="300" y="540" />
                <mxPoint x="300" y="440" />
              </Array>
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;EMISSION_FACTOR_C&lt;/font&gt;" tags="GROUP_C" id="gUdC2CcRAoVtNzy_I1OT-31">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="404" y="539" width="240" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;RESOURCE_EFFICIENCY_C&lt;/font&gt;" tags="GROUP_C" id="gUdC2CcRAoVtNzy_I1OT-36">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="160" y="634" width="129" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="&lt;font style=&quot;font-size: 6px;&quot; face=&quot;Courier New&quot;&gt;RESOURCE_PROPORTION_C&lt;/font&gt;" tags="GROUP_C" id="gUdC2CcRAoVtNzy_I1OT-40">
          <mxCell style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=6;" parent="1" vertex="1">
            <mxGeometry x="160" y="617" width="129" height="30" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" tags="GROUP_C" id="pkKilJBz2SehiPoet6P4-12">
          <mxCell style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="pkKilJBz2SehiPoet6P4-7" target="iPXNtMmSq03kvJjk4ff--2" edge="1">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="300" y="640" />
                <mxPoint x="300" y="440" />
              </Array>
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="RESOURCE_C" tags="GROUP_C" id="pkKilJBz2SehiPoet6P4-7">
          <mxCell style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=8;" parent="1" vertex="1">
            <mxGeometry x="67" y="600" width="90" height="80" as="geometry" />
          </mxCell>
        </UserObject>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""


def generate(model):
    SUB_TEMPLATE = string.Template(
        '<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="$config"></div>'
    )
    modelxml = get_drawn_model(model)
    config = {
        "highlight": "#0000ff",
        "lightbox": True,
        "nav": False,
        "resize": False,
        "auto-fit": True,
        "toolbar": "lightbox",
        "edit": "_blank",
        "editable": False,
        "title": "Activity Model Diagram",
        "xml": modelxml.decode()
    }
    return SUB_TEMPLATE.substitute(config=escape(json.dumps(config)))


drawio_file = "template_hex.drawio"
activity_folder = "/Users/mark/proj/cv/model-definitions/carbonCausalChains"


def delete_cells_with_tag(tree, tag_value):
    """Delete cells with the specified tag and remove any empty parent nodes."""
    root = tree.getroot()

    # Step 1: Iterate over all mxCell elements and remove those with the specified tag attribute
    parents_to_check = set()
    for cell in root.xpath(".//mxCell[@tags]"):  # Find all mxCell elements with a tag attribute
        if cell.attrib['tags'] == tag_value:
            parent_node = cell.getparent()
            parents_to_check.add(parent_node)  # Track the parent nodes to check later
            parent_node.remove(cell)
    for cell in root.xpath(".//UserObject[@tags]"):  # Find all mxCell elements with a tag attribute
        if cell.attrib['tags'] == tag_value:
            parent_node = cell.getparent()
            parents_to_check.add(parent_node)  # Track the parent nodes to check later
            parent_node.remove(cell)

    # Step 2: Remove any empty parent nodes
    for parent_node in parents_to_check:
        if len(parent_node) == 0:  # If the parent node has no children, remove it
            parent_of_parent = parent_node.getparent()
            if parent_of_parent is not None:
                parent_of_parent.remove(parent_node)


def delete_cells_and_empty_parents(tree, parent_id):
    """Delete cells with the specified parent_id and remove any empty parent nodes."""
    root = tree.getroot()

    # Step 1: Iterate over all mxCell elements and remove those with the specified parent
    parents_to_check = set()
    for cell in root.xpath(".//mxCell[@parent]"):  # Find all mxCell elements with a parent attribute
        if cell.attrib['parent'] == parent_id:
            parent_node = cell.getparent()
            parents_to_check.add(parent_node)  # Track the parent nodes to check later
            parent_node.remove(cell)

    # Step 2: Remove any empty parent nodes
    for parent_node in parents_to_check:
        if len(parent_node) == 0:  # If the parent node has no children, remove it
            parent_of_parent = parent_node.getparent()
            if parent_of_parent is not None:
                parent_of_parent.remove(parent_node)


def replace_mxcell_value(tree, old_value, new_value):
    """Find the mxCell node with a specific 'value' attribute and replace it with a new value."""
    root = tree.getroot()

    replaced = False
    # Step 1: Replace in mxCell elements with 'value' attribute
    for cell in root.xpath(".//mxCell[@value]"):  # Find all mxCell elements with a 'value' attribute
        if old_value in cell.attrib['value']:
            cell.attrib['value'] = cell.attrib['value'].replace(old_value, new_value)
            # new_value_clean = new_value.replace("\n", "\\n").replace("\t", "\\t")
            # print(f"  Replaced '{old_value}' with '{new_value_clean}' in mxCell")
            replaced = True

    # Step 2: Replace in UserObject elements with 'label' attribute
    for user_object in root.xpath(".//UserObject[@label]"):  # Find all UserObject elements with a 'label' attribute
        # print(old_value, user_object.attrib)
        if old_value in user_object.attrib['label']:
            # print("Found")
            user_object.attrib['label'] = user_object.attrib['label'] \
                                                     .replace(old_value, new_value)
            # new_value_clean = new_value.replace("\n", "\\n").replace("\t", "\\t")
            # print(f"  Replaced '{old_value}' with '{new_value_clean}' in UserObject")
            replaced = True

    # Step 3: Notify if no replacements were made
    if not replaced:
        print(f"No mxCell or UserObject found with the value '{old_value}'")


def load_drawio_file(file_path):
    """Load the .drawio XML file and return the parsed tree."""
    return ET.parse(file_path)


def save_drawio_file(tree, output_file):
    """Save the modified tree to an XML file."""
    tree.write(output_file, encoding='utf-8', xml_declaration=True)


def replace_expression_variables(expression, variables):
    """Replace placeholders like %[0], %[1], etc. in the expression with corresponding variables."""

    # Define a regex pattern to match %[0], %[1], %[2], etc.
    pattern = r"%\[(\d+)\]"

    # Replace each match in the expression
    def replace_match(match):
        # Get the index from the match (e.g., 0, 1, etc.)
        index = int(match.group(1))
        # Return the corresponding variable from the variables list if index is valid
        if index < len(variables):
            return variables[index]
        else:
            raise ValueError(f"Index {index} out of range for variables list.")

    # Use re.sub to replace all matches of the pattern
    replaced_expression = re.sub(pattern, replace_match, expression)

    return replaced_expression


def load_yaml_file(file_path):
    """Load a YAML file and return it as a deep dictionary."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


def get_drawn_model(chain):

    # Load the .drawio file
    # tree = ET.fromstring(drawio_template)
    tree = ET.parse(BytesIO(drawio_template))


    # Access chains
    if True:
        chain_name = chain.get('name', 'N/A')
        operation = chain.get('operation', {})
        growth_type = operation.get('growthType', 'N/A')
        growth_variable = operation.get('variable', 'N/A')
        operation_variable = operation.get('variable', 'N/A')
        operation_unit = ""
        replace_mxcell_value(tree, "OPERATIONS_PARAMETER", operation_variable)

        # Work section
        work_list = chain.get('work', [])
        for work in work_list:
            work_name = work.get('name', 'N/A')
            work_unit = work.get('unitOfMeasure', 'N/A')

            replace_mxcell_value(tree, "WORK", f"WORK:\n{work_name}\n({work_unit})")

            # Operation to Work
            operation_to_work = work.get('operationToWork', {})
            operation_to_work_unit = operation_to_work.get('unitOfMeasure', 'N/A')
            if len(operation_to_work_unit.split("/")) > 1:
                operation_unit = operation_to_work_unit.split("/")[1]
            else:
                operation_unit = "unknown"
            operation_to_work_expr = operation_to_work.get('expression', 'N/A')
            operation_to_work_variables = operation_to_work.get('variables', 'N/A')
            operation_to_work_variable = replace_expression_variables(operation_to_work_expr, operation_to_work_variables)
            replace_mxcell_value(tree, "OPERATION_EFFICIENCY",
                                 f"{operation_to_work_variable}\n({operation_to_work_unit})")


            # Input section
            inputs = work.get('input', [])
            if len(inputs) < 3:
                delete_cells_with_tag(tree, "GROUP_C")
            if len(inputs) < 2:
                delete_cells_with_tag(tree, "GROUP_B")

            i = 0
            for input_resource in inputs:
                i += 1
                
                resource_name = input_resource.get('resource', 'N/A')
                resource_unit = input_resource.get('unitOfMeasure', 'N/A')
                if i == 1:
                    replace_mxcell_value(tree, "RESOURCE_A",
                                f"RESOURCE:\n{resource_name}\n({resource_unit})")
                elif i == 2:
                    replace_mxcell_value(tree, "RESOURCE_B", 
                                f"RESOURCE:\n{resource_name}\n({resource_unit})")
                elif i == 3:
                    replace_mxcell_value(tree, "RESOURCE_C", 
                                 f"RESOURCE:\n{resource_name}\n({resource_unit})")
                
                resource_unit = input_resource.get('unitOfMeasure', 'N/A')
                resource_proportion = input_resource.get('resourceProportion', '')
                resource_work_unit = input_resource.get('resourceToWork', {}).get('unitOfMeasure', '')
                resource_work_expr = input_resource.get('resourceToWork', {}).get('expression', 'N/A')
                resource_work_vars = input_resource.get('resourceToWork', {}).get('variables', [])
                resource_work = replace_expression_variables(resource_work_expr, resource_work_vars)
                resource_emission_unit = input_resource.get('emissionFactor', {}).get('unitOfMeasure', '')
                resource_emission_expr = input_resource.get('emissionFactor', {}).get('expression', 'N/A')
                resource_emission_vars = input_resource.get('emissionFactor', {}).get('variables', [])
                resource_emission = replace_expression_variables(resource_emission_expr, resource_emission_vars)
                if i == 1:
                    replace_mxcell_value(tree, "RESOURCE_PROPORTION_A",
                                         resource_proportion)
                    replace_mxcell_value(tree, "RESOURCE_EFFICIENCY_A",
                                 f"{resource_work}\n({resource_work_unit})")
                    replace_mxcell_value(tree, "EMISSION_FACTOR_A",
                                 f"{resource_emission} ({resource_emission_unit})")
                elif i == 2:
                    replace_mxcell_value(tree, "RESOURCE_PROPORTION_B",
                                         resource_proportion)
                    replace_mxcell_value(tree, "RESOURCE_EFFICIENCY_B",
                                 f"{resource_work}\n({resource_work_unit})")
                    replace_mxcell_value(tree, "EMISSION_FACTOR_B",
                                 f"{resource_emission} ({resource_emission_unit})")
                elif i == 3:
                    replace_mxcell_value(tree, "RESOURCE_PROPORTION_C",
                                         resource_proportion)
                    replace_mxcell_value(tree, "RESOURCE_EFFICIENCY_C",
                                 f"{resource_work}\n({resource_work_unit})")
                    replace_mxcell_value(tree, "EMISSION_FACTOR_C",
                                 f"{resource_emission} ({resource_emission_unit})")

            # Output section
            outputs = work.get('output', [])
            if len(outputs) < 2:
                delete_cells_with_tag(tree, "GROUP_E")
            if len(outputs) < 1:
                delete_cells_with_tag(tree, "GROUP_D")
            i = 0
            for output_resource in outputs:
                i += 1
                resource_name = output_resource.get('resource', 'N/A')
                resource_unit = output_resource.get('unitOfMeasure', 'N/A')
                resource_work_expr = output_resource.get('workToResource', {}).get('expression', 'N/A')
                resource_work_vars = output_resource.get('workToResource', {}).get('variables', [])
                resource_work = replace_expression_variables(resource_work_expr, resource_work_vars)
                resource_work_unit = input_resource.get('resourceToWork', {}).get('unitOfMeasure', '')

                if i == 1:
                    replace_mxcell_value(tree, "RESOURCE_D",
                               f"RESOURCE:\n{resource_name}\n({resource_unit})")
                    replace_mxcell_value(tree, "RESOURCE_OUT_D",
                                 f"{resource_work}\n({resource_work_unit})")
                elif i == 2:
                    replace_mxcell_value(tree, "RESOURCE_E", 
                               f"RESOURCE:\n{resource_name}\n({resource_unit})")
                    replace_mxcell_value(tree, "RESOURCE_OUT_E",
                                 f"{resource_work}\n({resource_work_unit})")

        replace_mxcell_value(tree, "OPERATIONS", f"OPERATIONS:\n({work_unit})")

    # Write the modified file to disk
    return ET.tostring(tree)


