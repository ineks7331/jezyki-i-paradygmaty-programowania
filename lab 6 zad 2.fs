open System

let checkPalindrome (inputText: string) : bool =
    let normalizedText = inputText.ToLower().Replace(" ", "").Replace("\t", "")
    normalizedText = String(normalizedText.ToCharArray() |> Array.rev)

[<EntryPoint>]
let main args =
    printfn "Podaj tekst:"
    let userInput = Console.ReadLine()
    if checkPalindrome userInput then
        printfn "Podany ciąg jest palindromem"
    else
        printfn "Podany ciąg nie jest palindromem"
    0
