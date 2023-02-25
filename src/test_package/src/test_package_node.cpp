#include "ros/ros.h"
#include "std_msgs/Int16.h"

int main (int argv, char** argc) {
    ros::init(argv, argc, "test_node");

    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::Int16>("test_topic", 1000);

    ros::Rate loop_rate(10);

    std_msgs::Int16 data;

    int a = 0;

    while (ros::ok()) {

        data.data = a;

        a++;

        pub.publish(data);

        ros::spinOnce();
        loop_rate.sleep();
    }
}