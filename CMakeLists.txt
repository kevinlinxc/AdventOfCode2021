cmake_minimum_required(VERSION 3.21)
project(AdventOfCode2021)

set(CMAKE_CXX_STANDARD 14)
set(Boost_INCLUDE_DIR C:/MinGW/include/)
set(Boost_LIBRARY_DIR C:/MinGW/lib/)
find_package(Boost 1.77.0 COMPONENTS REQUIRED)
include_directories(${Boost_INCLUDE_DIR})
include_directories(CppSrc)

add_executable(AdventOfCode2021
        CppSrc/Day5.cpp
        CppSrc/Day5.h)
