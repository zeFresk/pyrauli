cmake_minimum_required(VERSION 3.15)
project(pyrauli LANGUAGES CXX)

set(CMAKE_POSITION_INDEPENDENT_CODE ON) # static -> dynamic

include(FetchContent)

FetchContent_Declare(
		pybind11
		GIT_REPOSITORY https://github.com/pybind/pybind11.git
		GIT_TAG        v2.13.6 # upgrade to v3?
)

# Import C++ backend
FetchContent_Declare(
		propauli
		GIT_REPOSITORY https://github.com/zefresk/propauli.git
		GIT_TAG v2.1.0
)

FetchContent_MakeAvailable(pybind11 propauli)

pybind11_add_module(_core src/pyrauli/_core/bindings.cpp)

target_link_libraries(_core PRIVATE propaulib)

install(
				TARGETS _core
				LIBRARY DESTINATION pyrauli
)
