function makeLineChart(context, labels, data, lineColor, fillColor) {
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
                    borderColor: lineColor,
                    tension: .3,
                    fill: {
                        target: 'origin',
                        above: fillColor,   // Area will be red above the origin
                        below: fillColor    // And blue below the origin
                    },
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
                }
            }
        }
    });
}

function makePieChart(context, labels, data, colors) {
    let chart = new Chart(context, {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "kWh",
                    backgroundColor: colors,
                    data: data
                }
            ]
        },
    });
}

function makeBarChart(context, labels, data, colors) {
    let chart = new Chart(context, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "€",
                    backgroundColor: colors,
                    data: data
                }
            ]
        },
        options: {
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