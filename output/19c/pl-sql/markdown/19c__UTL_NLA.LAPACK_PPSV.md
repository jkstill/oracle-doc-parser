---
id: 19c__UTL_NLA.LAPACK_PPSV
name: UTL_NLA.LAPACK_PPSV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_PPSV

This procedure computes the solution to a real system of linear equations a * x = b where a is an n by n symmetric positive definite matrix stored in packed format and x and b are n by nrhs matrices.

## Syntax

```sql
UTL_NLA.LAPACK_PPSV (
   uplo      IN      flag,
   n         IN      POSITIVEN,
   nrhs      IN      POSITIVEN,
   ap        IN OUT  UTL_NLA_ARRAY_DBL,
   b         IN OUT  UTL_NLA_ARRAY_DBL,
   ldb       IN      POSITIVEN,
   info      OUT     INTEGER,
   pack      IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uplo | flag | IN | uplo = 'U' . Upper triangular of A is stored. uplo = 'L' . Lower triangular of A is stored. |
| n | POSITIVEN | IN | The number of linear equations, that is, the order of the matrix a . n >= 0 |
| nrhs | POSITIVEN | IN | The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . |
| ap | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n*(n+1)/2) . On entry, the upper or lower triangle of the symmetric matrix a , packed columnwise in a linear array. The j -th column of a is stored in the array ap as follows: If uplo = 'U' , AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; If uplo = ' L ', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n; On exit, if info = 0, the factor U or 'L' from the Cholesky factorization A = U**T*U or A = L*L**T in the same storage format as A . |
| b | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . |
| ldb | POSITIVEN | IN | The leading dimension of the array b. ldb >= max(1,n) |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the leading minor of order i of a is not positive definite, so the factorization could not be completed, and the solution has not been computed. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

The Cholesky decomposition is used to factor A as A = U**T* U if UPLO = 'U' or A = L * L**T if UPLO = 'L' where U is an upper triangular matrix and L is a lower triangular matrix. The factored form of A is then used to solve the system of equations A * X = B . See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_PPSV ( uplo IN flag, n IN POSITIVEN, nrhs IN POSITIVEN, ap IN OUT UTL_NLA_ARRAY_DBL, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_PPSV ( uplo IN flag, n IN POSITIVEN, nrhs IN POSITIVEN, ap IN OUT UTL_NLA_ARRAY_FLT, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-49 LAPACK_PPSV Procedure Parameters Parameter Description uplo uplo = 'U' . Upper triangular of A is stored. uplo = 'L' . Lower triangular of A is stored. n The number of linear equations, that is, the order of the matrix a . n >= 0 nrhs The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . ap UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n*(n+1)/2) . On entry, the upper or lower triangle of the symmetric matrix a , packed columnwise in a linear array. The j -th column of a is stored in the array ap as follows: If uplo = 'U' , AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; If uplo = ' L ', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n; On exit, if info = 0, the factor U or 'L' from the Cholesky factorization A = U**T*U or A = L*L**T in the same storage format as A . b UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . ldb The leading dimension of the array b. ldb >= max(1,n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the leading minor of order i of a is not positive definite, so the factorization could not be completed, and the solution has not been computed. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major