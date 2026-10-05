cmake_minimum_required(VERSION 3.20)

project(allhjson LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_library(allhjson STATIC
    hjson_decode.cpp
    hjson_encode.cpp
    hjson_parsenumber.cpp
    hjson_value.cpp
)

target_include_directories(allhjson PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}"
)

target_compile_features(allhjson PUBLIC cxx_std_11)
