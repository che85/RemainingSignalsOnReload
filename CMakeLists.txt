cmake_minimum_required(VERSION 2.8.9)

project(SlicerIssueExamples)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/SlicerIssueExamples")
set(EXTENSION_CATEGORY "Examples")
set(EXTENSION_CONTRIBUTORS "Christian Herz ((SPL, BWH))")
set(EXTENSION_DESCRIPTION "This extension shows examples to 3D Slicer issues")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/SlicerIssueExamples.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/SlicerIssueExamples/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(RemaingSignalsAfterReload)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
