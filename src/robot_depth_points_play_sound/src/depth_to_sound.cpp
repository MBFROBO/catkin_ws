#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/PointCloud2.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>
#include <image_transport/image_transport.h>


void imageCb(const sensor_msgs::Image& msg)
{
    cv_bridge::CvImagePtr cv_ptr;    
    cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::TYPE_32FC1);
   
    cv::Mat convertImage;

    cv_ptr->image.convertTo(convertImage, CV_8UC1);

    cv::Mat colorImage;
    cv::applyColorMap(convertImage, colorImage, cv::COLORMAP_HOT);

    cv::imshow("image", colorImage);
    cv::waitKey(3);
}

int main(int argc, char **argv) {

    ros::init(argc, argv, "image_converter");
    
    ros::NodeHandle nh;

    // image_transport::Subscriber image_sub_;
    // image_transport::ImageTransport it_;

    ros::Subscriber image_sub_ = nh.subscribe("/camera/depth/image", 1, imageCb);

    ros::spin();
    return 0;
}