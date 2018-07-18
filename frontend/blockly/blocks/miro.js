'use strict';

goog.provide('Blockly.Blocks.miro');

goog.require('Blockly.Blocks');


Blockly.Blocks['move_forward'] = {
  init: function() {
    this.appendDummyInput()
	.appendField("Move Forward");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['move_backward'] = {
  init: function() {
    this.appendDummyInput()
	.appendField("Move Backward");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['turn_right'] = {
  init: function() {
    this.appendDummyInput()
	.appendField("Turn Right");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['turn_left'] = {
  init: function() {
    this.appendDummyInput()
	.appendField("Turn Left");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['get_distance'] = {
  init: function() {
    this.appendValueInput("distance")
        .appendField("Distance");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(0);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};




// Original code -- may not work

// Blockly.Blocks['caml_colour'] = {
//   init: function() {
//     this.appendDummyInput()
//         .appendField("Left camera colour")
//         .appendField(new Blockly.FieldColour("#ff0000"), "COLOR");
//     this.appendValueInput("colour_bool")
//         .setCheck(null)
//         .appendField("matches colour");
//     this.setPreviousStatement(true, null);
//     this.setNextStatement(true, null);
//     this.setColour(0);
//     this.setTooltip('');
//     this.setHelpUrl('');
//   }
// };
//
// Blockly.Blocks['camr_colour'] = {
//   init: function() {
//     this.appendDummyInput()
//         .appendField("Right camera colour")
//         .appendField(new Blockly.FieldColour("#ff0000"), "COLOR");
//     this.appendValueInput("colour_bool")
//         .setCheck(null)
//         .appendField("matches colour");
//     this.setPreviousStatement(true, null);
//     this.setNextStatement(true, null);
//     this.setColour(0);
//     this.setTooltip('');
//     this.setHelpUrl('');
//   }
// };
//







// Newer code - hopefully works

//
//
// Blockly.Blocks['caml_colour'] = {
//   init: function() {
//     this.appendDummyInput()
//         .appendField("Left camera colour")
//         .appendField(new Blockly.FieldColour("#ff0000"), "COLOUR");
//     this.setOutput(true, "Boolean");
//     this.setColour(230);
//  this.setTooltip("");
//  this.setHelpUrl("");
//   }
// };
//
// Blockly.Blocks['camr_colour'] = {
//   init: function() {
//     this.appendDummyInput()
//     this.setTooltip("");
//         .appendField("Right camera colour")
//         .appendField(new Blockly.FieldColour("#ff0000"), "COLOUR");
//     this.setOutput(true, "Boolean");
//     this.setColour(230);
//  this.setHelpUrl("");
//   }
// };
//
// Blockly.Blocks['test'] = {
//   init: function() {
//     this.appendDummyInput()
//         .appendField("TESTING EMPTY BLOCK");
//     this.setColour(230);
//  this.setTooltip("");
//  this.setHelpUrl("");
//   }
// };
//
//
//
//
//
Blockly.Blocks['neck_yaw'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Neck yaw")
        .appendField(new Blockly.FieldDropdown([["Left","Y_LEFT"], ["Center","Y_CENTER"], ["Right","Y_RIGHT"]]), "Yaw");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['neck_lift'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Neck lift")
        .appendField(new Blockly.FieldDropdown([["Up","L_UP"], ["Center","L_CENTER"], ["Down","L_DOWN"]]), "Lift");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['neck_pitch'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Neck pitch")
        .appendField(new Blockly.FieldDropdown([["Up","P_UP"], ["Center","P_CENTER"], ["Down","P_DOWN"]]), "Pitch");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};
//
//
//
//
//
// Blockly.Blocks['sanity_check'] = {
//   init: function() {
//     this.appendDummyInput()
// 	.appendField("Move Forward");
//     this.setPreviousStatement(true);
//     this.setNextStatement(true);
//     this.setTooltip('');
//     this.setHelpUrl('http://www.example.com/');
//   }
// };
