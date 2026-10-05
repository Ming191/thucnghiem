cmake_minimum_required(VERSION 3.20)

project(alljson LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_library(alljson STATIC
    bignum-dtoa.cc
    bignum.cc
    cached-powers.cc
    double-to-string.cc
    fast-dtoa.cc
    fixed-dtoa.cc
    json.cpp
    string-to-double.cc
    strtod.cc
)

target_include_directories(alljson PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}"
)

target_compile_features(alljson PUBLIC cxx_std_11)
