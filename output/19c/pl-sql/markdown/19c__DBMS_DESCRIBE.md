---
id: 19c__DBMS_DESCRIBE
name: DBMS_DESCRIBE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DESCRIBE
tags: [dbms_describe]
source_file: DBMS_DESCRIBE.html
---

# DBMS_DESCRIBE

One use of the DESCRIBE_PROCEDURE procedure is as an external service interface.

## Syntax

```sql
TABLE account (accnt_no NUMBER, person_id NUMBER,
               balance NUMBER(7,2)) 
TABLE person  (person_id number(4), person_nm varchar2(10))

CREATE OR REPLACE PACKAGE ACCOUNT_PKG is   FUNCTION ACCOUNT_UPDATE (accnt_no    NUMBER,
                            person      person%rowtype,
                            amounts     DBMS_DESCRIBE.NUMBER_TABLE,
                            trans_date  DATE)
                            return       account.balance%type;
 
   FUNCTION ACCOUNT_UPDATE (accnt_no     NUMBER, 
                            person       person%rowtype,
                            amounts      DBMS_DESCRIBE.NUMBER_TABLE, 
                            trans_no     NUMBER)
                            return       account.balance%type;
END;
```

**Returns:** `account.balance%type`

## Usage Notes

For example, consider a client that provides an OBJECT_NAME of SCOTT . ACCOUNT_UPDATE, where ACCOUNT_UPDATE is an overloaded function with specification: TABLE account (accnt_no NUMBER, person_id NUMBER, balance NUMBER(7,2)) TABLE person (person_id number(4), person_nm varchar2(10)) CREATE OR REPLACE PACKAGE ACCOUNT_PKG is FUNCTION ACCOUNT_UPDATE (accnt_no NUMBER, person person%rowtype, amounts DBMS_DESCRIBE.NUMBER_TABLE, trans_date DATE) return account.balance%type; FUNCTION ACCOUNT_UPDATE (accnt_no NUMBER, person person%rowtype, amounts DBMS_DESCRIBE.NUMBER_TABLE, trans_no NUMBER) return account.balance%type; END; This procedure might look similar to the following output: overload position argument level datatype length prec scale rad -------- --------- -------- ------ -------- ------ ---- ----- --- 1 0 0 2 22 7 2 10 1 1 ACCNT_NO 0 2 0 0 0 0 1 2 PERSON 0 250 0 0 0 0 1 1 PERSON_ID 1 2 22 4 0 10 1 2 PERSON_NM 1 1 10 0 0 0 1 3 AMOUNTS 0 251 0 0 0 0 1 1 1 2 22 0 0 0 1 4 TRANS_DATE 0 12 0 0 0 0 2 0 0 2 22 7 2 10 2 1 ACCNT_NO 0 2 22 0 0 0 2 2 PERSON 0 2 22 4 0 10 2 3 AMOUNTS 0 251 22 4 0 10 2 1 1 2 0 0 0 0 2 4 TRANS_NO 0 2 0 0 0 0 The following PL/SQL procedure has as its parameters all of the PL/SQL datatypes: CREATE OR REPLACE PROCEDURE p1 ( pvc2 IN VARCHAR2, pvc OUT VARCHAR, pstr IN OUT STRING, plong IN LONG, prowid IN ROWID, pchara IN CHARACTER, pchar IN CHAR, praw IN RAW, plraw IN LONG RAW, pbinint IN BINARY_INTEGER, pplsint IN PLS_INTEGER, pbool IN BOOLEAN, pnat IN NATURAL, ppos IN POSITIVE, pposn IN POSITIVEN, pnatn IN NATURALN, pnum IN NUMBER, pintgr IN INTEGER, pint IN INT, psmall IN SMALLINT, pdec IN DECIMAL, preal IN REAL, pfloat IN FLOAT, pnumer IN NUMERIC, pdp IN DOUBLE PRECISION, pdate IN DATE, pmls IN MLSLABEL) AS BEGIN NULL; END; If you describe this procedure using the following: CREATE OR REPLACE PACKAGE describe_it AS PROCEDURE desc_proc (name VARCHAR2); END describe_it; CREATE OR REPLACE PACKAGE BODY describe_it AS PROCEDURE prt_value(val VARCHAR2, isize INTEGER) IS n INTEGER; BEGIN n := isize - LENGTHB(val); IF n < 0 THEN n := 0; END IF; DBMS_OUTPUT.PUT(val); FOR i in 1..n LOOP DBMS_OUTPUT.PUT(' '); END LOOP; END prt_value; PROCEDURE desc_proc (name VARCHAR2) IS overload DBMS_DESCRIBE.NUMBER_TABLE; position DBMS_DESCRIBE.NUMBER_TABLE; c_level DBMS_DESCRIBE.NUMBER_TABLE; arg_name DBMS_DESCRIBE.VARCHAR2_TABLE; dty DBMS_DESCRIBE.NUMBER_TABLE; def_val DBMS_DESCRIBE.NUMBER_TABLE; p_mode DBMS_DESCRIBE.NUMBER_TABLE; length DBMS_DESCRIBE.NUMBER_TABLE; precision DBMS_DESCRIBE.NUMBER_TABLE; scale DBMS_DESCRIBE.NUMBER_TABLE; radix DBMS_DESCRIBE.NUMBER_TABLE; spare DBMS_DESCRIBE.NUMBER_TABLE; idx INTEGER := 0; BEGIN DBMS_DESCRIBE.DESCRIBE_PROCEDURE( name, null, null, overload, position, c_level, arg_name, dty, def_val, p_mode, length, precision, scale, radix, spare); DBMS_OUTPUT.PUT_LINE('Position Name DTY Mode'); LOOP idx := idx + 1; prt_value(TO_CHAR(position(idx)), 12); prt_value(arg_name(idx), 12); prt_value(TO_CHAR(dty(idx)), 5); prt_value(TO_CHAR(p_mode(idx)), 5); DBMS_OUTPUT.NEW_LINE; END LOOP; EXCEPTION WHEN NO_DATA_FOUND THEN DBMS_OUTPUT.NEW_LINE; DBMS_OUTPUT.NEW_LINE; END desc_proc; END describe_it; Then the results list all the numeric codes for the PL/SQL datatypes: Position Name Datatype_Code Mode 1 PVC2 1 0 2 PVC 1 1 3 PSTR 1 2 4 PLONG 8 0 5 PROWID 11 0 6 PCHARA 96 0 7 PCHAR 96 0 8 PRAW 23 0 9 PLRAW 24 0 10 PBININT 3 0 11 PPLSINT 3 0 12 PBOOL 252 0 13 PNAT 3 0 14 PPOS 3 0 15 PPOSN 3 0 16 PNATN 3 0 17 PNUM 2 0 18 PINTGR 2 0 19 PINT 2 0 20 PSMALL 2 0 21 PDEC 2 0 22 PREAL 2 0 23 PFLOAT 2 0 24 PNUMER 2 0 25 PDP 2 0 26 PDATE 12 0 27 PMLS 106 0