#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "utf8_range::utf8_validity" for configuration "Release"
set_property(TARGET utf8_range::utf8_validity APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(utf8_range::utf8_validity PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/utf8_validity.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/utf8_validity.dll"
  )

list(APPEND _cmake_import_check_targets utf8_range::utf8_validity )
list(APPEND _cmake_import_check_files_for_utf8_range::utf8_validity "${_IMPORT_PREFIX}/lib/utf8_validity.lib" "${_IMPORT_PREFIX}/bin/utf8_validity.dll" )

# Import target "utf8_range::utf8_range" for configuration "Release"
set_property(TARGET utf8_range::utf8_range APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(utf8_range::utf8_range PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/utf8_range.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/utf8_range.dll"
  )

list(APPEND _cmake_import_check_targets utf8_range::utf8_range )
list(APPEND _cmake_import_check_files_for_utf8_range::utf8_range "${_IMPORT_PREFIX}/lib/utf8_range.lib" "${_IMPORT_PREFIX}/bin/utf8_range.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
