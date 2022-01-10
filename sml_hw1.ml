(* SML comments appear like this *)
(* Bradley B *)

(* #1 - pow *) (*Should recurssively visit until b would be 0, ie a*a*a*1 *)
fun pow (a, b) = if b = 0 then 1
else a * pow(a,b-1);


(* #2 - sumTo *)
fun sumTo x = if x = 0 then 0.0 
else 1 div x + sumTo(x-1); (* this should create the smallest (1/x) then continue iterating until x=0 which adds 0 *)
               
               
(* #3 - repeat *) (* ment to iterate until n = 0, the concatenate each repeated word together*)
fun repeat (s, n) = if n = 0 then ""
else s ^ repeat(s, n-1);


(* #4 - binary *) (*manual transversion requires division of 2 with remainders becoming the binary, in inverse order*)
fun binary x = if x < 2 then (string)x 
else Integer.toString(x mod 2)  ^ binary(x/2); (*how make int to string directly*)

(* #5 - countNegative *) (*#2 list = 2nd element of list*)
fun countNegative x = 
if null x then 0 (*sees if empty list*)
else 
if hd x < 0 then 1+ countNegative (tl x) (*will look at list -hd after finding negative*)
else countNegative (tl x) ;


(* #6 - absList *)
fun helpLab y = (*help function to handle a tuple*)
if null y then nil
else (abs(hd y), helpLab(tl y)); 
fun absList x = 
if x null then nil (*if there is no list element, or until tl below brings no list element*)
else [helpLab (hd x)] @ absList (tl x); (*should do the abs of tuples and contatanate it as a list, to recursively done next list*)


(* #7 - split *)
fun helpSplit y = (*take an int and make tuple of two ints*)
if y mod 2 = 0 then (y div 2, y div 2)
else ((y div 2)+1, y div 2);
fun split x = (*just create a list element and concatinate to recursively done list elements*)
if x null then nil
else [helpSplit (hd x)] @ split (tl x);


(* #8 - isSorted *)
fun isSorted x = 
if length (x) <= 1 then true (*checking if size 1 or less*)
else
if hd x < isSorted(tl x) then true
else false;

(* #9 - collapse *) 
fun collapse x = 
if length (x) <=1 then x
else [#1 x + #2 x] @ collapse (tl (tl (x)) ;

        
(* #10 - insert *)        
fun insert (n, x) = 
if x null then [n] @ x
else
if n < hd x then [n] @ x
else [hd x] @ insert (n,tl x);
