let rec sequenceCalc x =
    if x <= 1 then x
    else sequenceCalc (x - 1) + sequenceCalc (x - 2)

let sequenceOptimized y =
    let rec helper p q r =
        if r = 0 then p
        else helper q (p + q) (r - 1)
    helper 0 1 y

[<EntryPoint>]
let main args =
    printfn "Obliczanie ciagu rekurencyjnie:"
    printfn "sequenceCalc(10) = %d" (sequenceCalc 10)
    printfn "sequenceOptimized(10) = %d" (sequenceOptimized 10)
    
    printfn "sequenceCalc(15) = %d" (sequenceCalc 15)
    printfn "sequenceOptimized(15) = %d" (sequenceOptimized 15)
    
    0
