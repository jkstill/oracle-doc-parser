---
id: 19c__DBMS_XMLSCHEMA
name: DBMS_XMLSCHEMA
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA
tags: [dbms_xmlschema]
source_file: DBMS_XMLSCHEMA.html
---

# DBMS_XMLSCHEMA

There are guidelines for using in-place XML schema evolution.

## Usage Notes

Before you perform an in-place XML-schema evolution, you should follow these preparatory steps: Back up all existing data (instance documents) for the XML schema that will be evolved. Perform a dry run using trace only, that is, without actually evolving the XML schema or updating any instance documents, to produce a trace of the update operations that would be performed during evolution. To do this, set the flag parameter value to only INPLACE_TRACE . Do not also use INPLACE_EVOLVE . After performing the dry run, examine the trace file, verifying that the listed DDL operations are in fact those that you intend.