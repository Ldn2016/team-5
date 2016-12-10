

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
      document.getElementById("code").value=1;
      document.getElementsByTagName("video")[0].style.width = "90vw";
      document.getElementsByTagName("canvas")[0].style.width="0%";
      
  });

    Quagga.onDetected(function(result) {
        var code = result.codeResult.code;
        document.getElementById("code").value=code;
        localStorage.setItem('barcode', code);
        Quagga.stop();
        $.post("/bookpost", localStorage.getItem("barcode"), function(data) {document.open(); 
                                   document.write(data);
                                   document.close();} );

        
    });


    
