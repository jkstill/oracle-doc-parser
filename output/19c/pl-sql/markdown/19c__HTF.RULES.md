---
id: 19c__HTF.RULES
name: HTF.RULES
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.RULES

If you use values of the LONG datatype in functions such as HTF.PRINT , HTF.PRN , HTF.PA or OWA_UTIL . CELLSPRINT , only the first 32 K of the LONG data is used. The LONG data is bound to a VARCHAR2 datatype in the function.