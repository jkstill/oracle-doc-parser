---
id: 19c__DBMS_DBFS_CONTENT.CHECKSPI
name: DBMS_DBFS_CONTENT.CHECKSPI
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.CHECKSPI

Given the name of a putative DBMS_DBFS_CONTENT_SPI conforming package, this function or procedure checks whether the package implements all of the provider subprograms with the proper signatures, and reports on the conformance.

## Syntax

```sql
DBMS_DBFS_CONTENT.CHECKSPI (
   package_name        IN              VARCHAR2)
  RETURN  CLOB;
 
DBMS_DBFS_CONTENT.CHECKSPI (
   schema_name         IN              VARCHAR2,
   package_name        IN              VARCHAR2)
  return  clob;
 
DBMS_DBFS_CONTENT.CHECKSPI (
   package_name        IN              VARCHAR2,
   chk                 IN OUT NOCOPY   CLOB);
 
DBMS_DBFS_CONTENT.CHECKSPI (
   schema_name         in              VARCHAR2,
   package_name        in              VARCHAR2,
   chk                 in out nocopy   CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| package_name | VARCHAR2) | IN | Name of package |
| schema_name | VARCHAR2 | IN | Name of schema |
| chk | NOCOPY | IN OUT | CLOB that contains the evaluation results |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.CHECKSPI ( package_name IN VARCHAR2) RETURN CLOB; DBMS_DBFS_CONTENT.CHECKSPI ( schema_name IN VARCHAR2, package_name IN VARCHAR2) return clob; DBMS_DBFS_CONTENT.CHECKSPI ( package_name IN VARCHAR2, chk IN OUT NOCOPY CLOB); DBMS_DBFS_CONTENT.CHECKSPI ( schema_name in VARCHAR2, package_name in VARCHAR2, chk in out nocopy CLOB); Parameters Table 52-21 CHECKSPI Procedure Parameters Parameter Description package_name Name of package schema_name Name of schema chk CLOB that contains the evaluation results Usage Notes The functional form returns a cached temporary LOB of session duration with the results of the analysis. The caller is expected to manage the lifetime of this LOB, as needed. The procedural form generates the results of the analysis into the chk LOB parameter; if the value passed in is NULL , the results are written to the foreground trace file provided that DBMS_DBFS_CONTENT interface tracing is enabled. If neither tracing is enabled nor a valid LOB passed in, the checker does not provide any useful indication of the analysis (other than raise exceptions if it encounters a serious error). If schema_name is NULL , standard name resolution rules (current schema, private synonym, public synonym) are used to try and locate a suitable package to analyze.