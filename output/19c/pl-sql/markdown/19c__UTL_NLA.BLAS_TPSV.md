---
id: 19c__UTL_NLA.BLAS_TPSV
name: UTL_NLA.BLAS_TPSV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_TPSV

This procedure solves one of the systems of equations A*x = b or A'*x = b , where b and x are n element vectors and A is an n by n unit, or non-unit, upper or lower triangular matrix, supplied in packed form.

## Syntax

```sql
UTL_NLA.BLAS_TPSV (
   uplo   IN      flag,
   trans  IN      flag,
   diag   IN      flag,
   n      IN      POSITIVEN,
   ap     IN      UTL_NLA_ARRAY_DBL,
   x      IN OUT  UTL_NLA_ARRAY_DBL,
   incx   IN      POSITIVEN,
   pack   IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uplo | flag | IN | Specifies whether the matrix is an upper or lower triangular matrix: uplo = 'U' or 'u' : A is an upper triangular matrix. uplo = 'L' or 'l' : A is a lower triangular matrix. |
| trans | flag | IN | Specifies the operation to be performed: trans = 'N' or 'n' : A*x = b trans = 'T' or 't' : A'*x = b trans = ' C' or 'c' : A'*x = b |
| diag | flag | IN | Specifies whether or not A is unit triangular: diag = 'U' or 'u' : A is assumed to be unit triangular. diag = 'N' or 'n' : 'A is not assumed to be unit triangular. |
| n | POSITIVEN | IN | Specifies the order of the matrix A . n must be at least zero. |
| ap | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ((n*(n+1))/2) Before entry with uplo = 'U' or 'u' , the array ap must contain the upper triangular matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(1,2) and a(2,2) respectively, and so on. Before entry with uplo = 'L' or 'l' , the array ap must contain the lower triangular matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(2,1) and a(3,1) respectively, and so on. Note that when diag = 'U' or 'u' , the diagonal elements of A are not referenced, but are assumed to be unity. |
| x | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 ) *abs( incx ) ) Before entry, the incremented array X must contain the n element right-hand side vector b . On exit, X is overwritten with the solution vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_TPSV ( uplo IN flag, trans IN flag, diag IN flag, n IN POSITIVEN, ap IN UTL_NLA_ARRAY_DBL, x IN OUT UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_TPSV ( uplo IN flag, trans IN flag, diag IN flag, n IN POSITIVEN, ap IN UTL_NLA_ARRAY_FLT, x IN OUT UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-34 BLAS_TPSV Procedure Parameters Parameter Description uplo Specifies whether the matrix is an upper or lower triangular matrix: uplo = 'U' or 'u' : A is an upper triangular matrix. uplo = 'L' or 'l' : A is a lower triangular matrix. trans Specifies the operation to be performed: trans = 'N' or 'n' : A*x = b trans = 'T' or 't' : A'*x = b trans = ' C' or 'c' : A'*x = b diag Specifies whether or not A is unit triangular: diag = 'U' or 'u' : A is assumed to be unit triangular. diag = 'N' or 'n' : 'A is not assumed to be unit triangular. n Specifies the order of the matrix A . n must be at least zero. ap UTL_NLA_ARRAY_FLT / DBL of dimension at least ((n*(n+1))/2) Before entry with uplo = 'U' or 'u' , the array ap must contain the upper triangular matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(1,2) and a(2,2) respectively, and so on. Before entry with uplo = 'L' or 'l' , the array ap must contain the lower triangular matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(2,1) and a(3,1) respectively, and so on. Note that when diag = 'U' or 'u' , the diagonal elements of A are not referenced, but are assumed to be unity. x UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 ) *abs( incx ) ) Before entry, the incremented array X must contain the n element right-hand side vector b . On exit, X is overwritten with the solution vector x . incx Specifies the increment for the elements of x . incx must not be zero. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major Usage Notes No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.