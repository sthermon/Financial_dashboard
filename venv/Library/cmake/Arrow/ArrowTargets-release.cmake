#----------------------------------------------------------------
# Generated CMake target import file for configuration "RELEASE".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Arrow::arrow_shared" for configuration "RELEASE"
set_property(TARGET Arrow::arrow_shared APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(Arrow::arrow_shared PROPERTIES
  IMPORTED_IMPLIB_RELEASE "D:/Personal_projects/Financial_health/venv/Library/arrow.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/arrow.dll"
  )

list(APPEND _cmake_import_check_targets Arrow::arrow_shared )
list(APPEND _cmake_import_check_files_for_Arrow::arrow_shared "D:/Personal_projects/Financial_health/venv/Library/arrow.lib" "${_IMPORT_PREFIX}/bin/arrow.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
