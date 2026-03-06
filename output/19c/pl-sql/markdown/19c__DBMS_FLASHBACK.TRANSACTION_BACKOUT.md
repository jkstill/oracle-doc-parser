---
id: 19c__DBMS_FLASHBACK.TRANSACTION_BACKOUT
name: DBMS_FLASHBACK.TRANSACTION_BACKOUT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK
tags: [dbms_flashback]
source_file: DBMS_FLASHBACK.html
---

# DBMS_FLASHBACK.TRANSACTION_BACKOUT

This procedure provides a mechanism to back out a set of transactions. The user can call these procedures with either transaction names or transaction identifiers ( XIDS ).

## Syntax

```sql
DBMS_FLASHBACK.TRANSACTION_BACKOUT
   numtxns            NUMBER,
   xids               XID_ARRAY,
   options            NUMBER default NOCASCADE, 
   timeHint           TIMESTAMP default MINTIME);

DBMS_FLASHBACK.TRANSACTION_BACKOUT
   numtxns            NUMBER,  
   xids               XID_ARRAY, 
   options            NUMBER default NOCASCADE,
   scnHint            TIMESTAMP default 0   );

DBMS_FLASHBACK.TRANSACTION_BACKOUT
   numtxns           NUMBER,
   txnnames          TXNAME_ARRAY,
   options           NUMBER default NOCASCADE,
   timehint          TIMESTAMP MINTIME );

DBMS_FLASHBACK.TRANSACTION_BACKOUT
   numtxns           NUMBER, 
   txnNames         TXNAME_ARRAY, 
   options          NUMBER default NOCASCADE,
   scnHint          NUMBER 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| numtxns | NUMBER | IN | Number of transactions passed as input |
| xids | XID_ARRAY | IN | List of transaction IDs in the form of an array |
| txnnames | TXNAME_ARRAY | IN | List of transaction names in the form of an array |
| options | NUMBER | IN | Back out dependent transactions: NOCASCADE - No dependency is expected. If a dependency is found, this raises an error, with the first dependent transaction provided in the report. NOCASCADE_FORCE - The user forcibly backs out the given transactions without considering the dependent transactions. The RDBMS executes the UNDO SQL for the given transactions in reverse order of their commit times. If no constraints break, and the result is satisfactory, the user can either COMMIT the changes or else ROLL BACK . NONCONFLICT_ONLY - This option lets the user back out the changes to the nonconflicting rows of the given transactions. Note that a transaction dependency can happen due to a row conflict through either WAW or primary/unique key constraints. If the user chooses to back out only the nonconflicting rows, this does not cause any problem with database consistency, although transaction atomicity is lost. As this is a recovery operation, the user can correct the data. CASCADE - This completely removes the given transactions including their dependents in a post order fashion (reverse order of commit times). |
| timehint | TIMESTAMP | IN | Time hint on the start of the transaction |
| scnhint | TIMESTAMP | IN | SCN hint on the start of the transaction |

## Usage Notes

The procedure analyzes the transactional dependencies, perform DMLs and generates an extensive report on the operation performed by the subprogram. This procedure does not commit the DMLs performed as part of transaction back out. However it holds all the required locks on rows and tables in the right form, so that no other dependencies can enter the system. To make the changes permanent you must explicitly commit the transaction. A report is generated in the system tables DBA_FLASHBACK_TRANSACTION_STATE and DBA_FLASHBACK_TRANSACTION_REPORT . Syntax DBMS_FLASHBACK.TRANSACTION_BACKOUT numtxns NUMBER, xids XID_ARRAY, options NUMBER default NOCASCADE, timeHint TIMESTAMP default MINTIME); DBMS_FLASHBACK.TRANSACTION_BACKOUT numtxns NUMBER, xids XID_ARRAY, options NUMBER default NOCASCADE, scnHint TIMESTAMP default 0 ); DBMS_FLASHBACK.TRANSACTION_BACKOUT numtxns NUMBER, txnnames TXNAME_ARRAY, options NUMBER default NOCASCADE, timehint TIMESTAMP MINTIME ); DBMS_FLASHBACK.TRANSACTION_BACKOUT numtxns NUMBER, txnNames TXNAME_ARRAY, options NUMBER default NOCASCADE, scnHint NUMBER 0); Parameters Table 72-6 TRANSACTION_BACKOUT Procedure Parameters Parameter Description numtxns Number of transactions passed as input xids List of transaction IDs in the form of an array txnnames List of transaction names in the form of an array options Back out dependent transactions: NOCASCADE - No dependency is expected. If a dependency is found, this raises an error, with the first dependent transaction provided in the report. NOCASCADE_FORCE - The user forcibly backs out the given transactions without considering the dependent transactions. The RDBMS executes the UNDO SQL for the given transactions in reverse order of their commit times. If no constraints break, and the result is satisfactory, the user can either COMMIT the changes or else ROLL BACK . NONCONFLICT_ONLY - This option lets the user back out the changes to the nonconflicting rows of the given transactions. Note that a transaction dependency can happen due to a row conflict through either WAW or primary/unique key constraints. If the user chooses to back out only the nonconflicting rows, this does not cause any problem with database consistency, although transaction atomicity is lost. As this is a recovery operation, the user can correct the data. CASCADE - This completely removes the given transactions including their dependents in a post order fashion (reverse order of commit times). timehint Time hint on the start of the transaction scnhint SCN hint on the start of the transaction Usage Notes Note: For information about restrictions in using TRANSACTION_BACKOUT , see "Using Flashback Transaction" in the Oracle Database Development Guide . If transaction name is used, a time hint must be provided. The time hint should be a time before the start of all the given transactions to back out. If the SCN hint is provided, it must be before the start of the earliest transaction in the specified input set, or this raises an error and terminates. If it is not provided and the transaction has committed within undo retention, the database system is able to determine the start time. Note: For information about restrictions in using TRANSACTION_BACKOUT , see "Using Flashback Transaction" in the Oracle Database Development Guide .