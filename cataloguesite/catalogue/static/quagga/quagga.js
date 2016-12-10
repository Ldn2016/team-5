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
            myRedirect('/catalogue/bookpost/', ['isbn', 'store'], [code, document.getElementById("store").value]);

        }

    }

    var myRedirect = function(redirectUrl, arg_array, val_array) {
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
