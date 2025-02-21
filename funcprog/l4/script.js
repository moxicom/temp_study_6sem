var add = function (a, b) { return a + b; };
var subtract = function (a, b) { return a - b; };
var multiply = function (a, b) { return a * b; };
var divide = function (a, b) { return (b !== 0 ? a / b : NaN); };
var power = function (a, b) { return Math.pow(a, b); };
var sqrt = function (a) { return (a >= 0 ? Math.sqrt(a) : NaN); };
var calculate = function (operation, a, b) {
    return operation(a, b);
};
document.addEventListener("DOMContentLoaded", function () {
    var resultDisplay = document.getElementById("result");
    var num1Input = document.getElementById("num1");
    var num2Input = document.getElementById("num2");
    var operationButtons = document.querySelectorAll(".operation");
    operationButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var num1 = parseFloat(num1Input.value);
            var num2 = parseFloat(num2Input.value);
            var operation = button.getAttribute("data-operation");
            var result;
            switch (operation) {
                case "add":
                    result = calculate(add, num1, num2);
                    break;
                case "subtract":
                    result = calculate(subtract, num1, num2);
                    break;
                case "multiply":
                    result = calculate(multiply, num1, num2);
                    break;
                case "divide":
                    result = calculate(divide, num1, num2);
                    break;
                case "power":
                    result = calculate(power, num1, num2);
                    break;
                case "sqrt":
                    result = calculate(sqrt, num1);
                    break;
                default:
                    result = NaN;
            }
            resultDisplay.textContent = "Result: ".concat(result);
        });
    });
});
