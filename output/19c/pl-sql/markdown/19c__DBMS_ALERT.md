---
id: 19c__DBMS_ALERT
name: DBMS_ALERT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ALERT
tags: [dbms_alert]
source_file: DBMS_ALERT.html
---

# DBMS_ALERT

In this example, suppose that you want to graph average salaries by department, for all employees. Your application needs to know whenever EMP is changed.

## Syntax

```sql
DBMS_ALERT.REGISTER('emp_table_alert');
    <<readagain>>: 
   /* ... read the emp table and graph it */ 
      DBMS_ALERT.WAITONE('emp_table_alert', :message, :status); 
      if status = 0 then goto <<readagain>>; else 
      /* ... error condition */
```

## Usage Notes

Your application would look similar to this code: DBMS_ALERT.REGISTER('emp_table_alert'); <<readagain>>: /* ... read the emp table and graph it */ DBMS_ALERT.WAITONE('emp_table_alert', :message, :status); if status = 0 then goto <<readagain>>; else /* ... error condition */ The EMP table would have a trigger similar to this: CREATE TRIGGER emptrig AFTER INSERT OR UPDATE OR DELETE ON emp BEGIN DBMS_ALERT.SIGNAL('emp_table_alert', 'message_text'); END; When the application is no longer interested in the alert, it makes this request: DBMS_ALERT.REMOVE('emp_table_alert'); This reduces the amount of work required by the alert signaller. If a session exits (or dies) while registered alerts exist, the alerts are eventually cleaned up by future users of this package. The example guarantees that the application always sees the latest data, although it may not see every intermediate value.