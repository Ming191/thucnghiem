cmake_minimum_required(VERSION 3.20)

project(jvar LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

option(JVAR_AUTOADDPROP "Enable adding properties on assignment" OFF)
option(JVAR_BUILD_EXAMPLES "Build jvar example executables" OFF)

add_library(jvar STATIC
    src/str.cpp
    src/util.cpp
    src/arr.cpp
    src/var.cpp
    src/json.cpp
)

target_include_directories(jvar PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}/src"
)

target_compile_features(jvar PUBLIC cxx_std_11)

if(UNIX AND NOT APPLE)
    target_compile_definitions(jvar PRIVATE _GNU_SOURCE)
endif()

target_compile_options(jvar PRIVATE
    -Wall
    -Wextra
    -Wno-unused-parameter
    -Wno-variadic-macros
    -Wno-ignored-qualifiers
)

if(JVAR_AUTOADDPROP)
    target_compile_definitions(jvar PUBLIC AUTOADDPROP)
endif()

if(JVAR_BUILD_EXAMPLES)
    foreach(example IN ITEMS basics arrays objs printv jsonparse func misc)
        add_executable("ex_${example}" "example/${example}.cpp")
        target_link_libraries("ex_${example}" PRIVATE jvar)
    endforeach()
endif()
