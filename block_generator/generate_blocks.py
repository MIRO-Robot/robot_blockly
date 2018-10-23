# Copyright (c) 2018, Cyberselves
# Author: Daniel Camilleri
# All rights reserved.
#!/usr/bin/env python2
import json
import os
import shutil
import sys
from collections import OrderedDict

compressed_flag = False

if len(sys.argv) > 1:
    if sys.argv[1] == "compressed":
        compressed_flag = True

block_notebook_fname = "block_definitions.ipynb"
# block_notebook_fname = "test.ipynb"

python_scripts_fname = "python_scripts"
python_scripts_dest = "../frontend/blockly/generators/python/scripts/miro"

python_js_fname = "python_js.js"
python_js_dest = "../frontend/blockly/generators/python/miro.js"

blocks_js_fname = "blocks_js.js"
blocks_js_dest = "../frontend/blockly/blocks/miro.js"

if compressed_flag:
    with open(os.path.join("blockly_html_p1.txt"), 'r') as b:
        blockly_p1 = b.readlines()
else:
    with open(os.path.join("blockly_html_p1_uncompressed.txt"), 'r') as b:
        blockly_p1 = b.readlines()

with open(os.path.join("blockly_html_p2.txt"), 'r') as b:
    blockly_p2 = b.readlines()

js_header = \
"""/**
 * @license
 *
 * Copyright 2018 Cyberselves
 * http://cyberselves.org
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


/**
 * @fileoverview Blocks for Miro.
 * @author Daniel Camilleri
*/

'use strict';
"""

blocks_js_header = \
"""
goog.provide('Blockly.Blocks.miro');
goog.require('Blockly.Blocks');

/**
 * Common HSV hue for all blocks in this category.
 */
// Blockly.Blocks.miro.HUE = 260;

"""

python_js_header = \
"""
goog.provide('Blockly.Python.miro');
goog.require('Blockly.Python');

"""


def partition(mode, name):
    return "\n#-----------------------------{0} {1}---------------------------------\n".format(mode.upper(), name.upper())


def python_js_template(block_dict, show_image):
    template_p1 = "Blockly.Python['{0}'] = function(block)".format(block_dict["name"])

    if len(block_dict["output"]) > 0:
        return_var = block_dict["output"]["return_var"]
        returns = block_dict["output"]["return_code"]
    else:
        return_var = None

    return_line = "        "
    if return_var is not None:
        block_read_var = "        var varName = Blockly.Python.valueToCode(block, '{0}', " \
                         "Blockly.Python.ORDER_ATOMIC);\n".format(return_var)

        return_line += 'return code + varName + "={0} \\n";'.format(returns)
    else:
        block_read_var = ""
        return_line += "return code;\n\n"

    template_p2 = \
"""        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/{0}.py");\n""".format(block_name)

    params_intro = """        var code = "";\n"""
    template_params = ""

    for in_var in block_dict["inputs"].keys():
        input_var_name = block_dict["inputs"][in_var]["var_name"]
        type = block_dict["inputs"][in_var]["type"]
        if input_var_name is not None:
            if type == "dropdown" or type == "colour_wheel":
                template_params += "        var {0} = block.getFieldValue('{0}');\n".format(input_var_name)
                template_params += '        code += "{0} = \\"" + {0}.toString() + "\\"\\n";\n'.format(input_var_name)
            else:
                template_params += '        var {0} = Blockly.Python.valueToCode(block, "{0}", Blockly.Python.ORDER_ATOMIC);\n'.format(input_var_name)
                template_params += '        code += "{0} = " + {0} + "\\n";\n'.format(input_var_name)


    show_image_str = ""
    if show_image:
        show_image_str = "\n        window.open(\n            '/pages/images/imageViewer.html',\n            " \
                         "'_blank' // <- This is what makes it open in a new window.\n        );\n\n"

    block = template_p1 + "\n    {\n" + show_image_str + block_read_var + params_intro + template_params + \
            template_p2 + return_line + "    };\n\n"
    print block
    return block


