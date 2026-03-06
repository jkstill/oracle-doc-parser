---
id: 19c__INTRODUCTION.USING
name: INTRODUCTION.USING
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: INTRODUCTION
tags: [introduction]
source_file: introduction-to-oracle-supplied-plsql-packages-and-types.html
---

# INTRODUCTION.USING

Most Oracle supplied packages are automatically installed when the database is created. Certain packages are not installed automatically. Special installation instructions for these packages are documented in the individual chapters.

## Usage Notes

To call a PL/SQL function from SQL, you must either own the function or have EXECUTE privileges on the function. To select from a view defined with a PL/SQL function, you must have SELECT privileges on the view. No separate EXECUTE privileges are needed to select from the view. Instructions on special requirements for packages are documented in the individual chapters.