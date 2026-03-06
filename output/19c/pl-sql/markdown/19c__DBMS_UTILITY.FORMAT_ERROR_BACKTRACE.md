---
id: 19c__DBMS_UTILITY.FORMAT_ERROR_BACKTRACE
name: DBMS_UTILITY.FORMAT_ERROR_BACKTRACE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.FORMAT_ERROR_BACKTRACE

This function displays the call stack at the point where an exception was raised, even if the subprogram is called from an exception handler in an outer scope.

## Syntax

```sql
DBMS_UTILITY.FORMAT_ERROR_BACKTRACE 
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

The output is similar to the output of the SQLERRM function, but not subject to the same size limitation. Syntax DBMS_UTILITY.FORMAT_ERROR_BACKTRACE RETURN VARCHAR2; Return Values The backtrace string. A NULL string is returned if no error is currently being handled. Examples CREATE OR REPLACE PROCEDURE Log_Errors ( i_buff in varchar2 ) IS g_start_pos integer := 1; g_end_pos integer; FUNCTION Output_One_Line RETURN BOOLEAN IS BEGIN g_end_pos := Instr ( i_buff, Chr(10), g_start_pos ); CASE g_end_pos > 0 WHEN true THEN DBMS_OUTPUT.PUT_LINE ( Substr ( i_buff, g_start_pos, g_end_pos-g_start_pos ) ); g_start_pos := g_end_pos+1; RETURN TRUE; WHEN FALSE THEN DBMS_OUTPUT.PUT_LINE ( Substr ( i_buff, g_start_pos, (Length(i_buff)-g_start_pos)+1 ) ); RETURN FALSE; END CASE; END Output_One_Line; BEGIN WHILE Output_One_Line() LOOP NULL; END LOOP; END Log_Errors; / Set Doc Off Set Feedback off Set Echo Off CREATE OR REPLACE PROCEDURE P0 IS e_01476 EXCEPTION; pragma exception_init ( e_01476, -1476 ); BEGIN RAISE e_01476; END P0; / Show Errors CREATE OR REPLACE PROCEDURE P1 IS BEGIN P0(); END P1; / SHOW ERRORS CREATE OR REPLACE PROCEDURE P2 IS BEGIN P1(); END P2; / SHOW ERRORS CREATE OR REPLACE PROCEDURE P3 IS BEGIN P2(); END P3; / SHOW ERRORS CREATE OR REPLACE PROCEDURE P4 IS BEGIN P3(); END P4; / CREATE OR REPLACE PROCEDURE P5 IS BEGIN P4(); END P5; / SHOW ERRORS CREATE OR REPLACE PROCEDURE Top_Naive IS BEGIN P5(); END Top_Naive; / SHOW ERRORS CREATE OR REPLACE PROCEDURE Top_With_Logging IS -- NOTE: SqlErrm in principle gives the same info as Format_Error_Stack. -- But SqlErrm is subject to some length limits, -- while Format_Error_Stack is not. BEGIN P5(); EXCEPTION WHEN OTHERS THEN Log_Errors ( 'Error_Stack...' || Chr(10) || DBMS_UTILITY.FORMAT_ERROR_STACK() ); Log_Errors ( 'Error_Backtrace...' || Chr(10) || DBMS_UTILITY.FORMAT_ERROR_BACKTRACE() ); DBMS_OUTPUT.PUT_LINE ( '----------' ); END Top_With_Logging; / SHOW ERRORS -------------------------------------------------------------------------------- Set ServerOutput On call Top_Naive() /* ERROR at line 1: ORA-01476: divisor is equal to zero ORA-06512: at "U.P0", line 4 ORA-06512: at "U.P1", line 3 ORA-06512: at "U.P2", line 3 ORA-06512: at "U.P3", line 3 ORA-06512: at "U.P4", line 2 ORA-06512: at "U.P5", line 2 ORA-06512: at "U.TOP_NAIVE", line 3 */ ; Set ServerOutput On call Top_With_Logging() /* Error_Stack... ORA-01476: divisor is equal to zero Error_Backtrace... ORA-06512: at "U.P0", line 4 ORA-06512: at "U.P1", line 3 ORA-06512: at "U.P2", line 3 ORA-06512: at "U.P3", line 3 ORA-06512: at "U.P4", line 2 ORA-06512: at "U.P5", line 2 ORA-06512: at "U.TOP_WITH_LOGGING", line 6 ---------- */ ; /* ORA-06512: Cause: Backtrace message as the stack is unwound by unhandled exceptions. Action: Fix the problem causing the exception or write an exception handler for this condition. Or you may need to contact your application administrator or database administrator. */