def blocks_js_template(block_dict):

    if block_dict["block_colour"] is None:
        block_dict["block_colour"] = 230
    cap_name = " ".join([k.capitalize() for k in block_dict["name"].split("_")])

    template_p1 = "Blockly.Blocks['{0}'] = ".format(block_dict["name"])
    template_p2 = "    init: function() \n"
    template_p4 = \
        """this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour({0});
        this.setTooltip("");
        this.setHelpUrl("");
      """.format(block_dict["block_colour"])


    named = False
    returns_flag = False
    inputs_flag = False

    # Handle outputs
    return_line = "        "
    if len(block_dict["output"]) > 0:
        return_line += """this.appendValueInput("{0}");\n        """.format(block_dict["output"]["return_var"])
        returns_flag = True

    # Handle Inputs
    num_ins = len(block_dict["inputs"])
    interface = ""
    if num_ins > 0:
        named = True
        interface = """        this.appendDummyInput()"""
        interface += """\n            .appendField("{0}")""".format(cap_name)

        for in_var in block_dict["inputs"].keys():
            interface_type = block_dict["inputs"][in_var]["type"]
            if interface_type is not None:
                input_var_name = block_dict["inputs"][in_var]["var_name"]
                if interface_type == "dropdown":
                    input_user_params = block_dict["inputs"][in_var]["user_params"]
                    input_code_params = block_dict["inputs"][in_var]["code_params"]
                    if len(input_user_params) > 0 and len(input_user_params) == len(input_code_params):
                        interface_prt = "            .appendField(new Blockly.FieldDropdown(["
                        for op in range(len(input_user_params)):
                            interface_prt += """["{0}","{1}"], """.format(input_user_params[op], input_code_params[op])
                        if num_ins > 1:
                            interface += """\n            .appendField("{0}")\n""".format(block_dict["inputs"][in_var]["user_name"])
                        else:
                            interface += "\n"
                        interface += interface_prt[:-2] + """]), "{0}")""".format(input_var_name)

                elif interface_type == "colour_wheel" or interface_type == "color_wheel":
                    interface += "\n            .appendField(new Blockly.FieldColour('#ff0000'), '{0}')".format(input_var_name)
                elif interface_type == "number":
                    interface += \
    """\n        this.appendValueInput("{0}")
                   .setCheck("Number")
                   .appendField("{1}")""".format(input_var_name, block_dict["inputs"][in_var]["user_name"])
        interface += ";\n"

    if not named:
        name = """        this.appendDummyInput()\n"""
        name += """            .appendField("{0}");\n""".format(cap_name)
    else:
        name = ""

    block = template_p1 + "{\n" + template_p2 + "    {\n" + name + \
                  interface + return_line + template_p4 + "}\n};\n\n"

    # block_part1 = template_p1 + "{\n" + template_p2 + "    {\n" + name + \
    #               interface + return_line
    #
    # parts = block_part1.split("this.")
    # part1 = parts[:2]
    #
    # part2 =  ""
    # for k in parts[2:]:
    #     part2 += "this." + k
    #
    # block_part1 = "this.".join(part1) + part2.replace("this", "    ")
    #
    # block = block_part1 + template_p4 + "}\n};\n\n"
    print block
    return block


# Empty folders
if os.path.isdir(python_scripts_fname):
    shutil.rmtree(python_scripts_fname)
os.mkdir(python_scripts_fname)

if os.path.isfile(python_js_fname):
    os.remove(python_js_fname)

if os.path.isfile(blocks_js_fname):
    os.remove(blocks_js_fname)

if os.path.isfile("blockly.html"):
    os.remove("blockly.html")

# Prepare js file headers
with open(os.path.join(blocks_js_fname), 'a') as b:
    b.writelines(js_header + blocks_js_header)

with open(os.path.join(python_js_fname), 'a') as b:
    b.writelines(js_header + python_js_header)

# Load Definitions Notebook and read cells
with open(block_notebook_fname, 'r') as f:
    nb = json.loads(f.read())

cells = nb["cells"]

# Cell number 1 is always
# import rospy
# rospy.init_node('blockly_server', anonymous=True)
# So notebook can be used to test code with gazebo before compiling

blocks_dict = OrderedDict()
group_colours = []

