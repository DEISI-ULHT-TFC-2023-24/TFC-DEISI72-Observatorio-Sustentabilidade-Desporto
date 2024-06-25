const autocolors = window['chartjs-plugin-autocolors'];
Chart.register(autocolors);

const lighten = (color, value) => Chart.helpers.color(color).lighten(value).rgbString();

const emptyDoug = {
  id: 'emptyDoughnut',
  afterDraw(chart, args, options) {
    const {datasets} = chart.data;
    const {color, width, radiusDecrease} = options;
    let hasData = false;

    for (let i = 0; i < datasets.length; i += 1) {
      const dataset = datasets[i];
      hasData |= dataset.data.length > 0;
    }

    if (!hasData) {
      const {chartArea: {left, top, right, bottom}, ctx} = chart;
      const centerX = (left + right) / 2;
      const centerY = (top + bottom) / 2;
      const r = Math.min(right - left, bottom - top) / 2;

      ctx.beginPath();
      ctx.lineWidth = width || 2;
      ctx.strokeStyle = color || 'rgba(255, 128, 0, 0.5)';
      ctx.arc(centerX, centerY, (r - radiusDecrease || 0), 0, 2 * Math.PI);
      ctx.stroke();
    }
  }
};

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

function makePieChart(context, labels, data, metric) {
    var dataIsEmpty = true;
    for(let a of data) {
        if(a != 0) {
            dataIsEmpty = false;
        }

    }

    if(dataIsEmpty) {
        data = [];
    }


    let chart = new Chart(context, {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [
                {
                    label: metric,
                    data: data
                }
            ]
        },
        options: {
            plugins: {
                autocolors: {
                    mode: 'data',
                    offset: 30,

                },
                emptyDoughnut: {
                    color: "rgba(0,255,244,0.5)",
                    width: 2,
                    radiusDecrease: 20
                }
            }
        },
        plugins: [emptyDoug]
    });
}

function makeBarChart(context, labels, data, metric) {
    let chart = new Chart(context, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: metric,
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