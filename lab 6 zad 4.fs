open System

let formatData (data: string) : string =
    let segments = data.Split(';') |> Array.map (fun x -> x.Trim())
    if segments.Length = 3 then
        let name = segments.[0]
        let surname = segments.[1]
        let years = segments.[2]
        sprintf "%s, %s (%s years old)" surname name years
    else
        "Invalid data format"

[<EntryPoint>]
let startProcess args =
    printfn "Wprowadź dane w formacie 'imię; nazwisko; wiek', oddzielając je nowymi liniami. Aby zakończyć, naciśnij Enter na pustej linii."
    let rec gatherData accumulated =
        let input = Console.ReadLine()
        if String.IsNullOrWhiteSpace(input) then accumulated
        else gatherData (input :: accumulated)
    let userData = gatherData [] |> List.rev
    let formattedData = userData |> List.map formatData
    printfn "Zaktualizowane dane:"
    formattedData |> List.iter (printfn "%s")
    0
