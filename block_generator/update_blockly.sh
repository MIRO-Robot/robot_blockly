#!/usr/bin/env bash

if [ $1 = "generate" ]
then
	if [ $2 = "compressed" ]
	then
		cd $SRC_FOLDER/blockly_ws/src/robot_blockly/block_generator && python generate_blocks.py compressed
		cd $SRC_FOLDER/blockly_ws/src/robot_blockly/frontend/blockly/ && python build.py compressed
	else
		cd $SRC_FOLDER/blockly_ws/src/robot_blockly/block_generator && python generate_blocks.py uncompressed
		cd $SRC_FOLDER/blockly_ws/src/robot_blockly/frontend/blockly/ && python build.py uncompressed
	fi
fi

cd $SRC_FOLDER/blockly_ws
catkin_make_isolated -j4 --pkg robot_blockly --install

source $SRC_FOLDER/blockly_ws/install_isolated/setup.bash
export PYTHONPATH=/usr/local/lib/python3.5/dist-packages/cv2:$MIRO_PATH_MDK/share:$PYTHONPATH
#export ROS_IP=192.168.1.3
roslaunch robot_blockly robot_blockly.launch
