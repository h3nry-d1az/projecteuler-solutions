#lang racket

(define (minimum-divisor m n)
    (if (= 0 (modulo m n)) n (minimum-divisor m (+ 1 n))))

(define (prime-factors n)
    (if (= n 1) (set)
        (let ([m (minimum-divisor n 2)])
            (set-union (set m) (prime-factors (/ n m))))))

(println (apply max ((compose set->list prime-factors) 600851475143)))