open System

// Definicja rekordu dla konta bankowego
type BankAccount = { AccountNumber: string; mutable Balance: float }

// Mapa przechowująca konta
let accounts = ref Map.empty<string, BankAccount>

// Funkcja do tworzenia konta
let createAccount (accountNumber: string) =
    if accounts.Value |> Map.containsKey accountNumber then
        printfn "Konto o tym numerze już istnieje."
    else
        let newAccount = { AccountNumber = accountNumber; Balance = 0.0 }
        accounts := Map.add accountNumber newAccount accounts.Value
        printfn "Konto o numerze %s zostało utworzone." accountNumber

// Funkcja do depozytowania środków
let deposit (accountNumber: string) (amount: float) =
    match accounts.Value |> Map.tryFind accountNumber with
    | Some(account) -> 
        account.Balance <- account.Balance + amount
        printfn "Złożono %.2f na konto %s. Nowe saldo: %.2f" amount accountNumber account.Balance
    | None -> printfn "Konto nie istnieje."

// Funkcja do wypłacania środków
let withdraw (accountNumber: string) (amount: float) =
    match accounts.Value |> Map.tryFind accountNumber with
    | Some(account) when account.Balance >= amount -> 
        account.Balance <- account.Balance - amount
        printfn "Wypłacono %.2f z konta %s. Nowe saldo: %.2f" amount accountNumber account.Balance
    | Some(_) -> printfn "Brak wystarczających środków."
    | None -> printfn "Konto nie istnieje."

// Funkcja do wyświetlania salda
let displayBalance (accountNumber: string) =
    match accounts.Value |> Map.tryFind accountNumber with
    | Some(account) -> printfn "Saldo konta %s: %.2f" accountNumber account.Balance
    | None -> printfn "Konto nie istnieje."

// Główna funkcja
[<EntryPoint>]
let main argv =
    let rec menu () =
        printfn "1. Utwórz konto"
        printfn "2. Depozytuj środki"
        printfn "3. Wypłać środki"
        printfn "4. Wyświetl saldo"
        printfn "5. Zakończ"
        printf "Wybierz opcję: "
        let option = Console.ReadLine() |> int

        match option with
        | 1 -> 
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            createAccount accountNumber
            menu()
        | 2 -> 
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            printf "Podaj kwotę do depozytu: "
            let amount = Console.ReadLine() |> float
            deposit accountNumber amount
            menu()
        | 3 -> 
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            printf "Podaj kwotę do wypłaty: "
            let amount = Console.ReadLine() |> float
            withdraw accountNumber amount
            menu()
        | 4 -> 
            printf "Podaj numer konta: "
            let accountNumber = Console.ReadLine()
            displayBalance accountNumber
            menu()
        | 5 -> 
            printfn "Koniec programu."
        | _ -> 
            printfn "Niepoprawna opcja."
            menu()

    menu()
    0
