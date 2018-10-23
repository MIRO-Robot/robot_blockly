/**
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

goog.provide('Blockly.Python.miro');
goog.require('Blockly.Python');

Blockly.Python['setup_miro'] = function(block)
    {
        var code = "";
        var miro_type = block.getFieldValue('miro_type');
        code += "miro_type = \"" + miro_type.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/setup_miro.py");
        return code;

    };

Blockly.Python['move_distance'] = function(block)
    {
        var code = "";
        var direction = block.getFieldValue('direction');
        code += "direction = \"" + direction.toString() + "\"\n";
        var velocity = Blockly.Python.valueToCode(block, "velocity", Blockly.Python.ORDER_ATOMIC);
        code += "velocity = " + velocity + "\n";
        var duration = Blockly.Python.valueToCode(block, "duration", Blockly.Python.ORDER_ATOMIC);
        code += "duration = " + duration + "\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/move_distance.py");
        return code;

    };

Blockly.Python['turn_angle'] = function(block)
    {
        var code = "";
        var direction = block.getFieldValue('direction');
        code += "direction = \"" + direction.toString() + "\"\n";
        var angular_velocity = Blockly.Python.valueToCode(block, "angular_velocity", Blockly.Python.ORDER_ATOMIC);
        code += "angular_velocity = " + angular_velocity + "\n";
        var duration = Blockly.Python.valueToCode(block, "duration", Blockly.Python.ORDER_ATOMIC);
        code += "duration = " + duration + "\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/turn_angle.py");
        return code;

    };

Blockly.Python['lift_neck'] = function(block)
    {
        var code = "";
        var dropdown_lift = block.getFieldValue('dropdown_lift');
        code += "dropdown_lift = \"" + dropdown_lift.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/lift_neck.py");
        return code;

    };

Blockly.Python['pitch_neck'] = function(block)
    {
        var code = "";
        var dropdown_pitch = block.getFieldValue('dropdown_pitch');
        code += "dropdown_pitch = \"" + dropdown_pitch.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/pitch_neck.py");
        return code;

    };

Blockly.Python['yaw_neck'] = function(block)
    {
        var code = "";
        var dropdown_yaw = block.getFieldValue('dropdown_yaw');
        code += "dropdown_yaw = \"" + dropdown_yaw.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/yaw_neck.py");
        return code;

    };

Blockly.Python['wag_tail'] = function(block)
    {
        var code = "";
        var dropdown_wag = block.getFieldValue('dropdown_wag');
        code += "dropdown_wag = \"" + dropdown_wag.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/wag_tail.py");
        return code;

    };

Blockly.Python['move_ears'] = function(block)
    {
        var code = "";
        var ears_group = block.getFieldValue('ears_group');
        code += "ears_group = \"" + ears_group.toString() + "\"\n";
        var ears_direction = block.getFieldValue('ears_direction');
        code += "ears_direction = \"" + ears_direction.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/move_ears.py");
        return code;

    };

Blockly.Python['get_distance'] = function(block)
    {
        var varName = Blockly.Python.valueToCode(block, 'get_distance_var', Blockly.Python.ORDER_ATOMIC);
        var code = "";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/get_distance.py");
        return code + varName + "=msg_distance.range \n";    };

Blockly.Python['get_colour_pixels'] = function(block)
    {
        var varName = Blockly.Python.valueToCode(block, 'get_colour_pixels_var', Blockly.Python.ORDER_ATOMIC);
        var code = "";
        var hex_string = block.getFieldValue('hex_string');
        code += "hex_string = \"" + hex_string.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/get_colour_pixels.py");
        return code + varName + "=result \n";    };

Blockly.Python['get_colour_direction'] = function(block)
    {
        var varName = Blockly.Python.valueToCode(block, 'get_colour_direction_var', Blockly.Python.ORDER_ATOMIC);
        var code = "";
        var hex_string = block.getFieldValue('hex_string');
        code += "hex_string = \"" + hex_string.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/get_colour_direction.py");
        return code + varName + "=result \n";    };

