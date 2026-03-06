---
id: 19c__UTL_NLA.LAPACK_PTSV
name: UTL_NLA.LAPACK_PTSV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_PTSV

This procedure computes the solution to a real system of linear equations a * x = b , where a is an n by n symmetric positive definite tridiagonal matrix, and x and b are n by nrhs matrices.

## Syntax

```sql
UTL_NLA.LAPACK_PTSV (
   n      IN       POSITIVEN,
   nrhs   IN       POSITIVEN,
   d      IN OUT   UTL_NLA_ARRAY_DBL,
   e      IN OUT   UTL_NLA_ARRAY_DBL,
   b      IN OUT   UTL_NLA_ARRAY_DBL,
   ldb    IN       POSITIVEN,
   info   OUT      INTEGER,
   pack   IN       flag  DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | POSITIVEN | IN | The order of the matrix a. N >= 0 . |
| nrhs | POSITIVEN | IN | The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . |
| d | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n) . On entry, the n diagonal elements of the tridiagonal matrix a . On exit, the n diagonal elements of the diagonal matrix d from the factorization A = L*D*L**T . |
| e | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n-1) . On entry, the (n-1) subdiagonal elements of the tridiagonal matrix a . On exit, the (n-1) diagonal elements of the unit bidiagonal factor L from the factorization A = L*D*L**T of a .( e can also be regarded as the superdiagonal of the unit bidiagonal factor U from the U**T*D*U factorization of a ) |
| b | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . |
| ldb | POSITIVEN | IN | The leading dimension of the array b . ldb >= max(1,n) |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the leading minor of order i of a is not positive definite, so the factorization could not be completed, and the solution has not been computed. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

a is factored as A = L*D*L**T , and the factored form of a is then used to solve the system of equations. See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_PTSV ( n IN POSITIVEN, nrhs IN POSITIVEN, d IN OUT UTL_NLA_ARRAY_DBL, e IN OUT UTL_NLA_ARRAY_DBL, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_PTSV ( n IN POSITIVEN, nrhs IN POSITIVEN, d IN OUT UTL_NLA_ARRAY_FLT, e IN OUT UTL_NLA_ARRAY_FLT, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-50 LAPACK_PTSV Procedure Parameters Parameter Description n The order of the matrix a. N >= 0 . nrhs The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . d UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n) . On entry, the n diagonal elements of the tridiagonal matrix a . On exit, the n diagonal elements of the diagonal matrix d from the factorization A = L*D*L**T . e UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n-1) . On entry, the (n-1) subdiagonal elements of the tridiagonal matrix a . On exit, the (n-1) diagonal elements of the unit bidiagonal factor L from the factorization A = L*D*L**T of a .( e can also be regarded as the superdiagonal of the unit bidiagonal factor U from the U**T*D*U factorization of a ) b UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . ldb The leading dimension of the array b . ldb >= max(1,n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the leading minor of order i of a is not positive definite, so the factorization could not be completed, and the solution has not been computed. pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major