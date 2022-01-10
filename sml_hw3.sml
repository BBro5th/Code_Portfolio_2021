(* SML comments appear like this *)
(* Bradly B*)

(* #1 - duplist *)
fun duplist x = foldr (fn(a,b) => a::a::b) [] x;

(* #2 - mylength *)
fun mylength x = foldr (op +) 0 (map (fn a => a div a) x);

(* #3 - il2absrl *)
fun il2absrl x = map (op real) (map(fn x => if x > 0 then x*1 else x * ~1) x);

(* #4 - myimplode *)
fun myimplode x = foldr (fn (a,b) => a^b) "" (map (fn a => str(a)) x);

(* #5 - lconcat *)
fun lconcat x = foldr (fn (a,b) => a@b) [] x; (*Closer to how this might work*)

(* #6 - convert *)
fun convert x = (nil,nil) ;
(*[(foldr (fn (a,b) => a::b) [] x) ,(foldr (fn (a::ax,b::bx) => ax::bx) [] x)];*)

(* #7 - mymap *)
fun mymap f x = foldr (fn (a,b) => (f a)::b ) [] x; (*works *)

(* #8 - myfoldl *)
fun myfoldl f initialValue aList = 0;
(*
fun myfoldl f initialValue [] = initialValue
| myfoldl f initialValue aList = myfoldl f (f(hd aList )initialValue tl aList;*)

