
(* Scales.ml *)

(* type for pitch class *)
type pitch = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12

type mode_type = Major | NaturalMinor | HarmonicMinor 

module type PITCHES = 
  sig
  	type t
  	val c : t
  	val half_next : t -> t
  	val half_prev : t -> t
  	val half_next : t -> t
  	val half_prev : t -> t
  	val aug_next : t -> t
  	val aug_prev : t -> t
  	val jump : t -> int -> t
  	val octave : t -> t
  end

module Pitches : PITCHES =
  struct
    type t = pitch
    let c : t = 1
    let half_next (p : t) : t = let x = p + 1 in if x > 12 then 1 else x
    let half_prev (p : t) = let x = p - 1 in if x < 1 then 12 else x
    let whole_next (p : t) = half_next (half_next p)
    let whole_prev (p : t) = half_prev (half_prev p)
    let aug_next (p : t) = half_next (whole_next p)
    let aug_prev (p : t) = half_prev (whole_prev p)
    let jump (p : t) (n : int) = let x = ((p + n) % 12) in if x = 0 then 1 else x
    let octave (p : t) = (p + 12) % 12
  end

module type SCALES =
  functor (P : PITCHES) ->
  sig
    type p
    type t 
  	val empty : t
  	val construct : mode -> p -> t
  	val get_degree : t -> int -> p option
  	val get_mode : mode -> bool
  	val is_mode : mode -> bool
  end


module Scale (P : PITCHES) : SCALES = 
  struct
  	let p = P.t (* element of scale *)
  	let t = p list (* scale implemented as a list *)
    let empty = []
    let construct (m: mode) (pch: p) =
      match m with
      | Major -> P.jump p 2 :: P.jump p 4 :: P.jump p 5 :: 
                 P.jump p 7 :: P.jump p 9 :: P.jump p 11
      | NaturalMinor -> P.jump p 2 :: P.jump p 3 :: P.jump p 5 ::
                        P.jump p 7 :: P.jump p 8 :: P.jump p 11
      | HarmonicMinor -> P.jump p 2 :: P.jump p 3 :: P.jump p 5 ::
                         P.jump p 7 :: P.jump p 8 :: P.jump p 11
    let rec get_degree (scale : t) (n : int) =
      if n > 7 || n < 1 then
        (match scale with
        | [] -> None
        | hd :: tl -> if n = 1 then hd else get_degree tl (n-1))
      else None


 end






