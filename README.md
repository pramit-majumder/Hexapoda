# KRS Hexapod Robot

## Overview
This repository contains the design and simulation files for a six-legged robotic platform (**hexapod**) developed by the KRS Embedded Team.  
The project integrates CAD modeling, ROS 2/Gazebo simulation, and control system development, with plans for hardware implementation using ST3215 digital servos.  

---

## Repository Structure
- **windows/** → Fusion 360 CAD model of the hexapod  
- **linux/** → ROS 2 + Gazebo simulation files and control configuration  
- **README.md** → Project documentation  

---

## Mechanical Design
- Complete design modeled in **Fusion 360**  
- **Leg configuration**: 6 legs, each with 3 revolute joints (coxa, femur, tibia)  
- **Approximate dimensions**:  
  - Coxa: 28 mm  
  - Femur: 78 mm  
  - Tibia: 110 mm  

---

## Simulation
- **Environment**: ROS 2 with Gazebo  
- **Control integration**: via `gazebo_ros2_control`  
- **Controllers available**:  
  - ForwardCommandController → direct position control of joints  
  - JointTrajectoryController → smooth trajectory-based motions  

---

## Actuation
- **Chosen hardware**: ST3215 digital servos  
- **Current status**: Simulation uses generic actuators; hardware integration planned for later stages  

---

## Research Focus
- Development of a **symbolic grid-based localization system** tailored for step-driven robots  
- Goal: link gait generation and localization for reliable movement in complex environments  

---

## Team
Developed and maintained by a **6-member team from the KIIT ROBOTICS SOCIETY**  

---

## Roadmap
1. Debug and finalize controller setup in ROS 2/Gazebo  
2. Implement basic tripod gait using ForwardCommandController  
3. Extend to JointTrajectoryController for advanced gaits  
4. Transition to physical prototype with ST3215 servos  
5. Integrate symbolic localization framework with locomotion  
