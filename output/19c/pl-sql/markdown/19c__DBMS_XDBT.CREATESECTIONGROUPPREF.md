---
id: 19c__DBMS_XDBT.CREATESECTIONGROUPPREF
name: DBMS_XDBT.CREATESECTIONGROUPPREF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CREATESECTIONGROUPPREF

This procedure creates a section group for the CONTEXT index on the XML DB hierarchy.

## Syntax

```sql
DBMS_XDBT.CREATESECTIONGROUPPREF;
```

## Usage Notes

Syntax DBMS_XDBT.CREATESECTIONGROUPPREF; Usage Notes The name of the section group can be changed; see the SectiongroupPref configuration setting. The HTML sectioner is used by default. No zone sections are created by default. If the vast majority of documents are XML, consider using the AUTO_SECTION_GROUP or the PATH_SECTION_GROUP ; see the SectionGroup configuration setting.