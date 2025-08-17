cmake_minimum_required(VERSION 3.8)
project(hexapod)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

install(
  DIRECTORY models/
  DESTINATION share/${PROJECT_NAME}/models
)
install(
  DIRECTORY urdf/
  DESTINATION share/${PROJECT_NAME}/urdf
)
install(
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)
install(
  DIRECTORY config/
  DESTINATION share/${PROJECT_NAME}/config
)
install(
  DIRECTORY yaml/
  DESTINATION share/${PROJECT_NAME}/yaml
)
ament_package()
