#include "std_msgs/Int8.h"
#include "ros/ros.h"
#include "signal.h"
#include "termios.h"
#include "stdio.h"

#define KEYCODE_R   0x43
#define KEYCODE_Q   0x71

uint8_t key_move = 0;

int kfd = 0;
struct termios cooked, raw;

void keyboard_setup() {
    tcgetattr(kfd, &cooked);
    memcpy(&kfd, &cooked, sizeof(struct termios));
    raw.c_lflag &= ~(ICANON | ECHO);
    raw.c_cc[VEOL] = 1;
    raw.c_cc[VEOF] = 2;
    tcsetattr(kfd, TCSANOW, &raw);
}

void quit (int sig) {
    (void)sig;
    tcsetattr(kfd, TCSANOW, &cooked);
    ros::shutdown();
    exit(0);
}

void keyboard_loop() {

    char c;

    if (read(kfd, &c, 1) < 0) {

    }

    ROS_INFO("key pressed = %c", c);


    if (c == KEYCODE_R) {
        key_move = 1;
    } else if (c == KEYCODE_Q) {
        key_move = 0;
    }

}

int main(int argc, char **argv) {

    ros::init(argc, argv, "robot_start_move");
    ros::NodeHandle nh;

    ros::Publisher move = nh.advertise<std_msgs::Int8>("/on_off", 1000);
    ros::Rate loop_rate(5);

    std_msgs::Int8 data;

    // data.data = 0;

    // keyboard_setup();

    // signal(SIGINT, quit);

    ros::Time time;

    time = ros::Time::now();

    double time_wait = 20.0;

    while (ros::ok()) {

        // keyboard_loop();

        if ((ros::Time::now() - time).toSec() > time_wait) {
            key_move = !key_move;
            if (key_move == 1) {
                time_wait = 5.0;
            } else {
                time_wait = 20.0;
            }
            data.data = key_move;
            move.publish(data);
            time = ros::Time::now();
        }

        ros::spinOnce();
        loop_rate.sleep();
    }

}