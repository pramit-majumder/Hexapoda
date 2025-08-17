import os
from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path

def generate_launch_description():
    urdf = os.path.join(get_package_share_path('hexapod'),'urdf',"Hexapoda.urdf.xacro")
    des = os.path.join(get_package_share_path('hexapod'),'config',"hexapod.rviz")
    print(des)
    print(urdf)

    rsp = Node(package="robot_state_publisher", executable="robot_state_publisher", parameters=[{'robot_description': Command(["xacro ", urdf])}])
    jsp = Node(package="joint_state_publisher_gui", executable="joint_state_publisher_gui")
    rviz = Node(package="rviz2", executable="rviz2", output="screen")

    return LaunchDescription([
        rsp, jsp, rviz
    ])