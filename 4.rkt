#lang racket

(define (next m n)
    (if (and (= m 999) (= n 999)) '(0 0)
        (if (= n 999) (list (+ 1 m) 100) (list m (+ 1 n)))))

(define (largest-palindrome m n)
    (if (= m n 0) 0
    (let ([p ((compose string->list number->string *) m n)])
        (if (equal? p (reverse p)) (max (* n m) (apply largest-palindrome (next m n)))
            (apply largest-palindrome (next m n))))))

(largest-palindrome 100 100)