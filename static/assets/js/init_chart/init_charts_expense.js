function chart_expense(slug) {
    console.log(slug);
    var url = `/transactions/${slug}/get_chart_expense`;
    console.log(url);
    $.ajax({
          url: url,
          success: function (data) {
    console.log(data);
    var result =  data['data']
    let income = result.map(({amount})=>
            { if (amount>0){
                return amount
            }else {
                return 0 }
            }
        );
    var spent = result.map(({amount})=>
            { if (amount<0)
             return amount*-1
            })

    var date = result.map(({date})=>{
        return moment(Date.parse(date)).format('DD.MM.YYYY');
    })

    var element = document.getElementById("kt_charts_widget_1_chart_expense");

        if (!element) {
            return;
        }

        var options = {
            series: [{
                name: 'Gelir',
                data: income
            }, {
                name: 'Gider',
                data: spent
            }],
            chart: {
                type: 'bar',
                height: 350,
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: ['100%'],
                    endingShape: 'rounded'
                },
            },
            legend: {
                show: false
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            xaxis: {
                categories: date,
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false
                },
                labels: {
                    style: {
                        colors: KTApp.getSettings()['colors']['gray']['gray-500'],
                        fontSize: '12px',
                        fontFamily: KTApp.getSettings()['font-family']
                    }
                }
            },
            yaxis: {
                labels: {
                    style: {
                        colors: KTApp.getSettings()['colors']['gray']['gray-500'],
                        fontSize: '12px',
                        fontFamily: KTApp.getSettings()['font-family']
                    }
                }
            },
            fill: {
                opacity: 1
            },
            states: {
                normal: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                hover: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                active: {
                    allowMultipleDataPointsSelection: false,
                    filter: {
                        type: 'none',
                        value: 0
                    }
                }
            },
            tooltip: {
                style: {
                    fontSize: '12px',
                    fontFamily: KTApp.getSettings()['font-family']
                },
                y: {
                    formatter: function (val) {
                        return   val + "₺"
                    }
                }
            },
            colors: [KTApp.getSettings()['colors']['theme']['base']['success'], KTApp.getSettings()['colors']['theme']['base']['danger']],
            grid: {
                borderColor: KTApp.getSettings()['colors']['gray']['gray-200'],
                strokeDashArray: 4,
                yaxis: {
                    lines: {
                        show: true
                    }
                }
            }
        };

        var chart = new ApexCharts(element, options);
        chart.render();

    }

});



 };

 $(document).ready(function() {
    chart_expense(
        $('#kt_charts_widget_1_chart_expense').data("slug")
    );
});