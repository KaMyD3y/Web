function drawAngle() {
    let canvas = document.getElementById('myCanvas');
    let ctx = canvas.getContext('2d');
    let angle = document.getElementById('angle').value;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    let startX = 200;
    let startY = 200;

    let length = 100;
    
    let radians = angle * Math.PI / 180;

    let endX = startX + length * Math.cos(radians);
    let endY = startY - length * Math.sin(radians);

    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(startX + length, startY);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(endX, endY);
    ctx.stroke();
}

function showCaracter() {
    let somethings = document.getElementById('caracter').value;
    let type;

    // Check boolean
    if (somethings.toLowerCase() === 'true' || somethings.toLowerCase() === 'false') {
        type = 'boolean';
    }
    // check Number
    else if (!isNaN(somethings) && somethings.trim() !== '') {
        type = 'number';
    }
    // Check null
    else if (somethings.toLowerCase() === 'null') {
        type = 'null';
    }
    // Check undefined
    else if (somethings.toLowerCase() === 'undefined') {
        type = 'undefined';
    }
    // check symbol ...
    else if (somethings.startsWith('Symbol(') && somethings.endsWith(')')) {
        type = 'symbol';
    }
    // check BigInt
    else if (/^-?\d+n$/.test(somethings)) {
        type = 'bigint';
    }
    // Restul e string
    else {
        type = 'string';
    }
    document.getElementById('result').innerText = `Tipul de date este ${type}`
}
const codulTara = (cod) => {
    let info;
    switch(cod.toLowerCase()) {
        case 'md':
            info = 'Republica Moldova, Prefix telefon: +373';
            break;
        case 'ro':
            info = 'Romania, Prefix telefon: +40';
            break;
        case 'us':
            info = 'United States, Prefix telefon: +1';
            break;
        case 'fr':
            info = 'France, Prefix telefon: +33';
            break;
        // Добавьте другие коды стран по мере необходимости
        default:
            info = 'Cod de tara necunoscut';
    }
    return info;
};

const showCountryInfo = () => {
    const cod = document.getElementById('countryCode').value;
    const result = codulTara(cod);
    document.getElementById('tara').innerText = result;
};