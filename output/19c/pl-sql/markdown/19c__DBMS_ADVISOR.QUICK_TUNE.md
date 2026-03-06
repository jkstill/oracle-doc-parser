---
id: 19c__DBMS_ADVISOR.QUICK_TUNE
name: DBMS_ADVISOR.QUICK_TUNE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.QUICK_TUNE

This procedure performs an analysis and generates recommendations for a single SQL statement.

## Syntax

```sql
DBMS_ADVISOR.QUICK_TUNE (
   advisor_name           IN VARCHAR2,
   task_name              IN VARCHAR2,
   attr1                  IN CLOB,
   attr2                  IN VARCHAR2 := NULL,
   attr3                  IN NUMBER := NULL,
   template               IN VARCHAR2 := NULL,
   implement              IN BOOLEAN := FALSE,
   description            IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| advisor_name | VARCHAR2 | IN | Name of the Advisor that will perform the analysis. |
| task_name | VARCHAR2 | IN | Name of the task. |
| attr1 | CLOB | IN | Advisor-specific attribute in the form of a CLOB variable. |
| attr2 | VARCHAR2 | IN | Advisor-specific attribute in the form of a VARCHAR2 variable. |
| attr3 | NUMBER | IN | Advisor-specific attribute in the form of a NUMBER . |
| template | VARCHAR2 | IN | Name of an existing task or template from which the initial settings need to be copied. |
| implement | BOOLEAN | IN | Flag specifying whether to implement the task. |
| description | VARCHAR2 | IN | Description of the task. |

## Usage Notes

This provides a shortcut method of all necessary operations to analyze the specified SQL statement. The operation creates a task using the specified task name. The task will be created using a specified Advisor task template. Finally, the task will be executed and the results will be saved in the repository. Syntax DBMS_ADVISOR.QUICK_TUNE ( advisor_name IN VARCHAR2, task_name IN VARCHAR2, attr1 IN CLOB, attr2 IN VARCHAR2 := NULL, attr3 IN NUMBER := NULL, template IN VARCHAR2 := NULL, implement IN BOOLEAN := FALSE, description IN VARCHAR2 := NULL); Parameters Table 16-28 QUICK_TUNE Procedure Parameters Parameter Description advisor_name Name of the Advisor that will perform the analysis. task_name Name of the task. attr1 Advisor-specific attribute in the form of a CLOB variable. attr2 Advisor-specific attribute in the form of a VARCHAR2 variable. attr3 Advisor-specific attribute in the form of a NUMBER . template Name of an existing task or template from which the initial settings need to be copied. implement Flag specifying whether to implement the task. description Description of the task. Usage Notes If indicated by the user, the final recommendations can be implemented by the procedure. The task will be created using either a specified SQL Access task template or the built-in default template of SQLACCESS_GENERAL . The workload will only contain the specified statement, and all task parameters will be defaulted. attr1 must be the single SQL statement to tune. For the SQL Access Advisor, attr2 is the user who would execute the single statement. If omitted, the current user will be used. Examples DECLARE task_name VARCHAR2(30); BEGIN task_name := 'My Task'; DBMS_ADVISOR.QUICK_TUNE(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_name, 'SELECT AVG(amount_sold) FROM sh.sales WHERE promo_id=10'); END; /