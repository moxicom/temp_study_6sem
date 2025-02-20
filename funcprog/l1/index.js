// Функция получения четных чисел.
const getEvenNumbers = (arr) => arr.filter(num => num % 2 === 0);

// Функция получения квадратов чисел
const getSquares = (arr) => arr.map(num => num ** 2);

// Фильтрация объектов по свойству
const filterByProperty = (arr, prop) => arr.filter(obj => obj.hasOwnProperty(prop))

// Вычисление суммы элементов массива
const sumArray = (arr) => arr.reduce((sum, num) => sum + num, 0);

// Функция высшего порядка
const applyFunctionToArray = (fn, arr) => arr.map(fn);

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const objects = [{ val: 1 }, { value: 3 },
    { value: 5 },{ val: 23 }, { name: "name" },];
console.log("Массив состоящий из четных чисел:", getEvenNumbers(numbers));
console.log("Массив состоящий из квадратов чисел:", getSquares(numbers));
console.log(
    "Объекты с указанным свойством 'val':",
    filterByProperty(objects, "val"),
);
console.log("Сумма чисел:", sumArray(numbers));
console.log(
    "Применение функции удвоения:",
    applyFunctionToArray((num) => num * 2, numbers),
);

// Пример использования функции для суммы квадратов всех чётных чисел
const sumOfEvenSquares = (arr) => {
    const evenNumbers = getEvenNumbers(arr);
    const squares = getSquares(evenNumbers);
    return sumArray(squares);
};
console.log("Сумма квадратов чётных чисел:", sumOfEvenSquares(numbers));

// Пример использования функции для нахождения среднего арифметического всех чисел, больших
// заданного значения
const averageGreaterThanValue = (arr, prop, minValue) => {
    const filteredValues = arr
        .filter((obj) => obj[prop] > minValue)
        .map((obj) => obj[prop]);
    const sum = sumArray(filteredValues);
    return filteredValues.length > 0 ? sum / filteredValues.length : 0;
};
console.log(
    "Среднее арифметическое значений, больше 2:",
    averageGreaterThanValue(objects, "value", 2),
);