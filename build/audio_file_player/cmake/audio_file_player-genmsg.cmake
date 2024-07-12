# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "audio_file_player: 7 messages, 0 services")

set(MSG_I_FLAGS "-Iaudio_file_player:/home/robot/catkin_ws/devel/share/audio_file_player/msg;-Iactionlib_msgs:/opt/ros/noetic/share/actionlib_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(audio_file_player_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg" NAME_WE)
add_custom_target(_audio_file_player_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "audio_file_player" "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg" "audio_file_player/AudioFilePlayActionGoal:std_msgs/Header:audio_file_player/AudioFilePlayActionResult:actionlib_msgs/GoalID:audio_file_player/AudioFilePlayGoal:audio_file_player/AudioFilePlayActionFeedback:audio_file_player/AudioFilePlayResult:audio_file_player/AudioFilePlayFeedback:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg" NAME_WE)
add_custom_target(_audio_file_player_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "audio_file_player" "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg" "actionlib_msgs/GoalID:std_msgs/Header:audio_file_player/AudioFilePlayGoal"
)

get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg" NAME_WE)
add_custom_target(_audio_file_player_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "audio_file_player" "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg" "actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus:audio_file_player/AudioFilePlayResult"
)

get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg" NAME_WE)
add_custom_target(_audio_file_player_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "audio_file_player" "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg" "actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus:audio_file_player/AudioFilePlayFeedback"
)

get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg" NAME_WE)
add_custom_target(_audio_file_player_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "audio_file_player" "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg" ""
)

get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg" NAME_WE)
add_custom_target(_audio_file_player_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "audio_file_player" "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg" ""
)

get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg" NAME_WE)
add_custom_target(_audio_file_player_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "audio_file_player" "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg"
  "${MSG_I_FLAGS}"
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
)
_generate_msg_cpp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
)
_generate_msg_cpp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
)
_generate_msg_cpp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
)
_generate_msg_cpp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
)
_generate_msg_cpp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
)
_generate_msg_cpp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
)

### Generating Services

### Generating Module File
_generate_module_cpp(audio_file_player
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(audio_file_player_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(audio_file_player_generate_messages audio_file_player_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_cpp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_cpp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_cpp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_cpp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_cpp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_cpp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_cpp _audio_file_player_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(audio_file_player_gencpp)
add_dependencies(audio_file_player_gencpp audio_file_player_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS audio_file_player_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg"
  "${MSG_I_FLAGS}"
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
)
_generate_msg_eus(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
)
_generate_msg_eus(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
)
_generate_msg_eus(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
)
_generate_msg_eus(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
)
_generate_msg_eus(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
)
_generate_msg_eus(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
)

### Generating Services

### Generating Module File
_generate_module_eus(audio_file_player
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(audio_file_player_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(audio_file_player_generate_messages audio_file_player_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_eus _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_eus _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_eus _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_eus _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_eus _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_eus _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_eus _audio_file_player_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(audio_file_player_geneus)
add_dependencies(audio_file_player_geneus audio_file_player_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS audio_file_player_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg"
  "${MSG_I_FLAGS}"
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
)
_generate_msg_lisp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
)
_generate_msg_lisp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
)
_generate_msg_lisp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
)
_generate_msg_lisp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
)
_generate_msg_lisp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
)
_generate_msg_lisp(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
)

### Generating Services

### Generating Module File
_generate_module_lisp(audio_file_player
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(audio_file_player_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(audio_file_player_generate_messages audio_file_player_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_lisp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_lisp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_lisp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_lisp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_lisp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_lisp _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_lisp _audio_file_player_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(audio_file_player_genlisp)
add_dependencies(audio_file_player_genlisp audio_file_player_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS audio_file_player_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg"
  "${MSG_I_FLAGS}"
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
)
_generate_msg_nodejs(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
)
_generate_msg_nodejs(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
)
_generate_msg_nodejs(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
)
_generate_msg_nodejs(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
)
_generate_msg_nodejs(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
)
_generate_msg_nodejs(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
)

### Generating Services

### Generating Module File
_generate_module_nodejs(audio_file_player
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(audio_file_player_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(audio_file_player_generate_messages audio_file_player_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_nodejs _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_nodejs _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_nodejs _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_nodejs _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_nodejs _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_nodejs _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_nodejs _audio_file_player_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(audio_file_player_gennodejs)
add_dependencies(audio_file_player_gennodejs audio_file_player_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS audio_file_player_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg"
  "${MSG_I_FLAGS}"
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
)
_generate_msg_py(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
)
_generate_msg_py(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
)
_generate_msg_py(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
)
_generate_msg_py(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
)
_generate_msg_py(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
)
_generate_msg_py(audio_file_player
  "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
)

### Generating Services

### Generating Module File
_generate_module_py(audio_file_player
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(audio_file_player_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(audio_file_player_generate_messages audio_file_player_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayAction.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_py _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_py _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_py _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayActionFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_py _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayGoal.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_py _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayResult.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_py _audio_file_player_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robot/catkin_ws/devel/share/audio_file_player/msg/AudioFilePlayFeedback.msg" NAME_WE)
add_dependencies(audio_file_player_generate_messages_py _audio_file_player_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(audio_file_player_genpy)
add_dependencies(audio_file_player_genpy audio_file_player_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS audio_file_player_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/audio_file_player
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(audio_file_player_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/audio_file_player
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(audio_file_player_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/audio_file_player
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(audio_file_player_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/audio_file_player
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(audio_file_player_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/audio_file_player
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(audio_file_player_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
