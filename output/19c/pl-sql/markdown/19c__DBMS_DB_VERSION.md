---
id: 19c__DBMS_DB_VERSION
name: DBMS_DB_VERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DB_VERSION
tags: [dbms_db_version]
source_file: DBMS_DB_VERSION.html
---

# DBMS_DB_VERSION

This example uses conditional compilation to guard new features.

## Syntax

```sql
CREATE OR REPLACE PROCEDURE whetstone IS
 
 -- Notice that conditional compilation constructs
 -- can interrupt a regular PL/SQL statement.
 -- You can locate a conditional compilation directive anywhere
 -- there is whitespace in the regular statement.

 SUBTYPE my_real IS
    $IF DBMS_DB_VERSION.VER_LE_9 $THEN NUMBER
                                 $ELSE BINARY_DOUBLE
    $END;

 t  CONSTANT my_real := $IF DBMS_DB_VERSION.VER_LE_9 $THEN 0.499975 
                                                     $ELSE 0.499975d 
                        $END;

 t2 CONSTANT my_real := $if DBMS_DB_VERSION.VER_LE_9 $THEN 2.0
                                                     $ELSE 2.0d
                        $END;

 x  CONSTANT my_real := $IF DBMS_DB_VERSION.VER_LE_9 $THEN 1.0
                                                     $ELSE 1.0d
                        $END;

 y  CONSTANT my_real := $IF DBMS_DB_VERSION.VER_LE_9 $THEN 1.0
                                                     $ELSE 1.0d
                        $END;
 
 z  MY_REAL;
 
 PROCEDURE P(x IN my_real, y IN my_real, z OUT NOCOPY my_real) IS
   x1 my_real;
   y1 my_real;
 BEGIN
   x1 := x;
   y1 := y;
   x1 := t * (x1 + y1);
   y1 := t * (x1 + y1);
   z := (x1 + y1)/t2;
 END P;
BEGIN
 P(x, y, z);
 DBMS_OUTPUT.PUT_LINE ('z = '|| z);
END whetstone;
/
```

## Usage Notes

CREATE OR REPLACE PROCEDURE whetstone IS -- Notice that conditional compilation constructs -- can interrupt a regular PL/SQL statement. -- You can locate a conditional compilation directive anywhere -- there is whitespace in the regular statement. SUBTYPE my_real IS $IF DBMS_DB_VERSION.VER_LE_9 $THEN NUMBER $ELSE BINARY_DOUBLE $END; t CONSTANT my_real := $IF DBMS_DB_VERSION.VER_LE_9 $THEN 0.499975 $ELSE 0.499975d $END; t2 CONSTANT my_real := $if DBMS_DB_VERSION.VER_LE_9 $THEN 2.0 $ELSE 2.0d $END; x CONSTANT my_real := $IF DBMS_DB_VERSION.VER_LE_9 $THEN 1.0 $ELSE 1.0d $END; y CONSTANT my_real := $IF DBMS_DB_VERSION.VER_LE_9 $THEN 1.0 $ELSE 1.0d $END; z MY_REAL; PROCEDURE P(x IN my_real, y IN my_real, z OUT NOCOPY my_real) IS x1 my_real; y1 my_real; BEGIN x1 := x; y1 := y; x1 := t * (x1 + y1); y1 := t * (x1 + y1); z := (x1 + y1)/t2; END P; BEGIN P(x, y, z); DBMS_OUTPUT.PUT_LINE ('z = '|| z); END whetstone; /