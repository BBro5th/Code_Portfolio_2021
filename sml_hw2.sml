(* SML comments appear like this *)
(* Bradley Brosovich*)

(* #1 - quicksort *)
(*partion fun*)
fun helphi (nil, p) = [] (*makes list of values higher than p in list a*)
| helphi (first::rest, p) = if (first > p) then [first] @ helphi (rest,p) 
else [] @ helphi(rest,p);

fun helplo (nil, p) = [] (*makes list of values lower than p in list a*)
| helplo (first::rest, p) = if (first < p) then [first] @ helplo(rest, p) 
else [] @ helplo(rest, p);

fun partition (nil, pivot) = ([],[]) (*uses help functions to create two lists*)
| partition (x, pivot) = 
(helplo(x, pivot) , helphi(x, pivot))
 ;

(*quicksort fun*)
fun quicksort nil = []
| quicksort [a] = [a]
| quicksort (first::rest)=
	let
	val (below,above) = partition(rest,first)
	in
	quicksort(below) @ [first] @ quicksort(above) (*pivot/quicksorts recursively*)
end;


(* #2 - member *) (*first is list, then the element looked for*)
fun member (e, nil) = false (*no list means false*)
| member (e, first::rest) = if e = first then true (*if first is same then true, else go on*)
else member (e,rest);
               
               
(* #3 - returns the union of sets (lists) s1 and s2*)
(* You may assume that s1 and s2 do not have any duplicate elements *) (*need to do different*)

fun bunion (nil,nil) = [] (*if elements are shared then it is skipped, then conncatonates at the end*)
| bunion (a,[]) = a
| bunion ([], b) = b
| bunion (a::ax, b) = if member(a,b) then bunion(ax,b)
else [a] @ bunion(ax , b);

fun union (a) = quicksort (bunion(a)); (*sorts the conjoined lists*)

;


(* #4 - returns the intersection of sets (lists) s1 and s2 *)
(* You may assume that s1 and s2 do not have any duplicate elements *)
(*I need to look at one element and iterate trough the list finding if theres a match*)
(* I can use member*)

fun intersection (nil,nil) = [] 
| intersection (s1, nil) = []
| intersection (nil, s2) = [] (*if there is a nil list, then no intersection*)
| intersection (s1::s1z, s2) = if member (s1, s2) then [s1] @ intersection(s1z,s2) (*if there is a member, add to interection list*)
else intersection(s1z,s2)
;

(* #5 - Return list of integers from start (inclusive) to stop (exclusive) by step *) (*~1*)
fun range(start, 0, step) = []
| range(start, stop, step) = if step > 0 then (*initial if else for between step of postive or negative*)
if start >= stop then [] else [start] @ range((start + step), stop, step)
else if start = stop then [] else [start] @ range((start + step), stop, step)
;

(* #6 - Return a slice of a list between indices start inclusive, and stop exclusive. Assume first element of list is at index 0*)
fun slice(aList, start, 0) = nil (*Finished condition*)
| slice (a::ax, start, stop) = if start =0(*goes through the list, returning list elements*)
	then [a] @ slice (ax, start, (stop -1))
	else slice (ax, (start-1), (stop-1)) (*Start is not zero, so will subtract from both start and stop, moves onto rest of list*)
;