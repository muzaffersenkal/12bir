/*
 * Title:   Travelo - Travel, Tour Booking HTML5 Template - Calendar Js used in the detailed pages
 * Author:  http://themeforest.net/user/soaptheme
 */

function Hours() {
    this.html = "";
}
(function ($, document, window) {
    Hours.prototype.generateHTML = function() {
        var hours = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"];
        var today = new Date();


        var html = "";




        html += "<table><thead><tr>";



        html += "</tr></thead><tbody><tr>";


         var column = 0;
        for ( i = 0; i <= hours.length-1; i++) {





                html += "<td class='available'><span>" + hours[i] + "</span></td>";


            column++;
            if (column == 7) {
                html += "</tr><tr>";
                column = 0;
            }
        }




        /*if (column > 0) {
            for ( i = 1; column < 7; i++) {
                html += "<td class='next-month'>" + i + "</td>";
                column++;
            }
        }*/
        html += "</tr></tbody></table>";
        this.html = html;
    };

    Hours.prototype.getHTML = function() {
        return this.html;
    };
}(jQuery, document, window));