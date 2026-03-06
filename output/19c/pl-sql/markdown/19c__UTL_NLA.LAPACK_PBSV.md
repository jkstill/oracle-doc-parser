---
id: 19c__UTL_NLA.LAPACK_PBSV
name: UTL_NLA.LAPACK_PBSV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_PBSV

This procedure computes the solution to a real system of linear equations a * x = b , where a is an n by n symmetric positive definite band matrix and x and b are n by nrhs matrices.

## Syntax

```sql
UTL_NLA.LAPACK_PBSV (
uplo       IN      flag,
n          IN      POSITIVEN,
kd         IN      NATURALN,
nrhs       IN      POSITIVEN,
ab         IN OUT  UTL_NLA_ARRAY_DBL,
ldab       IN      POSITIVEN,
b          IN OUT  UTL_NLA_ARRAY_DBL,
ldb        IN      POSITIVEN,
info       OUT     INTEGER,
pack       IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uplo | flag | IN | uplo = 'U' . Upper triangular of A is stored. uplo = 'L' . Lower triangular of A is stored. |
| n | POSITIVEN | IN | The number of linear equations, that is, the order of the matrix a . n >= 0 |
| kd | NATURALN | IN | The number of superdiagonals of the matrix A if uplo = 'U' , or the number of subdiagonals if UPLO = 'L'. KD >= 0. |
| nrhs | POSITIVEN | IN | The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . |
| ab | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldab, n) . On entry, the upper or lower triangle of the symmetric band matrix a , stored in the first kd+1 rows of the array. The j -th column of a is stored in the j -th column of the array ab is as follows: if uplo = 'U' , AB(KD+1+i-j,j) = A(i,j) for max(1,j-KD)<=i<=j; if uplo = 'L' , AB(1+i-j,j) = A(i,j) for j<=i<=min(N,j+KD) .See below for further details.On exit, if info = 0 , the triangular factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T of the bandmatrix A , in the same storage format as a . |
| ldab | POSITIVEN | IN | The leading dimension of the array ab . ldb >= kd+1 |
| b | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . |
| ldb | POSITIVEN | IN | The leading dimension of the array b . ldb >= max(1,n) |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the leading minor of order i of a is not positive definite, so the factorization could not be completed, and the solution has not been computed. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

The Cholesky decomposition is used to factor A as A = U**T*U if UPLO ='U' or A = L * L**T if UPLO = 'L' where U is an upper triangular matrix and L is a lower triangular matrix. The factored form of A is then used to solve the system of equations A * X = B . See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_PBSV ( uplo IN flag, n IN POSITIVEN, kd IN NATURALN, nrhs IN POSITIVEN, ab IN OUT UTL_NLA_ARRAY_DBL, ldab IN POSITIVEN, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_PBSV ( uplo IN flag, n IN POSITIVEN, kd IN NATURALN, nrhs IN POSITIVEN, ab IN OUT UTL_NLA_ARRAY_FLT, ldab IN POSITIVEN, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-47 LAPACK_PBSV Procedure Parameters Parameter Description uplo uplo = 'U' . Upper triangular of A is stored. uplo = 'L' . Lower triangular of A is stored. n The number of linear equations, that is, the order of the matrix a . n >= 0 kd The number of superdiagonals of the matrix A if uplo = 'U' , or the number of subdiagonals if UPLO = 'L'. KD >= 0. nrhs The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . ab UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldab, n) . On entry, the upper or lower triangle of the symmetric band matrix a , stored in the first kd+1 rows of the array. The j -th column of a is stored in the j -th column of the array ab is as follows: if uplo = 'U' , AB(KD+1+i-j,j) = A(i,j) for max(1,j-KD)<=i<=j; if uplo = 'L' , AB(1+i-j,j) = A(i,j) for j<=i<=min(N,j+KD) .See below for further details.On exit, if info = 0 , the triangular factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T of the bandmatrix A , in the same storage format as a . ldab The leading dimension of the array ab . ldb >= kd+1 b UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . ldb The leading dimension of the array b . ldb >= max(1,n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the leading minor of order i of a is not positive definite, so the factorization could not be completed, and the solution has not been computed. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major