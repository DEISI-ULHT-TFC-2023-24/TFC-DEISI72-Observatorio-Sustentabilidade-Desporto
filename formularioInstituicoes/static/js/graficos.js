const autocolors = window['chartjs-plugin-autocolors'];
Chart.register(autocolors);

const lighten = (color, value) => Chart.helpers.color(color).lighten(value).rgbString();

function makeLineChart(context, labels, data) {
    let chart = new Chart(context, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Consumo total (L)",
                    pointRadius: 0,
                    pointHitRadius: 50,
                    data: data,
                    tension: .3,
                    responsive: true,
                    maintainAspectRatio: false
                }
            ]
        },
        options: {
            title: {
                text: "Consumo total mensal",
                display: true
            },
            scales: {
                y: {
                    suggestedMin: 50,
                    suggestedMax: 40000,
                    display: false,
                }
            },
            plugins: {
                legend: {
                    display: false
                },
            }
        }

    });
}

function makePieChart(context, labels, data) {
    let chart = new Chart(context, {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "kWh",
                    data: data
                }
            ]
        },
        options: {
            plugins: {
                autocolors: {
                    mode: 'data',
                    offset: 30,

                }
            }
        }
    });
}

function makeBarChart(context, labels, data) {
    let chart = new Chart(context, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "€",
                    data: data
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                },
            }, plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}