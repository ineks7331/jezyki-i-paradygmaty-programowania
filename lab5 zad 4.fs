let rec solveHanoi disks start endPeg tempPeg =
    if disks = 1 then
        printfn "Przenieś krążek z %s do %s" start endPeg
    else
        solveHanoi (disks - 1) start tempPeg endPeg
        printfn "Przenieś krążek z %s do %s" start endPeg
        solveHanoi (disks - 1) tempPeg endPeg start

let solveHanoiIter disks start endPeg tempPeg =
    let totalMoves = pown 2 disks - 1
    for step in 1 .. totalMoves do
        let from = 
            match (step &&& step - 1) % 3 with
            | 0 -> start
            | 1 -> tempPeg
            | _ -> endPeg
        let to = 
            match ((step ||| step - 1) + 1) % 3 with
            | 0 -> start
            | 1 -> tempPeg
            | _ -> endPeg
        printfn "Przenieś krążek z %s do %s" from to

[<EntryPoint>]
let main args =
    let diskCount = 3
    printfn "Rekurencyjne rozwiązanie problemu wież Hanoi:"
    solveHanoi diskCount "A" "C" "B"

    printfn "\nIteracyjne rozwiązanie problemu wież Hanoi:"
    solveHanoiIter diskCount "A" "C" "B"

    0
