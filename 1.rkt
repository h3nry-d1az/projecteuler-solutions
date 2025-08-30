#lang racket

(print
 (apply +
        (filter (λ (n) (or (= 0 (modulo n 3))
                           (= 0 (modulo n 5))))
                (range 1000))))