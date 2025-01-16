let rec generatePermutations items =
    match items with
    | [] -> [[]]
    | _ -> 
        items
        |> List.collect (fun element -> 
            let remaining = List.filter ((<>) element) items
            generatePermutations remaining |> List.map (fun perm -> element :: perm))

[<EntryPoint>]
let main args =
    let sampleList = [1; 2; 3]
    let result = generatePermutations sampleList

    printfn "Permutacje listy %A:" sampleList
    result |> List.iter (fun perm -> printfn "%A" perm)

    0
