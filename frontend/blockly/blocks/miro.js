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

goog.provide('Blockly.Blocks.miro');
goog.require('Blockly.Blocks');

/**
 * Common HSV hue for all blocks in this category.
 */
// Blockly.Blocks.miro.HUE = 260;

Blockly.Blocks['setup_miro'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Setup Miro")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['move_backward'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Move Backward")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['move_forward'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Move Forward")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['turn_left'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Turn Left")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['turn_right'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Turn Right")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['get_distance'] = {
    init: function() 
    {
        this.appendValueInput("get_distance_var")
            .appendField("Get Distance")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(160);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['lift_neck'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Lift Neck")
            .appendField(new Blockly.FieldDropdown([["Up","L_UP"], ["Down","L_DOWN"], ["Centre","L_CENTRE"]]), "dropdown_lift");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['pitch_neck'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Pitch Neck")
            .appendField(new Blockly.FieldDropdown([["Up","P_UP"], ["Down","P_DOWN"], ["Centre","P_CENTRE"]]), "dropdown_pitch");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['yaw_neck'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Yaw Neck")
            .appendField(new Blockly.FieldDropdown([["Right","Y_RIGHT"], ["Left","Y_LEFT"], ["Centre","Y_CENTRE"]]), "dropdown_yaw");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['capture_image'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Capture Image")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['get_cam_colour'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Get Cam Colour")
            .appendField(new Blockly.FieldColour('#ff0000'), 'colorBGR');
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

