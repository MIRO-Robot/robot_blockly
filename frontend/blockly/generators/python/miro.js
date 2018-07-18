'use strict';

goog.provide('Blockly.Python.miro');
goog.require('Blockly.Python');

Blockly.Python['move_forward'] = function(block) {
  var code = "";
  code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/move_forward.py");
  return code;
};

Blockly.Python['move_backward'] = function(block) {
  var code = "";
  code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/move_backward.py");
  return code;
};

Blockly.Python['turn_right'] = function(block) {
  var code = "";
  code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/turn_right.py");
  return code;
};

Blockly.Python['turn_left'] = function(block) {
  var code = "";
  code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/turn_left.py");
  return code;
};

Blockly.Python['get_distance'] = function(block) {

    var varName = Blockly.Python.valueToCode(block, 'distance', Blockly.Python.ORDER_ATOMIC);

    var code = "";
    code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/get_distance.py");
    return code + varName + " = msg_distance.range\n"

};

//
//
//
// Blockly.Python['caml_colour'] = function(block) {
//
//     var colour_var = block.getFieldValue('COLOUR'); //collect field value for the colour drop down
//     var value_colour_bool = Blockly.Python.valueToCode(block, 'colour_bool', Blockly.Python.ORDER_ATOMIC); //code which is returned
//
//     //set colours to a standard bgr range from 0 to 255
//     var hex = color.replace(/[^0-9A-F]/gi, '');
//     var bigint = parseInt(hex, 16);
//     var r = (bigint >> 16) & 255;
//     var g = (bigint >> 8) & 255;
//     var b = bigint & 255;
//     var colourBGR = [b, g, r].join();
//
//
//
//     var code = "";
//     code += "colorBGR = \"" + colourBGR.toString() + "\"\n";  // bgr variable
//     code += "cam_location = \"caml\"\\n";
//     code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/get_cam_colour.py");
//     return code + value_colour_bool + " = result\n"
//
// };
//
// Blockly.Python['camr_colour'] = function(block) {
//
//     var colour_var = block.getFieldValue('COLOUR'); //collect field value for the colour drop down
//     var value_colour_bool = Blockly.Python.valueToCode(block, 'colour_bool', Blockly.Python.ORDER_ATOMIC); //code which is returned
//
//     //set colours to a standard bgr range from 0 to 255
//     var hex = color.replace(/[^0-9A-F]/gi, '');
//     var bigint = parseInt(hex, 16);
//     var r = (bigint >> 16) & 255;
//     var g = (bigint >> 8) & 255;
//     var b = bigint & 255;
//     var colourBGR = [b, g, r].join();
//
//     var code = "";
//     code += "colorBGR = \"" + colourBGR.toString() + "\"\n";  // bgr variable
//     code += "cam_location = \"camr\"\\n";
//     code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/get_cam_colour.py");
//     return code + value_colour_bool + " = result\n"
//
// };

//
//
// Blockly.Python['test'] = function(block) {
//   // TODO: Assemble Python into code variable.
//   var code = '...\n';
//   return code;
//
// };
//
//
Blockly.Python['neck_yaw'] = function(block) {
  var dropdown_yaw = block.getFieldValue('Yaw');
  var code = '...\n';
  code += "dropdown_yaw = \"" + dropdown_yaw.toString() + "\"\n";
  code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/neck_yaw.py");
  return code;
};

Blockly.Python['neck_lift'] = function(block) {
  var dropdown_lift = block.getFieldValue('Lift');
  var code = '...\n';
  code += "dropdown_lift = \"" + dropdown_yaw.toString() + "\"\n";
  code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/neck_lift.py");
  return code;
};

Blockly.Python['neck_pitch'] = function(block) {
  var dropdown_pitch = block.getFieldValue('Pitch');
  var code = '...\n';
  code += "dropdown_pitch = \"" + dropdown_yaw.toString() + "\"\n";
  code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/neck_pitch.py");
  return code;
};
//
//
// Blockly.Python['sanity_check'] = function(block) {
//   var code = "";
//   code += Blockly.readPythonFile("../blockly/generators/python/scripts/miro/move_forward.py");
//   return code;
// };
//
