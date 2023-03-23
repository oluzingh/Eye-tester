const chart = document.querySelector('#eye-chart');
const letters = ['E', 'F', 'P', 'T', 'O', 'Z', 'L', 'D', 'C', 'B', 'K', 'A', 'N', 'H', 'Y', 'X', 'M', 'W', 'V', 'U', 'Q', 'R', 'S', 'G', 'I', 'J'];
let index = 0;

function generateChart() {
    chart.querySelectorAll('div').forEach((div, i) => {
        div.textContent = letters[(i + index