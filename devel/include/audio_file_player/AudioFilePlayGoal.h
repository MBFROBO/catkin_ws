// Generated by gencpp from file audio_file_player/AudioFilePlayGoal.msg
// DO NOT EDIT!


#ifndef AUDIO_FILE_PLAYER_MESSAGE_AUDIOFILEPLAYGOAL_H
#define AUDIO_FILE_PLAYER_MESSAGE_AUDIOFILEPLAYGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace audio_file_player
{
template <class ContainerAllocator>
struct AudioFilePlayGoal_
{
  typedef AudioFilePlayGoal_<ContainerAllocator> Type;

  AudioFilePlayGoal_()
    : filepath()  {
    }
  AudioFilePlayGoal_(const ContainerAllocator& _alloc)
    : filepath(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _filepath_type;
  _filepath_type filepath;





  typedef boost::shared_ptr< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> const> ConstPtr;

}; // struct AudioFilePlayGoal_

typedef ::audio_file_player::AudioFilePlayGoal_<std::allocator<void> > AudioFilePlayGoal;

typedef boost::shared_ptr< ::audio_file_player::AudioFilePlayGoal > AudioFilePlayGoalPtr;
typedef boost::shared_ptr< ::audio_file_player::AudioFilePlayGoal const> AudioFilePlayGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator1> & lhs, const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator2> & rhs)
{
  return lhs.filepath == rhs.filepath;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator1> & lhs, const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace audio_file_player

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5ef967a25f780d4a216c15b3834dca97";
  }

  static const char* value(const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5ef967a25f780d4aULL;
  static const uint64_t static_value2 = 0x216c15b3834dca97ULL;
};

template<class ContainerAllocator>
struct DataType< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "audio_file_player/AudioFilePlayGoal";
  }

  static const char* value(const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Path to the audio file\n"
"string filepath\n"
;
  }

  static const char* value(const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.filepath);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AudioFilePlayGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::audio_file_player::AudioFilePlayGoal_<ContainerAllocator>& v)
  {
    s << indent << "filepath: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.filepath);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AUDIO_FILE_PLAYER_MESSAGE_AUDIOFILEPLAYGOAL_H
