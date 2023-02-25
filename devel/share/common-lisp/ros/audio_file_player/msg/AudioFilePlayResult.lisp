; Auto-generated. Do not edit!


(cl:in-package audio_file_player-msg)


;//! \htmlinclude AudioFilePlayResult.msg.html

(cl:defclass <AudioFilePlayResult> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (reason
    :reader reason
    :initarg :reason
    :type cl:string
    :initform "")
   (total_time
    :reader total_time
    :initarg :total_time
    :type cl:real
    :initform 0))
)

(cl:defclass AudioFilePlayResult (<AudioFilePlayResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AudioFilePlayResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AudioFilePlayResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name audio_file_player-msg:<AudioFilePlayResult> is deprecated: use audio_file_player-msg:AudioFilePlayResult instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <AudioFilePlayResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader audio_file_player-msg:success-val is deprecated.  Use audio_file_player-msg:success instead.")
  (success m))

(cl:ensure-generic-function 'reason-val :lambda-list '(m))
(cl:defmethod reason-val ((m <AudioFilePlayResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader audio_file_player-msg:reason-val is deprecated.  Use audio_file_player-msg:reason instead.")
  (reason m))

(cl:ensure-generic-function 'total_time-val :lambda-list '(m))
(cl:defmethod total_time-val ((m <AudioFilePlayResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader audio_file_player-msg:total_time-val is deprecated.  Use audio_file_player-msg:total_time instead.")
  (total_time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AudioFilePlayResult>) ostream)
  "Serializes a message object of type '<AudioFilePlayResult>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'reason))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'reason))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'total_time)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'total_time) (cl:floor (cl:slot-value msg 'total_time)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AudioFilePlayResult>) istream)
  "Deserializes a message object of type '<AudioFilePlayResult>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'reason) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'reason) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'total_time) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AudioFilePlayResult>)))
  "Returns string type for a message object of type '<AudioFilePlayResult>"
  "audio_file_player/AudioFilePlayResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AudioFilePlayResult)))
  "Returns string type for a message object of type 'AudioFilePlayResult"
  "audio_file_player/AudioFilePlayResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AudioFilePlayResult>)))
  "Returns md5sum for a message object of type '<AudioFilePlayResult>"
  "63da86c1ec3bfb8b78f7e875747b385b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AudioFilePlayResult)))
  "Returns md5sum for a message object of type 'AudioFilePlayResult"
  "63da86c1ec3bfb8b78f7e875747b385b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AudioFilePlayResult>)))
  "Returns full string definition for message of type '<AudioFilePlayResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result information~%# If it was successful~%bool success~%# If it wasn't reason why it wasn't~%string reason~%# Total time the file was playing~%time total_time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AudioFilePlayResult)))
  "Returns full string definition for message of type 'AudioFilePlayResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result information~%# If it was successful~%bool success~%# If it wasn't reason why it wasn't~%string reason~%# Total time the file was playing~%time total_time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AudioFilePlayResult>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'reason))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AudioFilePlayResult>))
  "Converts a ROS message object to a list"
  (cl:list 'AudioFilePlayResult
    (cl:cons ':success (success msg))
    (cl:cons ':reason (reason msg))
    (cl:cons ':total_time (total_time msg))
))
