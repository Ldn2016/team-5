//Initialise the Quagga barcode scanner and defines the startup function.
Quagga.init(
    {
        /*Specifies a live camera and not a still image are being used 
         * to detect barcodes.
         * This is used, so that a tablet or mobile computer can be used as a scanner without downloading any extra applications.
         */
        inputStream : 
        {
            name : "Live",
            type : "LiveStream"
        },
            decoder : 
        {
            /*Quagga is configured to read both the EAN and UPC barcode specificaitons.
            *These are the specificaitons most likely to be used for retail goods
            *in the UK.
            * */
            readers : ["ean_reader", "upc_reader"] 
        }
    }, function(err) 
    {
    //Handles initialisation.
        if (err)
        {
            console.log(err);
            return
        }
        console.log("Initialization finished. Ready to start");

        Quagga.start();
    
        /*The video display is styled, such that it takes up nearly the width of
        * the screen - the image can be easily seen, but is not overpowering.
        * The canvas box is shrunk to minimum size to prevent large gaps from
        * being visible in the webpage. */
        document.getElementsByTagName("video")[0].style.width = "90vw";
        document.getElementsByTagName("canvas")[0].style.width="0%";

  }
);

/* This script provides multiple ways to submit data:
 * 1. A barcode which represents a valid ISBN is scanned.
 *      The data is automatically processed, so the user can input an item
 *      with a simple scan.
 * 2. A user presses the 'submit' key. This allows the user to input the
 *      ISBN manually if scanning fails.
 * 3. A user presses 'enter'. This is a quick way of submitting data if the
 *      user wishes to keep hands on the keyboard
 * */

//This executes code when Quagga detects and decodes a bar code (case 1).
Quagga.onDetected(
    function(result)
    {
        var isbn = result.codeResult.code;        
        submitData(isbn);
    }
);

//When the "Submit" button is pressed, the form is submitted (case 2).
document.getElementById("submit").onclick = function()
    {
        var code = document.getElementById("isbn").value;
        submitData(code);
    };

//When 'Enter' is pressed, the form is submitted (case 3).
document.onkeydown = function()
    {
        if(window.event.keyCode=='13')
        {
            var code = document.getElementById("isbn").value
            submitData(code);
        }
    };



/*Runs the code which is used by all 3 cases to submit data to the server.
* This code checks if the value entered is valid, then submits it to the server
* and loads the next page to the user
* */
var submitData = function(code)
    {
        if (isValidIsbn(code) == true)
        {
            document.getElementById("isbn").value=code;
            localStorage.setItem('barcode', code);
            Quagga.stop();
            redirect('/catalogue/bookpost/', ['isbn', 'store'], [code, document.getElementById("store").value]);

        }

    }

/*This uses Javascript to create and submit a hidden form.
 * This allows POST data to be submitted, and the webpage to be redirected,
 * while allowing multiple ways for the user to submit the required data.
 * 
 * A list of arguments and values are used to enable the webpage loaded
 * by this script to be extended in the future.
 * */
var redirect = function(redirectUrl, arg_array, val_array)
    {
        form_string = '<form action="' + redirectUrl + '" method="post">';
            
        for (i = 0; i < arg_array.length; i++)
            {
                form_string = form_string + '<input type="hidden" name="'+ arg_array[i] +'" value="' + val_array[i] + '"></input>';
            }
             
        form_string = form_string + '</form>';
                 
        var form = $(form_string);
        $('body').append(form);
        $(form).submit();
    };

    /*this uses code on stack overflow.
    *It implements the algorithms used to check ISBNs to return a 
    * boolean result depending on the validity of the ISBN. It suppports 10-digit and 13-digit ISBN.
    * 
    * In addition, it checks, that 13-digit ISBNs start with 978 or 979.
    * In theory, 13-digit ISBNs are valid with other starting figures.
    * However, most English language books have these as initial digits.
    * 
    * Additionally, restricting the pool of valid ISBNs reduces the number of 
    * false positives.
    * */
    var isValidIsbn = function(str) {

    var sum,
        weight,
        digit,
        check,
        i;

    if (str.length != 10 && str.length != 13) {
        return false;
    }

    if (str.length == 13) {
        sum = 0;
        for (i = 0; i < 12; i++) {
            digit = parseInt(str[i]);
            if (i % 2 == 1) {
                sum += 3*digit;
            } else {
                sum += digit;
            }
        }
        check = (10 - (sum % 10)) % 10;
        return (check == str[str.length-1]) && (str.slice(0,3) == "979" || str.slice(0,3) == "978"); //check of first three characters of code
    }

    if (str.length == 10) {
        weight = 10;
        sum = 0;
        for (i = 0; i < 9; i++) {
            digit = parseInt(str[i]);
            sum += weight*digit;
            weight--;
        }
        check = 11 - (sum % 11);
        if (check == 10) {
            check = 'X';
        }
        return (check == str[str.length-1].toUpperCase());
    }
}
