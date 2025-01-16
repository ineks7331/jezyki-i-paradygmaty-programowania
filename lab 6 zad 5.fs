open System

let getLongestWord (content: string) : string * int =
    content.Split([|' '; '\t'; '\n'|], StringSplitOptions.RemoveEmptyEntries)
    |> Array.fold (fun (currentWord, maxLen) word ->
        if word.Length > maxLen then (word, word.Length)
        else (currentWord, maxLen)
    ) ("", 0)

[<EntryPoint>]
let runApp args =
    printfn "Wprowadź tekst:"
    let userInput = Console.ReadLine()
    let longest, wordLength = getLongestWord userInput
    printfn "Najdłuższe słowo: %s" longest
    printfn "Długość najdłuższego słowa: %d" wordLength
    0
