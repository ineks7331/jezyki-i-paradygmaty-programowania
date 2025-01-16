open System

// Mapowanie kursów wymiany (przykład kursów)
let exchangeRates = 
    Map.ofList [
        ("USD", 1.0);  // 1 USD = 1 USD
        ("EUR", 0.94); // 1 USD = 0.94 EUR
        ("GBP", 0.83)  // 1 USD = 0.83 GBP
    ]

// Funkcja konwertująca walutę
let convertCurrency (amount: float) (fromCurrency: string) (toCurrency: string) =
    match Map.tryFind fromCurrency exchangeRates, Map.tryFind toCurrency exchangeRates with
    | Some(fromRate), Some(toRate) -> 
        amount * (toRate / fromRate)  // Przeliczanie kwoty
    | _ -> 
        printfn "Błąd: Niepoprawna waluta!"
        0.0

// Główna funkcja
[<EntryPoint>]
let main argv =
    // Odczyt kwoty do przeliczenia
    printfn "Podaj kwotę do przeliczenia:"
    let amount = Console.ReadLine() |> float

    // Odczyt waluty źródłowej
    printfn "Podaj walutę źródłową (np. USD, EUR, GBP):"
    let fromCurrency = Console.ReadLine()

    // Odczyt waluty docelowej
    printfn "Podaj walutę docelową (np. USD, EUR, GBP):"
    let toCurrency = Console.ReadLine()

    // Przeliczenie waluty
    let result = convertCurrency amount fromCurrency toCurrency

    // Wyświetlenie przeliczonej kwoty
    if result > 0.0 then
        printfn "Przeliczona kwota: %.2f %s" result toCurrency

    0
