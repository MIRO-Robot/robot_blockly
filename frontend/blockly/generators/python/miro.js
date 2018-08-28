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
