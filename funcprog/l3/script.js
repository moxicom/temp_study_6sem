// tsc script.ts
// node script.js
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
function filterMultiplesOf(array, divisor) {
    return array.filter(function (num) { return num % divisor === 0; });
}
console.log(filterMultiplesOf([2, 3, 5, 6, 10], 3));
function joinStrings(strings, separator) {
    return strings.join(separator);
}
console.log(joinStrings(["str1", "str2", "str3"], "..."));
function sortByProperty(array, property) {
    return __spreadArray([], array, true).sort(function (a, b) {
        if (a[property] < b[property])
            return -1;
        if (a[property] > b[property])
            return 1;
        return 0;
    });
}
var racers = [
    { name: "Schumacher", titles: 7 },
    { name: "Verstappen", titles: 4 },
    { name: "Hamilton", titles: 7 },
];
console.log(sortByProperty(racers, "name"));
function withLogging(fn) {
    return function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        console.log("Args:", args);
        var result = fn.apply(void 0, args);
        console.log("Result:", result);
        return result;
    };
}
var multiply = function (x, y) { return x * y; };
var loggedMultiply = withLogging(multiply);
console.log(loggedMultiply(133, 2));
