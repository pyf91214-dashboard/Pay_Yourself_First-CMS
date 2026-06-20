
        document.addEventListener("DOMContentLoaded", function() {
            var ctx = document.getElementById('revenueChart').getContext('2d');
            
            // Create a gradient for the chart
            var gradient = ctx.createLinearGradient(0, 0, 0, 300);
            gradient.addColorStop(0, 'rgba(56, 148, 0, 0.4)'); // brand-700 with opacity
            gradient.addColorStop(1, 'rgba(56, 148, 0, 0.0)'); 

            var revenueChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'],
                    datasets: [{
                        label: 'Revenue ($)',
                        data: [12000, 19000, 15000, 22000, 20000, 24850],
                        borderColor: '#389400', // brand-700
                        backgroundColor: gradient,
                        borderWidth: 3,
                        pointBackgroundColor: '#ffffff',
                        pointBorderColor: '#389400',
                        pointBorderWidth: 2,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                        fill: true,
                        tension: 0.4 // Smooth curves
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false // Hide legend for cleaner look
                        },
                        tooltip: {
                            backgroundColor: '#1c1c1c',
                            titleFont: { family: 'Inter', size: 13, weight: 'bold' },
                            bodyFont: { family: 'Inter', size: 14 },
                            padding: 12,
                            displayColors: false,
                            callbacks: {
                                label: function(context) {
                                    return '$' + context.parsed.y.toLocaleString();
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: {
                                color: '#f3f4f6', // gray-100
                                drawBorder: false,
                            },
                            ticks: {
                                font: { family: 'Inter', size: 12 },
                                color: '#9ca3af', // gray-400
                                callback: function(value) {
                                    return '$' + (value / 1000) + 'k';
                                }
                            }
                        },
                        x: {
                            grid: {
                                display: false, // Hide vertical lines
                                drawBorder: false,
                            },
                            ticks: {
                                font: { family: 'Inter', size: 12 },
                                color: '#9ca3af' // gray-400
                            }
                        }
                    }
                }
            });
        });
    
