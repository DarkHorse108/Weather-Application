
        function farenheit_to_celsius(elementID)
       {

            var celsius = $(elementID).text();
            celsius = (celsius - 32) * (5/9);
            celsius = Math.round(celsius * 10) / 10;
            $(elementID).html(celsius);
       }

       function celsius_to_farenheit(elementID)
       {
            var farenheit = $(elementID).text();
            farenheit = (farenheit * (9/5)) + 32;
            farenheit = Math.round(farenheit * 10) / 10;
            $(elementID).html(farenheit);
       }

        $(document).ready(function(){

            $('input:radio').change(function(){

                var days = ['#current_temp', '#current_high', '#current_low', '#day1_high', '#day1_low', '#day2_high', '#day2_low', '#day3_high', '#day3_low', '#day4_high', '#day4_low', '#day5_high', '#day5_low', '#day6_high', '#day6_low', '#day7_high', '#day7_low'];

                if(this.value == 'celsius')
                {
                    
                    days.forEach(element => farenheit_to_celsius(element));
                }
                else if (this.value == 'farenheit')
                {
                    days.forEach(element => celsius_to_farenheit(element));
                }
            });
        });
            
