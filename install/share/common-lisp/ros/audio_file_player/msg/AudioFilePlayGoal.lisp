; Auto-generated. Do not edit!


(cl:in-package audio_file_player-msg)


;//! \htmlinclude AudioFilePlayGoal.msg.html

(cl:defclass <AudioFilePlayGoal> (roslisp-msg-protocol:ros-message)
  ((filepath
    :reader filepath
    :initarg :filepath
    :type cl:string
    :initform ""))
)

(cl:defclass AudioFilePlayGoal (<AudioFilePlayGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AudioFilePlayGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AudioFilePlayGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name audio_file_player-msg:<AudioFilePlayGoal> is deprecated: use audio_file_player-msg:AudioFilePlayGoal instead.")))

(cl:ensure-generic-function 'filepath-val :lambda-list '(m))
(cl:defmethod filepath-val ((m <AudioFilePlayGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader audio_file_player-msg:filepath-val is deprecated.  Use audio_file_player-msg:filepath instead.")
  (filepath m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AudioFilePlayGoal>) ostream)
  "Serializes a message object of type '<AudioFilePlayGoal>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'filepath))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'filepath))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AudioFilePlayGoal>) istream)
  "Deserializes a message object of type '<AudioFilePlayGoal>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'filepath) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'filepath) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AudioFilePlayGoal>)))
  "Returns string type for a message object of type '<AudioFilePlayGoal>"
  "audio_file_player/AudioFilePlayGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AudioFilePlayGoal)))
  "Returns string type for a message object of type 'AudioFilePlayGoal"
  "audio_file_player/AudioFilePlayGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AudioFilePlayGoal>)))
  "Returns md5sum for a message object of type '<AudioFilePlayGoal>"
  "5ef967a25f780d4a216c15b3834dca97")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AudioFilePlayGoal)))
  "Returns md5sum for a message object of type 'AudioFilePlayGoal"
  "5ef967a25f780d4a216c15b3834dca97")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AudioFilePlayGoal>)))
  "Returns full string definition for message of type '<AudioFilePlayGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Path to the audio file~%string filepath~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AudioFilePlayGoal)))
  "Returns full string definition for message of type 'AudioFilePlayGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Path to the audio file~%string filepath~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AudioFilePlayGoal>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'filepath))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AudioFilePlayGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'AudioFilePlayGoal
    (cl:cons ':filepath (filepath msg))
))
