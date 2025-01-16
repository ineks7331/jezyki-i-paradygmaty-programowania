type TreeStructure<'T> =
    | Null
    | Branch of 'T * TreeStructure<'T> * TreeStructure<'T>

let rec findElement key structure =
    match structure with
    | Null -> false
    | Branch(v, left, right) ->
        if v = key then true
        else findElement key left || findElement key right

let findElementIterative key structure =
    let rec traverse stack =
        match stack with
        | [] -> false
        | Null :: rest -> traverse rest
        | Branch(v, left, right) :: rest ->
            if v = key then true
            else traverse (left :: right :: rest)
    traverse [structure]

[<EntryPoint>]
let main args =
    let exampleTree = Branch(10, Branch(5, Null, Null), Branch(20, Null, Branch(25, Null, Null)))
    
    printfn "Rekurencyjne wyszukiwanie:"
    printfn "Czy wartość 25 jest w drzewie? %b" (findElement 25 exampleTree)
    printfn "Czy wartość 15 jest w drzewie? %b" (findElement 15 exampleTree)

    printfn "Iteracyjne wyszukiwanie:"
    printfn "Czy wartość 25 jest w drzewie? %b" (findElementIterative 25 exampleTree)
    printfn "Czy wartość 15 jest w drzewie? %b" (findElementIterative 15 exampleTree)

    0