if len(cells) > 1:
    for c in cells[1:]:
        return_code = None
        return_var_name = None
        user_interface = None
        input_var_name = None
        input_params_list = None
        input_vars_list = None
        block_color = None
        show_image_flag = False

        if c["cell_type"] == "code":
            src_code = c["source"]
            # Functions defined with 'def' are the ones extracted into blocks. This leaves developer free to test
            # and call blocks of code
            # A cell containing a function MUST ONLY contain ONE function definition
            def_lnum = [n for n, j in enumerate(src_code) if "def " in j]
            if len(def_lnum) == 1:
                def_lnum = def_lnum[0]
                def_parts = src_code[def_lnum].split("def ")[1].split("(")
                block_name = def_parts[0]

                blocks_dict[block_name] = dict()
                blocks_dict[block_name]["name"] = block_name
                blocks_dict[block_name]["block_group"] = "Miro"
                blocks_dict[block_name]["block_colour"] = None
                blocks_dict[block_name]["group_colour"] = None
                blocks_dict[block_name]["inputs"] = OrderedDict()
                blocks_dict[block_name]["output"] = dict()
                input_counter = 0

                if def_parts[1] != "):\n":
                    input_var_names = def_parts[1].split(")")[0].split(", ")

                # Create script
                with open(os.path.join(python_scripts_fname, block_name + ".py"), 'a') as b:
                    unindented_code = []
                    unindented_code.append(partition("start", block_name))
                    for k in src_code:
                        if "return " in k:
                            return_code = k.split("return ")[1]
                            return_var_name = block_name + "_var"
                            blocks_dict[block_name]["output"]["return_code"] = return_code
                            blocks_dict[block_name]["output"]["return_var"] = return_var_name
                        elif "Interface:" in k and "#" in k:
                            user_interface = k.split("Interface:")[1].replace(" ", "").replace("\n", "")
                            blocks_dict[block_name]["inputs"][str(input_counter)] = dict()
                            blocks_dict[block_name]["inputs"][str(input_counter)]["var_name"] = input_var_names[0]
                            input_var_names.pop(0)
                            blocks_dict[block_name]["inputs"][str(input_counter)]["type"] = user_interface
                            input_counter += 1
                        elif "InterfaceName:" in k and "#" in k:
                            username = k.split("InterfaceName:")[1].replace(" ", "").replace("\n", "")
                            blocks_dict[block_name]["inputs"][str(input_counter-1)]["user_name"] = username.replace("_", " ")
                        elif "Parameters:" in k and "#" in k:
                            if user_interface == "dropdown" or user_interface == "checkbox":
                                if "UserParameters" in k:
                                    input_params_list = k.split("UserParameters:")[1] \
                                                            .replace(" ", "").replace("\n", "")[1:-1].split(",")
                                    blocks_dict[block_name]["inputs"][str(input_counter-1)]["user_params"] = input_params_list
                                elif "CodeParameters" in k:
                                    input_vars_list = k.split("CodeParameters:")[1] \
                                                            .replace(" ", "").replace("\n", "")[1:-1].split(",")
                                    blocks_dict[block_name]["inputs"][str(input_counter-1)]["code_params"] = input_vars_list
                            elif user_interface is None:
                                raise TypeError("Specify Interface before Parameters")
                            else:
                                raise ValueError(str(user_interface) + "not yet supported")
                        elif "GroupColour:" in k and "#" in k:
                            try:
                                blocks_dict[block_name]["group_colour"] = int(k.split("GroupColour:")[1].replace(" ", "").replace("\n", ""))
                            except Exception as e:
                                pass
                        elif "GroupColor:" in k and "#" in k:
                            try:
                                blocks_dict[block_name]["group_colour"] = int(k.split("GroupColor:")[1].replace(" ", "").replace("\n", ""))
                            except Exception as e:
                                pass
                        elif "Group:" in k and "#" in k:
                            try:
                                blocks_dict[block_name]["block_group"] = k.split("Group:")[1].replace(" ", "").replace("\n", "").replace("_", " ")
                            except Exception as e:
                                pass
                        elif "Colour:" in k and "#" in k:
                            try:
                                blocks_dict[block_name]["block_colour"] = int(k.split("Colour:")[1].replace(" ", "").replace("\n", ""))
                            except Exception as e:
                                block_color = None
                        elif "def " in k and "(" in k and "):" in k or "global" in k:
                            pass
                        elif "# Show Image" in k:
                            show_image_flag = True
                        elif k != "\n":
                            unindented_code.append(k[4:])
                        else:
                            unindented_code.append(k)
                    unindented_code.append(partition("end", block_name))
                    b.writelines(unindented_code)

                # Append to blocks_js
                with open(os.path.join(blocks_js_fname), 'a') as b:
                    b.writelines(blocks_js_template(block_dict=blocks_dict[block_name]))

                # Append to python_js
                with open(os.path.join(python_js_fname), 'a') as b:
                    b.writelines(python_js_template(block_dict=blocks_dict[block_name],
                                                    show_image=show_image_flag))
    last_group = None

    processed_groups = OrderedDict()
    for k in blocks_dict:
        this_group = blocks_dict[k]["block_group"]
        group_colour = blocks_dict[k]["group_colour"]
        if group_colour is not None and this_group not in processed_groups.keys():
            processed_groups[this_group] = dict()
            processed_groups[this_group]["blocks"] = []
            processed_groups[this_group]["colour"] = group_colour
            for g in blocks_dict:
                if blocks_dict[g]["block_group"] == this_group:
                    processed_groups[this_group]["blocks"].append(g)
                    blocks_dict[g]["group_colour"] = group_colour

    with open(os.path.join("blockly.html"), 'a') as b:
        b.writelines(blockly_p1)
        for g in processed_groups:
            b.write('        <category id="{1}" name="{0}" colour="{2}">\n'.format(g,
                                                                                   g.lower(),
                                                                                   processed_groups[g]["colour"] ))
            for n in processed_groups[g]["blocks"]:
                b.write('            <block type="{0}"></block>\n'.format(n))
            b.write('        </category>\n')
        b.writelines(blockly_p2)

    shutil.copy(python_js_fname, python_js_dest)
    shutil.copy(blocks_js_fname, blocks_js_dest)
    shutil.rmtree(python_scripts_dest)
    shutil.copytree(python_scripts_fname, python_scripts_dest)
    shutil.copy("blockly.html", "../frontend/pages/blockly.html")
    print "Finished Compiling Blocks"
