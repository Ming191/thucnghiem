cmake_minimum_required(VERSION 3.20)

project(allxml LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_library(tinyxml2 STATIC
    tinyxml2.cpp
)

target_include_directories(tinyxml2 PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}"
)

target_compile_features(tinyxml2 PUBLIC cxx_std_11)

option(ALLXML_BUILD_EXAMPLES "Build TinyXML2 example programs" OFF)

if(ALLXML_BUILD_EXAMPLES)
    add_executable(xmltest xmltest.cpp)
    target_link_libraries(xmltest PRIVATE tinyxml2)

    add_executable(html5-printer html5-printer.cpp)
    target_link_libraries(html5-printer PRIVATE tinyxml2)
endif()
