

        function record_starting_values(days)
        {
            var original = [];

            var i = 0;
            for (i = 0; i < days.length; i++)
            {
                original.push($(days[i]).text());
            }

            return original;
        }

        function farenheit_array_to_celsius_array(farenheit_array)
        {
            var celsius_array = [];

            var i = 0;
            for (i = 0; i < farenheit_array.length; i++)
            {
                celsius_array.push(farenheit_to_celsius(farenheit_array[i]));
            }

            return celsius_array;
        }

        function farenheit_to_celsius(farenheit)
       {

            var celsius = (farenheit - 32) * (5/9);
            celsius = Math.round(celsius); 
            
            return celsius;
       }

        function mph_array_to_kmh_array(mph_array)
        {
            var kmh_array = [];

            var i = 0;
            for (i = 0; i < mph_array.length; i++)
            {
                kmh_array.push(mph_to_kmh(mph_array[i]));
            }

            return kmh_array;
        }

        function mph_to_kmh(mph)
       {
            var kmh = Math.round((mph * 1.60934) * 10) / 10;
            
            return kmh;
       }


       function update_html_with_array_values(element_array, data_array)
       {
            var i = 0;

            for(i = 0; i < element_array.length; i++)
            {
                $(element_array[i]).html(data_array[i]);
            }
       }

       function change_mph_text_to_kmh(elementID)
       {
             var km_units_text = "km/h";

             $(elementID).html(km_units_text);

        }

        function change_kmh_text_to_mph(elementID)
       {
             var mph_units_text = "mph";

             $(elementID).html(mph_units_text);

        }

        $(document).ready(function(){
            
            var days = ['#current_temp', '#current_high', '#current_low', '#day1_high', '#day1_low', '#day2_high', '#day2_low', '#day3_high', '#day3_low', '#day4_high', '#day4_low', '#day5_high', '#day5_low', '#day6_high', '#day6_low', '#day7_high', '#day7_low'];
            var wind_values = ['#current_wind', '#day1_wind', '#day2_wind', '#day3_wind', '#day4_wind', '#day5_wind', '#day6_wind', '#day7_wind'];
            var wind_units = ['#current_wind_units', '#day1_wind_units', '#day2_wind_units', '#day3_wind_units', '#day4_wind_units', '#day5_wind_units', '#day6_wind_units', '#day7_wind_units'];

            var farenheit_array = record_starting_values(days);
            var celsius_array = farenheit_array.slice();
            celsius_array = farenheit_array_to_celsius_array(celsius_array);

            var mph_array = record_starting_values(wind_values);
            var kmh_array = mph_array.slice();
            kmh_array = mph_array_to_kmh_array(kmh_array);




            $('input:radio').change(function(){

                if(this.value == 'celsius')
                {
                    update_html_with_array_values(days, celsius_array);
                    update_html_with_array_values(wind_values, kmh_array);
                    wind_units.forEach(element => change_mph_text_to_kmh(element));
                    $('#pills-fahr').removeClass('active');
                    $('#pills-cel').addClass('active');
                    
                }
                else if (this.value == 'farenheit')
                {
                    update_html_with_array_values(days, farenheit_array);
                    update_html_with_array_values(wind_values, mph_array);
                    wind_units.forEach(element => change_kmh_text_to_mph(element));
                    $('#pills-cel').removeClass('active');
                    $('#pills-fahr').addClass('active');
                    
                }
            });
        });
            
