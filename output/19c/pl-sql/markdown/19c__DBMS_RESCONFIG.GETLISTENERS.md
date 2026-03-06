---
id: 19c__DBMS_RESCONFIG.GETLISTENERS
name: DBMS_RESCONFIG.GETLISTENERS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.GETLISTENERS

This function returns the list of listeners applicable for a given resource.

## Syntax

```sql
DBMS_RESCONFIG.GETLISTENERS(
   path    IN   VARCHAR2)
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2) | IN | Absolute path of the target resource |

**Returns:** `XMLTYPE`

## Usage Notes

The value returned by this function is an XML document containing the <event-listeners> element of the XDBResconfig . xsd schema. It contains all the listeners applicable to the target resource, including repository-level listeners. From the returned XML document users can use the EXTRACT operator to retrieve the listeners defined for a specific event. Syntax DBMS_RESCONFIG.GETLISTENERS( path IN VARCHAR2) RETURN XMLTYPE; Parameters Table 141-7 GETLISTENERS Function Parameters Parameter Description path Absolute path of the target resource Usage Notes Users must have the required access privilege on all resource configurations referenced by the repository and the target resource; otherwise, an error is returned.