cmake_minimum_required(VERSION 3.20)

project(jsonxx LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_library(jsonxx STATIC
    jsonxx.cc
)

target_include_directories(jsonxx PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}"
)

target_compile_features(jsonxx PUBLIC cxx_std_11)

option(JSONXX_BUILD_TESTS "Build the legacy jsonxx test executable" OFF)

if(JSONXX_BUILD_TESTS)
    add_executable(jsonxx_test jsonxx_test.cc)
    target_link_libraries(jsonxx_test PRIVATE jsonxx)
endif()
