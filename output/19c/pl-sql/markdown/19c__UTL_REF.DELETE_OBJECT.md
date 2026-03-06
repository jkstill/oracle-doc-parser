---
id: 19c__UTL_REF.DELETE_OBJECT
name: UTL_REF.DELETE_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_REF
tags: [utl_ref]
source_file: UTL_REF.html
---

# UTL_REF.DELETE_OBJECT

This procedure deletes an object given a reference.

## Syntax

```sql
DELETE FROM object_table  
WHERE REF(t) = reference;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| reference |  |  | Reference of the object to delete. |

## Usage Notes

The semantic of this subprogram is similar to the following SQL statement: DELETE FROM object_table WHERE REF(t) = reference; Unlike the preceding SQL statement, this subprogram does not require you to specify the object table name where the object resides. Syntax UTL_REF.DELETE_OBJECT ( reference IN REF "<typename>"); Parameters Table 274-3 DELETE_OBJECT Procedure Parameters Parameter Description reference Reference of the object to delete. Exceptions May be raised. Examples The following example illustrates usage of the UTL_REF package to implement this scenario: if an employee of a company changes their address, their manager should be notified. ... declarations of Address_t and others... CREATE OR REPLACE TYPE Person_t ( name VARCHAR2(64), gender CHAR(1), address Address_t, MEMBER PROCEDURE setAddress(addr IN Address_t) ); CREATE OR REPLACE TYPE BODY Person_t ( MEMBER PROCEDURE setAddress(addr IN Address_t) IS BEGIN address := addr; END; ); CREATE OR REPLACE TYPE Employee_t ( Under Person_t : Simulate implementation of inheritance using a REF to Person_t and delegation of setAddress to it. thePerson REF Person_t, empno NUMBER(5), deptREF Department_t, mgrREF Employee_t, reminders StringArray_t, MEMBER PROCEDURE setAddress(addr IN Address_t), MEMBER procedure addReminder(reminder VARCHAR2); ); CREATE TYPE BODY Employee_t ( MEMBER PROCEDURE setAddress(addr IN Address_t) IS myMgr Employee_t; meAsPerson Person_t; BEGIN Update the address by delegating the responsibility to thePerson . Lock the Person object from the reference, and also select it: UTL_REF.LOCK_OBJECT(thePerson, meAsPerson); meAsPerson.setAddress(addr); Delegate to thePerson : UTL_REF.UPDATE_OBJECT(thePerson, meAsPerson); if mgr is NOT NULL THEN Give the manager a reminder: UTL_REF.LOCK_OBJECT(mgr); UTL_REF.SELECT_OBJECT(mgr, myMgr); myMgr.addReminder ('Update address in the employee directory for' || thePerson.name || ', new address: ' || addr.asString); UTL_REF.UPDATE_OBJECT(mgr, myMgr); END IF; EXCEPTION WHEN OTHERS THEN errnum := SQLCODE; errmsg := SUBSTR(SQLERRM, 1, 200);