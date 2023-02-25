# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from audio_file_player/AudioFilePlayFeedback.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class AudioFilePlayFeedback(genpy.Message):
  _md5sum = "8da3f4d23c993ec117df61a7ea32b30c"
  _type = "audio_file_player/AudioFilePlayFeedback"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Feedback about the amount of time the audio has been played
time elapsed_played_time

"""
  __slots__ = ['elapsed_played_time']
  _slot_types = ['time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       elapsed_played_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AudioFilePlayFeedback, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.elapsed_played_time is None:
        self.elapsed_played_time = genpy.Time()
    else:
      self.elapsed_played_time = genpy.Time()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2I().pack(_x.elapsed_played_time.secs, _x.elapsed_played_time.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.elapsed_played_time is None:
        self.elapsed_played_time = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.elapsed_played_time.secs, _x.elapsed_played_time.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.elapsed_played_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2I().pack(_x.elapsed_played_time.secs, _x.elapsed_played_time.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.elapsed_played_time is None:
        self.elapsed_played_time = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.elapsed_played_time.secs, _x.elapsed_played_time.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.elapsed_played_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
