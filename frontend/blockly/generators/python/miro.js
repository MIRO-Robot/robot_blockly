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
