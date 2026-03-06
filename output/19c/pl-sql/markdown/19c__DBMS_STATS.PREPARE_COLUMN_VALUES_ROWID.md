---
id: 19c__DBMS_STATS.PREPARE_COLUMN_VALUES_ROWID
name: DBMS_STATS.PREPARE_COLUMN_VALUES_ROWID
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.PREPARE_COLUMN_VALUES_ROWID

This procedure converts user-specified minimum, maximum, and histogram endpoint datatype-specific values into Oracle's internal representation for future storage using SET_COLUMN_STATS .

## Syntax

```sql
DBMS_STATS.PREPARE_COLUMN_VALUES_ROWID (
   srec  IN OUT StatRec, 
   rwmin        ROWID, 
   rwmax        ROWID);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| srec | StatRec | IN OUT | Values ( IN ): epc bkvals rpcnts Values ( OUT ): minval maxval bkvals novals eavals rpcnts |
| rwmin | ROWID | IN | Minimum value when the column type is rowid . No histogram information is provided for a column of this type. |
| rwmax | ROWID) | IN | Maximum value when the column type is rowid . No histogram information is provided for a column of this type. |

## Usage Notes

Syntax DBMS_STATS.PREPARE_COLUMN_VALUES_ROWID ( srec IN OUT StatRec, rwmin ROWID, rwmax ROWID); Pragmas pragma restrict_references(prepare_column_values_rowid, WNDS, RNDS, WNPS, RNPS); Parameters Table 171-93 PREPARE_COLUMN_VALUES_ROWID Procedure Parameters Parameter Description srec Values ( IN ): epc bkvals rpcnts Values ( OUT ): minval maxval bkvals novals eavals rpcnts rwmin Minimum value when the column type is rowid . No histogram information is provided for a column of this type. rwmax Maximum value when the column type is rowid . No histogram information is provided for a column of this type. Table 171-94 StatRec Record Type Fields Field Description epc ( IN) Number of values specified in charvals , datevals , dblvals , fltvals , numvals , or rawvals . This value must be between 2 and 2050, inclusive, and it should be set to 2 for procedures which do not allow histogram information ( nvarchar and rowid ). The first corresponding array entry should hold the minimum value for the column, and the last entry should hold the maximum. If there are more than two entries, then all the others hold the remaining height-balanced or frequency histogram endpoint values (with in-between values ordered from next-smallest to next-largest). This value may be adjusted to account for compression, so the returned value should be left as is for a call to SET_COLUMN_STATS . bkvals ( IN ) If you want a frequency or hybrid histogram, this array contains the number of occurrences of each distinct value specified in charvals , datevals , dblvals , fltvals , numvals , or rawvals . Otherwise, it is merely an output parameter, and it must be set to NULL when this procedure is called. rpcnts ( IN ) If you want a hybrid histogram, this array contains the total frequency of values that are less than or equal to each distinct value specified in charvals , datevals , numvals , or rawvals . Otherwise, it is merely an output argument and must be set to NULL when this procedure is called. As an example, for a given array numvals with numvals(i)=4, rpcnts(i)=13 means that there are 13 rows in the column which are less than or equal to 4. Note: Whenever srec.rpcnts is populated, srec.bkvals must be populated as described above. Whenever bkvals and/or rpcnts are populated, there should not be any duplicates in charvals , datevals , numvals , or rawvals . minval ( OUT ) Internal representation of the minimum suitable for use in a call to SET_COLUMN_STATS . maxval ( OUT ) Internal representation of the maximum suitable for use in a call to SET_COLUMN_STATS . bkvals ( OUT ) Array suitable for use in a call to SET_COLUMN_STATS . novals ( OUT ) Array suitable for use in a call to SET_COLUMN_STATS . eavals ( OUT ) Array suitable for use in a call to SET_COLUMN_STATS rpcnts ( OUT ) Array suitable for use in a call to SET_COLUMN_STATS Usage Notes No special privilege or role is needed to invoke this procedure.