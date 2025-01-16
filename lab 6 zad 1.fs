open System

let calculateWordCount (inputText: string) : int =
    inputText.Split([|' '; '\t'; '\n'|], StringSplitOptions.RemoveEmptyEntries).Length

let calculateCharCountWithoutSpaces (inputText: string) : int =
    inputText.Replace(" ", "").Length

[<EntryPoint>]
let main args =
    printfn "Podaj tekst:"
    let userInput = Console.ReadLine()
    let wordTotal = calculateWordCount userInput
    let charTotal = calculateCharCountWithoutSpaces userInput
    printfn "Liczba słów: %d" wordTotal
    printfn "Liczba znaków (bez spacji): %d" charTotal
    0
