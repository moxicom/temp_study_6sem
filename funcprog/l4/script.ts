const add = (a: number, b: number): number => a + b;
const subtract = (a: number, b: number): number => a - b;
const multiply = (a: number, b: number): number => a * b;
const divide = (a: number, b: number): number => (b !== 0 ? a / b : NaN);
const power = (a: number, b: number): number => Math.pow(a, b);
const sqrt = (a: number): number => (a >= 0 ? Math.sqrt(a) : NaN);

const calculate = (operation: (a: number, b?: number) => number, a: number, b?: number): number => {
    return operation(a, b!);
};

document.addEventListener("DOMContentLoaded", () => {
    const resultDisplay = document.getElementById("result") as HTMLParagraphElement;
    const num1Input = document.getElementById("num1") as HTMLInputElement;
    const num2Input = document.getElementById("num2") as HTMLInputElement;
    const operationButtons = document.querySelectorAll(".operation");

    operationButtons.forEach(button => {
        button.addEventListener("click", () => {
            const num1 = parseFloat(num1Input.value);
            const num2 = parseFloat(num2Input.value);
            const operation = button.getAttribute("data-operation");

            let result: number;
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

            resultDisplay.textContent = `Result: ${result}`;
        });
    });
});
