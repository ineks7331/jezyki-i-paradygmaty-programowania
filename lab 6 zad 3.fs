open System

let filterWords (inputList: string list) : string list =
    inputList |> List.distinct

[<EntryPoint>]
let startApp args =
    printfn "Wprowadź tekst oddzielony spacjami:"
    let userInput = Console.ReadLine()
    let items = userInput.Split(' ') |> Array.toList
    let distinctItems = filterWords items
    printfn "Wynik: %A" distinctItems
    0
