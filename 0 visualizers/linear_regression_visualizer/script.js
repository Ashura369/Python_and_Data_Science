const canvas = document.getElementById('regressionCanvas');
const ctx = canvas.getContext('2d');
const slopeVal = document.getElementById('slope-val');
const interceptVal = document.getElementById('intercept-val');
const equationVal = document.getElementById('equation-val');
const mseVal = document.getElementById('mse-val');
const resetBtn = document.getElementById('reset-btn');

let width, height;
let points = [];
const scale = 40; // Pixels per unit

// Resize canvas to fill container
function resize() {
    const container = canvas.parentElement;
    width = container.clientWidth;
    height = container.clientHeight;
    canvas.width = width;
    canvas.height = height;
    draw();
}

window.addEventListener('resize', resize);
resize();

// Coordinate Transformations
function toScreenX(x) {
    return width / 2 + x * scale;
}

function toScreenY(y) {
    return height / 2 - y * scale;
}

function toLogicalX(screenX) {
    return (screenX - width / 2) / scale;
}

function toLogicalY(screenY) {
    return (height / 2 - screenY) / scale;
}

// Interaction
canvas.addEventListener('mousedown', (e) => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const logicalX = toLogicalX(x);
    const logicalY = toLogicalY(y);

    points.push({ x: logicalX, y: logicalY });
    update();
});

resetBtn.addEventListener('click', () => {
    points = [];
    update();
});

// Logic
function calculateRegression() {
    if (points.length < 2) return null;

    const n = points.length;
    let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;

    for (const p of points) {
        sumX += p.x;
        sumY += p.y;
        sumXY += p.x * p.y;
        sumXX += p.x * p.x;
    }

    const meanX = sumX / n;
    const meanY = sumY / n;

    // Least Squares Formula
    const numerator = sumXY - n * meanX * meanY;
    const denominator = sumXX - n * meanX * meanX;

    if (denominator === 0) return null; // Vertical line

    const m = numerator / denominator;
    const c = meanY - m * meanX;

    // Calculate MSE
    let sumSquaredError = 0;
    for (const p of points) {
        const predictedY = m * p.x + c;
        const error = p.y - predictedY;
        sumSquaredError += error * error;
    }
    const mse = sumSquaredError / n;

    return { m, c, mse };
}

function update() {
    const result = calculateRegression();

    if (result) {
        slopeVal.textContent = result.m.toFixed(2);
        interceptVal.textContent = result.c.toFixed(2);
        const sign = result.c >= 0 ? '+' : '-';
        equationVal.textContent = `y = ${result.m.toFixed(2)}x ${sign} ${Math.abs(result.c).toFixed(2)}`;
        mseVal.textContent = result.mse.toFixed(2);
    } else {
        slopeVal.textContent = '0.00';
        interceptVal.textContent = '0.00';
        equationVal.textContent = 'y = 0.00x + 0.00';
        mseVal.textContent = '0.00';
    }

    draw(result);
}

// Rendering
function drawGrid() {
    ctx.strokeStyle = '#334155'; // Using CSS var --grid-line color manually
    ctx.lineWidth = 1;
    ctx.beginPath();

    // Vertical lines
    const startX = Math.floor(toLogicalX(0));
    const endX = Math.ceil(toLogicalX(width));
    for (let i = startX; i <= endX; i++) {
        const x = toScreenX(i);
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
    }

    // Horizontal lines
    const startY = Math.floor(toLogicalY(height));
    const endY = Math.ceil(toLogicalY(0));
    for (let i = startY; i <= endY; i++) {
        const y = toScreenY(i);
        ctx.moveTo(0, y);
        ctx.lineTo(width, y);
    }
    ctx.stroke();

    // Axes
    ctx.strokeStyle = '#94a3b8'; // Axis color
    ctx.lineWidth = 2;
    ctx.beginPath();
    // X Axis
    ctx.moveTo(0, toScreenY(0));
    ctx.lineTo(width, toScreenY(0));
    // Y Axis
    ctx.moveTo(toScreenX(0), 0);
    ctx.lineTo(toScreenX(0), height);
    ctx.stroke();
}

function drawPoints() {
    ctx.fillStyle = '#38bdf8'; // Accent color
    for (const p of points) {
        const x = toScreenX(p.x);
        const y = toScreenY(p.y);
        ctx.beginPath();
        ctx.arc(x, y, 6, 0, Math.PI * 2);
        ctx.fill();

        // Inner white dot for "pop"
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(x, y, 2, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#38bdf8';
    }
}

function drawRegressionLine(model) {
    if (!model) return;

    const { m, c } = model;

    // Calculate two points at the edges of the visible area
    const minX = toLogicalX(0);
    const maxX = toLogicalX(width);

    const y1 = m * minX + c;
    const y2 = m * maxX + c;

    ctx.strokeStyle = '#ec4899'; // Secondary color
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(toScreenX(minX), toScreenY(y1));
    ctx.lineTo(toScreenX(maxX), toScreenY(y2));
    ctx.stroke();
}

function drawResiduals(model) {
    if (!model) return;
    const { m, c } = model;

    ctx.strokeStyle = 'rgba(236, 72, 153, 0.4)'; // Faint secondary color
    ctx.lineWidth = 1;
    ctx.setLineDash([5, 5]);

    for (const p of points) {
        const predictedY = m * p.x + c;
        const x = toScreenX(p.x);
        const yActual = toScreenY(p.y);
        const yPred = toScreenY(predictedY);

        ctx.beginPath();
        ctx.moveTo(x, yActual);
        ctx.lineTo(x, yPred);
        ctx.stroke();
    }
    ctx.setLineDash([]);
}

function draw(model = calculateRegression()) {
    ctx.clearRect(0, 0, width, height);
    drawGrid();
    drawResiduals(model); // Draw residuals under points
    drawRegressionLine(model);
    drawPoints();
}

// Initial draw
draw();
