---
id: 19c__DBMS_SCHEDULER.GET_ATTRIBUTE
name: DBMS_SCHEDULER.GET_ATTRIBUTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.GET_ATTRIBUTE

This procedure retrieves the value of an attribute of a Scheduler object. It is overloaded to retrieve values of various types.

## Syntax

```sql
DBMS_SCHEDULER.GET_ATTRIBUTE (
   name           IN VARCHAR2,
   attribute      IN VARCHAR2,
   value          OUT {VARCHAR2|PLS_INTEGER|BOOLEAN|DATE|TIMESTAMP|
                        TIMESTAMP WITH TIME ZONE|TIMESTAMP WITH LOCAL TIME ZONE|
                        INTERVAL DAY TO SECOND});

DBMS_SCHEDULER.GET_ATTRIBUTE (
   name           IN VARCHAR2,
   attribute      IN VARCHAR2,
   value          OUT VARCHAR2,
   value2         OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The name of the object |
| attribute | VARCHAR2 | IN | The attribute being retrieved. See the SET_ATTRIBUTE Procedure for tables of attribute values. |
| value | OUT | IN | The existing value of the attribute |
| value2 | VARCHAR2) | OUT | The value2 argument is for an optional second value. Most attributes have only one value associated with them, but some can have two. |

## Usage Notes

Syntax DBMS_SCHEDULER.GET_ATTRIBUTE ( name IN VARCHAR2, attribute IN VARCHAR2, value OUT {VARCHAR2|PLS_INTEGER|BOOLEAN|DATE|TIMESTAMP| TIMESTAMP WITH TIME ZONE|TIMESTAMP WITH LOCAL TIME ZONE| INTERVAL DAY TO SECOND}); DBMS_SCHEDULER.GET_ATTRIBUTE ( name IN VARCHAR2, attribute IN VARCHAR2, value OUT VARCHAR2, value2 OUT VARCHAR2); Parameters Table 151-66 GET_ATTRIBUTE Procedure Parameters Parameter Description name The name of the object attribute The attribute being retrieved. See the SET_ATTRIBUTE Procedure for tables of attribute values. value The existing value of the attribute value2 The value2 argument is for an optional second value. Most attributes have only one value associated with them, but some can have two. Usage Notes To run GET_ATTRIBUTE for a job class, you must have the MANAGE SCHEDULER privilege or have EXECUTE privileges on the class. For a schedule, window, or group, no privileges are necessary. Otherwise, you must be the owner of the object or have ALTER or EXECUTE privileges on that object or have the CREATE ANY JOB privilege. See the SET_ATTRIBUTE Procedure for tables of attribute values that you can retrieve for the various Scheduler object types.