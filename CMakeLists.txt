cmake_minimum_required(VERSION 3.15)
project(pyrauli LANGUAGES CXX)

set(CMAKE_POSITION_INDEPENDENT_CODE ON) # static -> dynamic

include(FetchContent)

if(APPLE)
    find_program(BREW_EXECUTABLE brew)

    if(BREW_EXECUTABLE)
        message(STATUS "Homebrew found, checking for libomp.")
        
        # 3. Get the Homebrew prefix (e.g., /opt/homebrew or /usr/local)
        execute_process(
            COMMAND ${BREW_EXECUTABLE} --prefix
            OUTPUT_VARIABLE BREW_PREFIX
            OUTPUT_STRIP_TRAILING_WHITESPACE
            RESULT_VARIABLE BREW_RESULT
        )

        if(BREW_RESULT EQUAL 0)
            set(LIBOMP_ROOT "${BREW_PREFIX}/opt/libomp")
            
            if(EXISTS "${LIBOMP_ROOT}")
                list(APPEND CMAKE_PREFIX_PATH "${LIBOMP_ROOT}")
		set(OpenMP_ROOT "${LIBOMP_ROOT}")
            endif()
        endif()
    endif()
endif()


FetchContent_Declare(
		pybind11
		GIT_REPOSITORY https://github.com/pybind/pybind11.git
		GIT_TAG        v2.13.6 # upgrade to v3?
)

# Import C++ backend
FetchContent_Declare(
		propauli
		GIT_REPOSITORY https://github.com/zefresk/propauli.git
		GIT_TAG v4.0.0
)

FetchContent_MakeAvailable(pybind11 propauli)

pybind11_add_module(_core src/pyrauli/_core/bindings.cpp)

target_link_libraries(_core PRIVATE propaulib)

install(
				TARGETS _core
				LIBRARY DESTINATION pyrauli
)
