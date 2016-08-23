SUBROUTINE testfunc(x, y)
    IMPLICIT NONE

    !threadsafe

    INTEGER, INTENT(IN) :: x
    INTEGER, INTENT(OUT) :: y

    y = x + 1

    RETURN

END SUBROUTINE testfunc
