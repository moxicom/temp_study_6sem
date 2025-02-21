open System

// Функции для операций
let add x y = x + y
let subtract x y = x - y
let multiply x y = x * y
let divide x y =
    if y = 0.0 then
        failwith "Деление на ноль невозможно"
    else
        x / y

let power x y = Math.Pow(x, y)
let sqrt x = Math.Sqrt(x)
let sine x = Math.Sin(x)
let cosine x = Math.Cos(x)
let tangent x = Math.Tan(x)

// Функции для обработки пользовательского ввода
let parseFloat (input: string) =
    match System.Double.TryParse(input) with
    | (true, value) -> Some value
    | _ -> None

// Функция высшего порядка для обработки операций
let performOperation op x y =
    op x y

// Вывод меню
let displayMenu () =
    printfn "Выберите операцию:"
    printfn "1. Сложение"
    printfn "2. Вычитание"
    printfn "3. Умножение"
    printfn "4. Деление"
    printfn "5. Возведение в степень"
    printfn "6. Квадратный корень"
    printfn "7. Синус"
    printfn "8. Косинус"
    printfn "9. Тангенс"
    printfn "0. Выход"

// Основная функция калькулятора
let rec calculator () =
    displayMenu()
    let operation = Console.ReadLine()

    match operation with
    | "0" -> printfn "Выход из программы."; ()
    | "1" ->
        printfn "Введите первое число:"
        let input1 = Console.ReadLine()
        match parseFloat input1 with
        | Some x ->
            printfn "Введите второе число:"
            let input2 = Console.ReadLine()
            match parseFloat input2 with
            | Some y ->
                let result = performOperation add x y
                printfn "Результат: %f" result
            | None -> printfn "Некорректный ввод второго числа."
        | None -> printfn "Некорректный ввод первого числа."
    | "2" ->
        printfn "Введите первое число:"
        let input1 = Console.ReadLine()
        match parseFloat input1 with
        | Some x ->
            printfn "Введите второе число:"
            let input2 = Console.ReadLine()
            match parseFloat input2 with
            | Some y ->
                let result = performOperation subtract x y
                printfn "Результат: %f" result
            | None -> printfn "Некорректный ввод второго числа."
        | None -> printfn "Некорректный ввод первого числа."
    | "3" ->
        printfn "Введите первое число:"
        let input1 = Console.ReadLine()
        match parseFloat input1 with
        | Some x ->
            printfn "Введите второе число:"
            let input2 = Console.ReadLine()
            match parseFloat input2 with
            | Some y ->
                let result = performOperation multiply x y
                printfn "Результат: %f" result
            | None -> printfn "Некорректный ввод второго числа."
        | None -> printfn "Некорректный ввод первого числа."
    | "4" ->
        printfn "Введите первое число:"
        let input1 = Console.ReadLine()
        match parseFloat input1 with
        | Some x ->
            printfn "Введите второе число:"
            let input2 = Console.ReadLine()
            match parseFloat input2 with
            | Some y ->
                try
                    let result = performOperation divide x y
                    printfn "Результат: %f" result
                with
                | :? System.Exception -> printfn "Ошибка: Деление на ноль!"
            | None -> printfn "Некорректный ввод второго числа."
        | None -> printfn "Некорректный ввод первого числа."
    | "5" ->
        printfn "Введите число:"
        let input = Console.ReadLine()
        match parseFloat input with
        | Some x ->
            printfn "Введите степень:"
            let exponentInput = Console.ReadLine()
            match parseFloat exponentInput with
            | Some y ->
                let result = power x y
                printfn "Результат: %f" result
            | None -> printfn "Некорректный ввод степени."
        | None -> printfn "Некорректный ввод числа."
    | "6" ->
        printfn "Введите число:"
        let input = Console.ReadLine()
        match parseFloat input with
        | Some x ->
            let result = sqrt x
            printfn "Результат: %f" result
        | None -> printfn "Некорректный ввод числа."
    | "7" ->
        printfn "Введите угол (в радианах):"
        let input = Console.ReadLine()
        match parseFloat input with
        | Some x ->
            let result = sine x
            printfn "Синус: %f" result
        | None -> printfn "Некорректный ввод угла."
    | "8" ->
        printfn "Введите угол (в радианах):"
        let input = Console.ReadLine()
        match parseFloat input with
        | Some x ->
            let result = cosine x
            printfn "Косинус: %f" result
        | None -> printfn "Некорректный ввод угла."
    | "9" ->
        printfn "Введите угол (в радианах):"
        let input = Console.ReadLine()
        match parseFloat input with
        | Some x ->
            let result = tangent x
            printfn "Тангенс: %f" result
        | None -> printfn "Некорректный ввод угла."
    | _ -> printfn "Некорректный выбор операции."

    // Рекурсивно вызываем калькулятор для нового ввода
    calculator()

// Запуск калькулятора
calculator()
