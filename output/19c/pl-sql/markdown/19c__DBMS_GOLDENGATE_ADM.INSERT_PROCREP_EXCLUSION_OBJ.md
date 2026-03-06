---
id: 19c__DBMS_GOLDENGATE_ADM.INSERT_PROCREP_EXCLUSION_OBJ
name: DBMS_GOLDENGATE_ADM.INSERT_PROCREP_EXCLUSION_OBJ
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.INSERT_PROCREP_EXCLUSION_OBJ

This procedure inserts a database object into the exclusion list for Oracle GoldenGate procedural replication.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.INSERT_PROCREP_EXCLUSION_OBJ(
   package_owner     IN VARCHAR2 DEFAULT NULL,
   package_name      IN VARCHAR2 DEFAULT NULL,
   object_owner      IN VARCHAR2 DEFAULT NULL,
   object_name       IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| package_owner | VARCHAR2 | IN | The owner of the package. |
| package_name | VARCHAR2 | IN | The name of the package. |
| object_owner | VARCHAR2 | IN | The owner of the object. |
| object_name | VARCHAR2 | IN | The name of the object. |

## Usage Notes

When a database object is on the exclusion list for Oracle GoldenGate procedural replication, execution of subprogram in the package is not replicated if the subprogram operates on the excluded object. For example, if hr.employees is an excluded database object for the DBMS_REDEFINITION package, then an execution of the DBMS_REDEFINITION.START_REDEF_TABLE procedure on the hr.employees table is not replicated. Caution: Run the INSERT_PROCREP_EXCLUSION_OBJ procedure only under the direction of Oracle Support. Caution: Run the INSERT_PROCREP_EXCLUSION_OBJ procedure only under the direction of Oracle Support. Syntax DBMS_GOLDENGATE_ADM.INSERT_PROCREP_EXCLUSION_OBJ( package_owner IN VARCHAR2 DEFAULT NULL, package_name IN VARCHAR2 DEFAULT NULL, object_owner IN VARCHAR2 DEFAULT NULL, object_name IN VARCHAR2 DEFAULT NULL); Parameters Table 76-8 INSERT_PROCREP_EXCLUSION_OBJ Procedure Parameters Parameter Description package_owner The owner of the package. package_name The name of the package. object_owner The owner of the object. object_name The name of the object.