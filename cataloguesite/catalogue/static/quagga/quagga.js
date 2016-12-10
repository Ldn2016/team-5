

/*Init code is adapted from code at https://github.com/serratus/quaggaJS
 * 
 * This code is licensed with the MIT License.
 * 
 * 
The MIT License (MIT)

Copyright (c) 2014 Christoph Oberhofer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

Quagga.init({
    inputStream : {
      name : "Live",
      type : "LiveStream"
    },
    decoder : {
      readers : ["ean_reader", "upc_reader"]
    }
  }, function(err) {
      if (err) {
          console.log(err);
          return
      }
      console.log("Initialization finished. Ready to start");

      Quagga.start();
      document.getElementsByTagName("video")[0].style.width = "90vw";
      document.getElementsByTagName("canvas")[0].style.width="0%";

  });

    
    
    var myRedirect = function(redirectUrl, arg, value) {
  var form = $('<form action="' + redirectUrl + '" method="post">' +
  '<input type="hidden" name="'+ arg +'" value="' + value + '"></input>' + '</form>');
  $('body').append(form);
  $(form).submit();
    };

    Quagga.onDetected(function(result) {
        //only registers if isbn valid
        var isbn = result.codeResult.code;
        
        submitData(isbn);
    });
    
    document.onkeydown = function()
    {
        if(window.event.keyCode=='13')
        {
            var code = document.getElementById("isbn").value
            submitData(code);
        }
    };
    
    document.getElementById("submit").onclick = function()
    {
        var code = document.getElementById("isbn").value;
        submitData(code);
    };


    var submitData = function(code)
    {
        if (isValidIsbn(code) == true)
        {
            document.getElementById("isbn").value=code;
            localStorage.setItem('barcode', code);
            Quagga.stop();
            myRedirect('/catalogue/bookpost/', 'isbn', code);

        }

    }

    var myRedirect = function(redirectUrl, arg, value) {
  var form = $('<form action="' + redirectUrl + '" method="post">' +
  '<input type="hidden" name="'+ arg +'" value="' + value + '"></input>' + '</form>');
  $('body').append(form);
  $(form).submit();
};

    Quagga.onDetected(function(result) {
        //only registers if isbn valid
        var code = result.codeResult.code;

        submitData(code);
    });

    //this is inspired by code on stack overflow
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
        return (check == str[str.length-1]) && (str.slice(0,3) == "979" || str.slice(0,3) == "978");
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
