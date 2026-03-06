---
id: 19c__UTL_RAW
name: UTL_RAW
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW

UTL_RAW allows a RAW "record" to be composed of many elements. By using the RAW datatype, character set conversion will not be performed, keeping the RAW in its original format when being transferred through remote procedure calls.

## Usage Notes

With the RAW functions, you can manipulate binary data that was previously limited to the hextoraw and rawtohex functions. Note: Notes on datatypes: The PLS_INTEGER and BINARY_INTEGER datatypes are identical. This document uses BINARY_INTEGER to indicate datatypes in reference information (such as for table types, record types, subprogram parameters, or subprogram return values), but may use either in discussion and examples. The INTEGER and NUMBER(38) datatypes are also identical. This document uses INTEGER throughout. Note: Notes on datatypes: The PLS_INTEGER and BINARY_INTEGER datatypes are identical. This document uses BINARY_INTEGER to indicate datatypes in reference information (such as for table types, record types, subprogram parameters, or subprogram return values), but may use either in discussion and examples. The INTEGER and NUMBER(38) datatypes are also identical. This document uses INTEGER throughout.