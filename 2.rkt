#lang racket

(define (fib n)
    (if (<= n 1)
        1
        (+ (fib (- n 1)) (fib (- n 2)))))

(define (main n)
    (define f (fib n))
    (if (> (fib n) 4000000) 0
        (+ (if (even? f) f 0) (main (+ n 1)))))

(println (main 1))