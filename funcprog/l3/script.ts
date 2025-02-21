// tsc script.ts
// node script.js

function filterMultiplesOf(array: number[], divisor: number): number[] {
    return array.filter((num) => num % divisor === 0);
}

console.log(filterMultiplesOf([2, 3, 5, 6, 10], 3));

function joinStrings(strings: string[], separator: string): string {
    return strings.join(separator);
}

console.log(joinStrings(["str1", "str2", "str3"], "..."));

function sortByProperty<T, K extends keyof T>(array: T[], property: K): T[] {
    return [...array].sort((a, b) => {
        if (a[property] < b[property]) return -1;
        if (a[property] > b[property]) return 1;
        return 0;
    });
}

type Racers = { name: string; titles: number };
const racers: Racers[] = [
    { name: "Schumacher", titles: 7 },
    { name: "Verstappen", titles: 4 },
    { name: "Hamilton", titles: 7 },
];
console.log(sortByProperty(racers, "titles"));

function withLogging<T extends (...args: any[]) => any>(fn: T): T {
    return function (...args: Parameters<T>): ReturnType<T> {
        console.log("Args:", args);
        const result = fn(...args);
        console.log("Result:", result);
        return result;
    } as T;
}

const multiply = (x: number, y: number): number => x * y;
const loggedMultiply = withLogging(multiply);
console.log(loggedMultiply(133, 2));