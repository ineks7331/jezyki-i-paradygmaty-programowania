open System

type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages
    member this.GetInfo() = sprintf "Tytuł: %s, Autor: %s, Strony: %d" this.Title this.Author this.Pages

type User(name: string) =
    let mutable borrowedBooks = []
    member this.Name = name
    member this.BorrowBook(book: Book) =
        borrowedBooks <- book :: borrowedBooks
        printfn "%s wypożyczył(a) książkę: %s" this.Name book.Title
    member this.ReturnBook(book: Book) =
        if List.exists (fun b -> b = book) borrowedBooks then
            borrowedBooks <- List.filter (fun b -> b <> book) borrowedBooks
            printfn "%s zwrócił(a) książkę: %s" this.Name book.Title
        else
            printfn "Książka %s nie znajduje się na liście wypożyczonych książek użytkownika %s" book.Title this.Name
    member this.ListBorrowedBooks() =
        if borrowedBooks.IsEmpty then
            printfn "%s nie ma wypożyczonych książek" this.Name
        else
            printfn "Książki wypożyczone przez %s:" this.Name
            borrowedBooks |> List.iter (fun book -> printfn "- %s" book.Title)

type Library() =
    let mutable books = []
    let mutable users = []
    
    member this.AddBook(book: Book) =
        books <- book :: books
        printfn "Dodano książkę: %s" book.Title
    
    member this.AddUser(user: User) =
        users <- user :: users
        printfn "Dodano użytkownika: %s" user.Name

    member this.RemoveBook(book: Book) =
        if List.exists (fun b -> b = book) books then
            books <- List.filter (fun b -> b <> book) books
            printfn "Usunięto książkę: %s" book.Title
        else
            printfn "Książka %s nie znajduje się w bibliotece" book.Title
    
    member this.RemoveUser(user: User) =
        if List.exists (fun u -> u = user) users then
            users <- List.filter (fun u -> u <> user) users
            printfn "Usunięto użytkownika: %s" user.Name
        else
            printfn "Użytkownik %s nie znajduje się w systemie" user.Name

    member this.ListBooks() =
        if books.IsEmpty then
            printfn "Biblioteka jest pusta"
        else
            printfn "Książki dostępne w bibliotece:"
            books |> List.iter (fun book -> printfn "- %s" (book.GetInfo()))
    
    member this.ListUsers() =
        if users.IsEmpty then
            printfn "Brak użytkowników w systemie"
        else
            printfn "Użytkownicy w systemie:"
            users |> List.iter (fun user -> printfn "- %s" user.Name)

    member this.FindBookByTitle(title: string) =
        books |> List.tryFind (fun book -> book.Title = title)

    member this.FindUserByName(name: string) =
        users |> List.tryFind (fun user -> user.Name = name)

[<EntryPoint>]
let main argv =
    let library = Library()

    let rec showMenu () =
        printfn "Wybierz opcję:"
        printfn "1. Dodaj książkę"
        printfn "2. Dodaj użytkownika"
        printfn "3. Usuń książkę"
        printfn "4. Usuń użytkownika"
        printfn "5. Lista książek"
        printfn "6. Lista użytkowników"
        printfn "7. Wypożycz książkę"
        printfn "8. Zwróć książkę"
        printfn "9. Wyjście"
        let choice = Console.ReadLine()
        
        match choice with
        | "1" ->
            printfn "Podaj tytuł książki:"
            let title = Console.ReadLine()
            printfn "Podaj autora książki:"
            let author = Console.ReadLine()
            printfn "Podaj liczbę stron książki:"
            let pages = int (Console.ReadLine())
            let book = Book(title, author, pages)
            library.AddBook(book)
            showMenu()
        | "2" ->
            printfn "Podaj nazwisko użytkownika:"
            let name = Console.ReadLine()
            let user = User(name)
            library.AddUser(user)
            showMenu()
        | "3" ->
            printfn "Podaj tytuł książki do usunięcia:"
            let title = Console.ReadLine()
            match library.FindBookByTitle(title) with
            | Some(book) -> library.RemoveBook(book)
            | None -> printfn "Nie znaleziono książki o tytule %s" title
            showMenu()
        | "4" ->
            printfn "Podaj nazwisko użytkownika do usunięcia:"
            let name = Console.ReadLine()
            match library.FindUserByName(name) with
            | Some(user) -> library.RemoveUser(user)
            | None -> printfn "Nie znaleziono użytkownika o nazwisku %s" name
            showMenu()
        | "5" ->
            library.ListBooks()
            showMenu()
        | "6" ->
            library.ListUsers()
            showMenu()
        | "7" ->
            printfn "Podaj nazwisko użytkownika:"
            let name = Console.ReadLine()
            printfn "Podaj tytuł książki do wypożyczenia:"
            let title = Console.ReadLine()
            match library.FindUserByName(name), library.FindBookByTitle(title) with
            | Some(user), Some(book) -> user.BorrowBook(book)
            | Some(user), None -> printfn "Nie znaleziono książki o tytule %s" title
            | None, _ -> printfn "Nie znaleziono użytkownika o nazwisku %s" name
            showMenu()
        | "8" ->
            printfn "Podaj nazwisko użytkownika:"
            let name = Console.ReadLine()
            printfn "Podaj tytuł książki do zwrócenia:"
            let title = Console.ReadLine()
            match library.FindUserByName(name), library.FindBookByTitle(title) with
            | Some(user), Some(book) -> user.ReturnBook(book)
            | Some(user), None -> printfn "Nie znaleziono książki o tytule %s" title
            | None, _ -> printfn "Nie znaleziono użytkownika o nazwisku %s" name
            showMenu()
        | "9" -> printfn "Do widzenia!"
        | _ ->
            printfn "Nieprawidłowa opcja. Spróbuj ponownie."
            showMenu()

    showMenu()
    0
