// dotnet new console -lang "F#" -o MyFSharpApp

printfn "Hello from F#"

// Функции
let add x y = x + y
let subtract x y = x - y
let multiply x y = x * y
let divide x y =
    if y = 0 then
        failwith "Деление на ноль невозможно"
    else
        x / y

let rec factorial n =
    if n = 0 then
        1
    else
        n * factorial (n - 1)

let addCurried x = fun y -> x + y
let subtractCurried x = fun y -> x - y
let multiplyCurried x = fun y -> x * y
let divideCurried x = fun y ->
    if y = 0 then
        failwith "Деление на ноль невозможно"
    else
        x / y

let sum = add 5 3  // 8
printfn "sum: %d" sum

let diff = subtract 5 3  // 2
printfn "diff: %d" diff

let product = multiply 5 3  // 15
printfn "product: %d" product

let quotient = divide 5 3  // 1
printfn "quotient: %d" quotient

let factorialOf5 = factorial 5  // 120
printfn "factorialOf5: %d" factorialOf5

let add5 = addCurried 5
let result = add5 3  // 8
printfn "add5 3: %d" result
