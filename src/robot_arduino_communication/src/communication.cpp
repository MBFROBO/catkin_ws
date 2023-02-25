#include "servo_angle_restrictions.h"
#include "ros/ros.h"
#include "std_msgs/UInt8MultiArray.h"
#include "std_msgs/Int8.h"
#include "std_msgs/String.h"

uint8_t flag_on_off = 0;
uint8_t flag_on = 0;
uint8_t flag_move_mouth = 0;
uint8_t flag_state_mouth = 0;

ros::Time now_time;

void on_off(const std_msgs::Int8::ConstPtr& msg) {
    if (flag_on_off != msg->data) {
        flag_on_off = msg->data;
        flag_on = 1;
        flag_move_mouth = 1;
        now_time = ros::Time::now();
    } 
}

int main(int argc, char **argv) {

    ros::init(argc, argv, "robot_servo_communication");
    ros::NodeHandle nh;

    ros::Subscriber sub_on_off = nh.subscribe("/on_off", 1000, on_off);
    ros::Publisher play_audio = nh.advertise<std_msgs::String>("/audio_file_player/play", 1000);
    ros::Publisher right_arm = nh.advertise<std_msgs::UInt8MultiArray>("/right_arm", 1000);
    ros::Publisher right_shoulder = nh.advertise<std_msgs::UInt8MultiArray>("/right_shoulder", 1000);
    ros::Publisher head = nh.advertise<std_msgs::UInt8MultiArray>("/head", 1000);
    ros::Publisher neck = nh.advertise<std_msgs::UInt8MultiArray>("/neck", 1000);
    ros::Rate loop_rate(20);

    std_msgs::UInt8MultiArray data_right_arm;
    data_right_arm.layout.dim.clear();
    // data_right_arm.data.resize(6);
    data_right_arm.data.push_back(RHAND_FINGER_1_MAX);
    data_right_arm.data.push_back(RHAND_FINGER_2_MAX);
    data_right_arm.data.push_back(RHAND_FINGER_3_MAX);
    data_right_arm.data.push_back(RHAND_FINGER_4_MAX);
    data_right_arm.data.push_back(RHAND_FINGER_5_MAX);
    data_right_arm.data.push_back(RHAND_WRIST_MID);

    std_msgs::UInt8MultiArray data_right_shoulder;
    data_right_shoulder.layout.dim.clear();
    data_right_shoulder.data.push_back(RHAND_BICEPS_MID);
    data_right_shoulder.data.push_back(RSHOUL_ROTAT_MID);
    data_right_shoulder.data.push_back(RSHOUL_UD_MID);
    data_right_shoulder.data.push_back(RSHOUL_TILT_MID);

    std_msgs::UInt8MultiArray data_head;
    data_head.layout.dim.clear();
    data_head.data.push_back(HEAD_MOUTH_MID);
    data_head.data.push_back(HEAD_EYE_ROTAT_MID);
    data_head.data.push_back(HEAD_EYE_TILT_MID);
    data_head.data.push_back(HEAD_ROTAT_MID);

    std_msgs::UInt8MultiArray data_neck;
    data_neck.layout.dim.clear();
    data_neck.data.push_back(NECK_RIGHT_MID);
    data_neck.data.push_back(NECK_LEFT_MID);
    data_neck.data.push_back(NECK_MID_MID);

    std_msgs::String data_play_audio;

    std::stringstream ss;
    ss << "/home/robot/_15.mp3";
    data_play_audio.data = ss.str();

    while (ros::ok()) {

        if (flag_on_off) {
            if (flag_on == 1) {
                flag_on = 0;
                data_right_shoulder.data[0] = 60;
                data_right_shoulder.data[1] = 100;
                data_right_shoulder.data[2] = 80;
                data_right_shoulder.data[3] = 63;
                play_audio.publish(data_play_audio);
                right_arm.publish(data_right_arm);
                right_shoulder.publish(data_right_shoulder);
            }
            if (flag_move_mouth == 1) {
                if ((ros::Time::now() - now_time).toSec() > 6.0) {
                    flag_move_mouth = 0;
                    data_head.data[0] = HEAD_MOUTH_MID;
                    data_neck.data[2] = NECK_MID_MID;
                } else {
                    if (flag_state_mouth == 1) {
                        data_head.data[0] += 3;
                        if (data_head.data[0] >= 20) {
                            data_head.data[0] = 20;
                            flag_state_mouth = 0;
                        }
                        data_neck.data[2] += 2;
                        if (data_neck.data[2] >= 80) {
                            data_neck.data[2] = 80;
                        }
                    } else {
                        int a = data_head.data[0];
                        a -= 3;
                        if (a < 0) {
                            a = 0;
                        }
                        data_head.data[0] = a;
                        if (data_head.data[0] <= 0) {
                            data_head.data[0] = 0;
                            flag_state_mouth = 1;
                        }
                        data_neck.data[2] -= 2;
                        if (data_neck.data[2] <= 55) {
                            data_neck.data[2] = 55;
                        }
                    }
                }
                head.publish(data_head);
                neck.publish(data_neck);
            }
            // data_right_arm.data[0] = RHAND_FINGER_1_MAX;
            // data_right_arm.data[1] = RHAND_FINGER_2_MAX;
            // data_right_arm.data[2] = RHAND_FINGER_3_MAX;
            // data_right_arm.data[3] = RHAND_FINGER_4_MAX;
            // data_right_arm.data[4] = RHAND_FINGER_5_MAX;
            // data_right_arm.data[5] = RHAND_WRIST_MID;
           
        } else {
            if (flag_on == 1) {
                flag_on = 0;
                data_right_shoulder.data[0] = RHAND_BICEPS_MID;
                data_right_shoulder.data[1] = RSHOUL_ROTAT_MID;
                data_right_shoulder.data[2] = RSHOUL_UD_MID;
                data_right_shoulder.data[3] = RSHOUL_TILT_MID;
                right_arm.publish(data_right_arm);
                right_shoulder.publish(data_right_shoulder);

                data_head.data[0] = HEAD_MOUTH_MID;
                head.publish(data_head);
                data_neck.data[2] = NECK_MID_MID;
                neck.publish(data_neck);
            }
            // data_right_arm.data[0] = RHAND_FINGER_1_MIN;
            // data_right_arm.data[1] = RHAND_FINGER_2_MIN;
            // data_right_arm.data[2] = RHAND_FINGER_3_MIN;
            // data_right_arm.data[3] = RHAND_FINGER_4_MIN;
            // data_right_arm.data[4] = RHAND_FINGER_5_MIN;
            // data_right_arm.data[5] = RHAND_WRIST_MID;
        }
        ros::spinOnce();
        loop_rate.sleep();
    }
}