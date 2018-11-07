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
            .appendField(new Blockly.FieldDropdown([["Simulation","sim"], ["Physical","physical"]]), "miro_type");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip('Inputs: Dropdown choice of physical or simulated \n' + 
                        'robot | Output: None \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['move_distance'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Move Distance")
            .appendField("Direction")
            .appendField(new Blockly.FieldDropdown([["Forward","forward"], ["Backward","backward"]]), "direction")
        this.appendValueInput("velocity")
                   .setCheck("Number")
                   .appendField("Velocity")
        this.appendValueInput("duration")
                   .setCheck("Number")
                   .appendField("Duration");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip('Inputs: Dropdown choice of direction (Forward or \n' + 
                        'Backward). Floating point input velocity in \n' + 
                        'metres/s. Floating point duration in seconds | \n' + 
                        'Output: None \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['turn_angle'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Turn Angle")
            .appendField("Direction")
            .appendField(new Blockly.FieldDropdown([["Clockwise","clockwise"], ["Anti-Clockwise","anticlockwise"]]), "direction")
        this.appendValueInput("angular_velocity")
                   .setCheck("Number")
                   .appendField("Velocity")
        this.appendValueInput("duration")
                   .setCheck("Number")
                   .appendField("Duration");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip('Inputs: Dropdown choice of direction (Clockwise \n' + 
                        'or Anticlockwise). Floating point input velocity \n' + 
                        'in radians/s. Floating point duration in seconds \n' + 
                        '| Output: None \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['lift_neck'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Lift Neck")
            .appendField(new Blockly.FieldDropdown([["Up","L_UP"], ["Down","L_DOWN"], ["Centre","L_CENTRE"]]), "dropdown_lift");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip('Inputs: Dropdown choice of  Up, Down or Centre \n' + 
                        'that changes the head height | Output: None \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['pitch_neck'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Pitch Neck")
            .appendField(new Blockly.FieldDropdown([["Up","P_UP"], ["Down","P_DOWN"], ["Centre","P_CENTRE"]]), "dropdown_pitch");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip('Inputs: Dropdown choice of  Up, Down or Centre \n' + 
                        'that changes the head pitch | Output: None \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['yaw_neck'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Yaw Neck")
            .appendField(new Blockly.FieldDropdown([["Right","Y_RIGHT"], ["Left","Y_LEFT"], ["Centre","Y_CENTRE"]]), "dropdown_yaw");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip('Inputs: Dropdown choice of  Right, Left or Centre \n' + 
                        'that changes the head yaw | Output: None \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['wag_tail'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Wag Tail")
            .appendField(new Blockly.FieldDropdown([["Droop","Droop"], ["Neutral","Neutral"], ["Wagging","Wagging"]]), "dropdown_wag");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip('Inputs: Dropdown choice of  Droop, Neutral or \n' + 
                        'Wagging that changes the activity of the tail | \n' + 
                        'Output: None \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['move_ears'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Move Ears")
            .appendField("Group")
            .appendField(new Blockly.FieldDropdown([["Left","Left"], ["Right","Right"], ["Both","Both"]]), "ears_group")
            .appendField("Direction")
            .appendField(new Blockly.FieldDropdown([["Forward","Forward"], ["Sideways","Sideways"]]), "ears_direction");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip('Inputs: Dropdown choice of ear group (Left, Right \n' + 
                        'or Both) and ear direction (Forwards, Sideways) \n' + 
                        'to control ear movements| Output: None \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['get_distance'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Get Distance");
        this.appendValueInput("get_distance_var");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(160);
        this.setTooltip('Inputs: None | Output: Returns the distance in \n' + 
                        'metres from the nose to the closest object using \n' + 
                        'ultrasound \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['get_colour_pixels'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Get Colour Pixels")
            .appendField(new Blockly.FieldColour('#ff0000'), 'hex_string');
        this.appendValueInput("get_colour_pixels_var");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip('Inputs: Colour to search | Method: Stitches input \n' + 
                        'from both cameras and counts number of pixels \n' + 
                        'that are of the same input colour| Output: \n' + 
                        'Returns a positive value from 0 to 1 which is a \n' + 
                        'percentage of same coloured pixels with the field \n' + 
                        'of view \n');
        this.setHelpUrl("");
      }
};

Blockly.Blocks['get_colour_direction'] = {
    init: function() 
    {
        this.appendDummyInput()
            .appendField("Get Colour Direction")
            .appendField(new Blockly.FieldColour('#ff0000'), 'hex_string');
        this.appendValueInput("get_colour_direction_var");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip('Inputs: Colour to search | Method: Stitches input \n' + 
                        'from both cameras and finds the orientation of \n' + 
                        'the largest amount with respect to robot head | \n' + 
                        'Returns: Integer value representing direction of \n' + 
                        'colour. -1 to indicate left, 0 to indicate \n' + 
                        'straight ahead and 1 to indicate right.    \n');
        this.setHelpUrl("");
      }
};

