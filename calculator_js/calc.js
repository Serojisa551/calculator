let number_one = ''; // first number
let number_two = ''; // secont number
let operator = ''; // second number
let finish = false;
let is_negative = false

const digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'];
const action = ['-', '+', 'X', '/', '%'];

// screen
const out = document.querySelector('.calc-screen p');

function clearAll() {
    number_one = ''; // first number and result
    number_two = ''; // second number 
    operator = '';
    finish = false;
    is_negative = false;
    out.textContent = 0;
}

function positive_negative() {
    if (operator === '') {
        number_one = -number_one;
        out.textContent = number_one;
    } else {
        number_two = -number_two;
        out.textContent = number_two;
    }
    console.table(number_one, number_two, operator);
}

document.querySelector('.ac').onclick = clearAll;
document.querySelector('.plus-minus').onclick = positive_negative;


document.querySelector('.buttons').onclick = (event) => {
    // the button is not pressed
    if (!event.target.classList.contains('btn')) return;
    // the clear All ac button is pressed
    if (event.target.classList.contains('ac')) return;
    // the +/- button
    if (event.target.classList.contains('plus-minus')) return;

    out.textContent = '';
    // I get the button pressed
    const key = event.target.textContent;

    // if the 0-9 or key is pressed .
    if (digit.includes(key)) {
        if (number_two === '' && operator === '') {
            number_one += key;
            out.textContent = number_one;
        }
        else if (number_one !== '' && number_two !== '' && finish) {
            number_two = key;
            finish = false;
            out.textContent = number_two;
        }
        else {
            number_two += key;
            out.textContent = number_two;
        }
        console.table(number_one, number_two, operator);
        return;
    }

    // if the + key is pressed - / *
    if (action.includes(key)) {
        operator = key;
        out.textContent = number_one;
        console.table(number_one, number_two, operator);
        return;
    }

    // pressed =
    if (key === '=') {
        if (number_two === '') number_two = number_one;
        switch (operator) {
            case "%":
                number_one = number_one / 100
                break;
            case "+":
                number_one = (+number_one) + (+number_two);
                break;
            case "-":
                number_one = number_one - number_two;
                break;
            case "X":
                number_one = number_one * number_two;
                break;
            case "/":
                if (number_two === '0') {
                    out.textContent = 'Ошибка';
                    number_one = '';
                    number_two = '';
                    operator = '';
                    return;
                }
                number_one = number_one / number_two;
                break;
        }
        finish = true;
        out.textContent = number_one;
        console.table(number_one, number_two, operator);
    }

}