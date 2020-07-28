
        function record_starting_temp(days)
        {
            original_temperature = [];

            for (i = 0; i < days.length; i++)
            {
                original_temperature.push($(days[i]).text());
            }

            return original_temperature;

        }

        function farenheit_to_celsius(elementID)
       {

            var celsius = $(elementID).text();
            celsius = (celsius - 32) * (5/9);
            celsius = Math.round(celsius); 
            $(elementID).html(celsius);
       }

       function celsius_to_farenheit(element_array, farenheit_array)
       {
            var i = 0;
            var length = element_array.length;

            for (i = 0; i < element_array.length; i++)
            {
                $(element_array[i]).html(farenheit_array[i]);
            }       
       }

        $(document).ready(function(){

            var days = ['#current_temp', '#current_high', '#current_low', '#day1_high', '#day1_low', '#day2_high', '#day2_low', '#day3_high', '#day3_low', '#day4_high', '#day4_low', '#day5_high', '#day5_low', '#day6_high', '#day6_low', '#day7_high', '#day7_low'];
            var farenheit = record_starting_temp(days);

            $('input:radio').change(function(){

                if(this.value == 'celsius')
                {
                    
                    days.forEach(element => farenheit_to_celsius(element));
                }
                else if (this.value == 'farenheit')
                {
                    celsius_to_farenheit(days, farenheit);
                }
            });
        });
            
