
        function record_starting_values(days)
        {
            original = [];

            for (i = 0; i < days.length; i++)
            {
                original.push($(days[i]).text());
            }

            return original;
        }

        function revert_to_imperial_units(element_array, farenheit_array)
       {
            var i = 0;
            var length = element_array.length;

            for (i = 0; i < element_array.length; i++)
            {
                $(element_array[i]).html(farenheit_array[i]);
            }       
       }


        function farenheit_to_celsius(elementID)
       {

            var celsius = $(elementID).text();
            celsius = (celsius - 32) * (5/9);
            celsius = Math.round(celsius); 
            $(elementID).html(celsius);
       }

       function mph_to_meters_per_sec(elementID)
       {
            var one_mph_equals_ms = 0.44704;

            var ms = $(elementID).text();
            ms = Math.round((ms * one_mph_equals_ms) * 10) / 10;
            $(elementID).html(ms);
       }

       function change_mph_text_to_ms(elementID)
       {
            var ms_units_text = "m/s";

            $(elementID).html(ms_units_text);

        }

        $(document).ready(function(){
            
            var days = ['#current_temp', '#current_high', '#current_low', '#day1_high', '#day1_low', '#day2_high', '#day2_low', '#day3_high', '#day3_low', '#day4_high', '#day4_low', '#day5_high', '#day5_low', '#day6_high', '#day6_low', '#day7_high', '#day7_low'];
            var wind_values = ['#current_wind', '#day1_wind', '#day2_wind', '#day3_wind', '#day4_wind', '#day5_wind', '#day6_wind', '#day7_wind'];
            var wind_units = ['#current_wind_units', '#day1_wind_units', '#day2_wind_units', '#day3_wind_units', '#day4_wind_units', '#day5_wind_units', '#day6_wind_units', '#day7_wind_units'];

            var farenheit = record_starting_values(days);
            var mph = record_starting_values(wind_values);
            var mph_text = record_starting_values(wind_units);

            $('input:radio').change(function(){

                if(this.value == 'celsius')
                {
                    days.forEach(element => farenheit_to_celsius(element));
                    wind_values.forEach(element => mph_to_meters_per_sec(element));
                    wind_units.forEach(element => change_mph_text_to_ms(element));
                }
                else if (this.value == 'farenheit')
                {
                    revert_to_imperial_units(days, farenheit);
                    revert_to_imperial_units(wind_values, mph);
                    revert_to_imperial_units(wind_units, mph_text);
                }
            });
        });
            
