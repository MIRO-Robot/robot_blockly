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
 * @author Daniel Camilleri, Natalie Wood
*/

'use strict';

goog.provide('Blockly.Python.miro');
goog.require('Blockly.Python');

Blockly.Python['setup_miro'] = function(block)
    {
        var code = "";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/setup_miro.py");
        return code;
    };

Blockly.Python['move_backward'] = function(block)
    {
        var code = "";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/move_backward.py");
        return code;
    };

Blockly.Python['move_forward'] = function(block)
    {
        var code = "";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/move_forward.py");
        return code;
    };

Blockly.Python['turn_left'] = function(block)
    {
        var code = "";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/turn_left.py");
        return code;
    };

Blockly.Python['turn_right'] = function(block)
    {
        var code = "";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/turn_right.py");
        return code;
    };

Blockly.Python['get_distance'] = function(block)
    {
        var varName = Blockly.Python.valueToCode(block, 'get_distance_var', Blockly.Python.ORDER_ATOMIC);
        var code = "";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/get_distance.py");
        return code + varName + msg_distance.range;
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

Blockly.Python['capture_image'] = function(block)
    {

        window.open(
            '/pages/images/imageViewer.html',
            '_blank' // <- This is what makes it open in a new window.
        );

        var code = "";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/capture_image.py");
        return code;
    };

Blockly.Python['get_cam_colour'] = function(block)
    {
        var code = "";
        var colorBGR = block.getFieldValue('colorBGR');
        code += "colorBGR = \"" + colorBGR.toString() + "\"\n";
        code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/get_cam_colour.py");
        return code;
    };

