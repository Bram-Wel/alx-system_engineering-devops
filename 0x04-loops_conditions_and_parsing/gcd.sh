#!/usr/bin/env bash
# gcd.sh: Calculates gcd with
# 	Euclid's theorm

# -----------------------------------------------
# Check Arguments
ARGS=2
E_BADARGS=85

if [ $# -ne "$ARGS" ]
then
  echo "Usage: $(basename "$0") first-no. 2nd-no."
  exit $E_BADARGS
fi
# ------------------------------------------------

gcd ()
{
  dividend=$1
  divisor=$2
  remainder=1		#Initialize to avoid error when
            		#+ bracketed
  until [ "$remainder" -eq 0 ]
  do
    ((remainder = dividend % divisor))
    dividend=$divisor
    divisor=$remainder
  done
}

gcd "$1" "$2"
echo "GCD of $1 & $2 = $dividend"; echo

exit 0
