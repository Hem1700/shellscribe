cmake_minimum_required(VERSION 3.20)
project(shellscribe_core LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(shellscribe_core STATIC src/core.cpp)
target_include_directories(shellscribe_core PUBLIC include)
