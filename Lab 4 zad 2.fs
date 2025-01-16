open System

// Funkcja licząca słowa
let countWords (text: string) =
    text.Split([|' '; '\n'; '\t'|], StringSplitOptions.RemoveEmptyEntries) |> Array.length

// Funkcja licząca znaki (bez spacji)
let countChars (text: string) =
    text.Replace(" ", "").Length

// Funkcja znajdująca najczęściej występujące słowo
let findMostFrequentWord (text: string) =
    let words = text.Split([|' '; '\n'; '\t'|], StringSplitOptions.RemoveEmptyEntries)
    let wordCounts = words |> Array.groupBy id |> Array.map (fun (word, occurrences) -> (word, occurrences.Length))
    let maxOccurrence = wordCounts |> Array.maxBy snd
    fst maxOccurrence

// Główna funkcja
[<EntryPoint>]
let main argv =
    printfn "Wprowadź tekst do analizy:"
    let text = Console.ReadLine()

    let wordCount = countWords text
    let charCount = countChars text
    let mostFrequentWord = findMostFrequentWord text

    printfn "Liczba słów: %d" wordCount
    printfn "Liczba znaków (bez spacji): %d" charCount
    printfn "Najczęściej występujące słowo: %s" mostFrequentWord

    0
