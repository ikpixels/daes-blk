$(document).ready(function(){
	  $('#small_menu_btn').click(function(){
      $('#small_ik_menu').toggle();
     });

     $('#nav_close').click(function(){
       $('#small_ik_menu').hide();
     });

     $('#Search_btn').click(function(){
       $('#Searching_form').toggle();
     });

     $('#Search_btn3').click(function(){
       $('#Searching_form').toggle();
     });

     $('#search_close').click(function(){
       $('#Searching_form').hide();
     });


});

$(document).ready(function(){
      $('#dac_btn1').click(function(){
         $('#dac_btn1').css('display','none');
         $('#dac_btn2').css('display','block');
         $('#dac').toggle();
      });

      $('#dac_btn2').click(function(){
         $('#dac_btn1').css('display','block');
         $('#dac_btn2').css('display','none');
         $('#dac').toggle();
      });

      $('#daecc_btn1').click(function(){
         $('#daecc_btn1').css('display','none');
         $('#daecc_btn2').css('display','block');
         $('#daecc').toggle();
      });

      $('#daecc_btn2').click(function(){
         $('#daecc_btn1').css('display','block');
         $('#daecc_btn2').css('display','none');
         $('#daecc').toggle();
      });


       $('#dsp_btn1').click(function(){
         $('#dsp_btn1').css('display','none');
         $('#dsp_btn2').css('display','block');
         $('#dsp').toggle();
      });

      $('#dsp_btn2').click(function(){
         $('#dsp_btn1').css('display','block');
         $('#dsp_btn2').css('display','none');
         $('#dsp').toggle();
      });

      $('#asp_btn1').click(function(){
         $('#asp_btn1').css('display','none');
         $('#asp_btn2').css('display','block');
         $('#asp').toggle();
      });

      $('#asp_btn2').click(function(){
         $('#asp_btn1').css('display','block');
         $('#asp_btn2').css('display','none');
         $('#asp').toggle();
      });

      $('#vac_btn1').click(function(){
         $('#vac_btn1').css('display','none');
         $('#vac_btn2').css('display','block');
         $('#vac').toggle();
      });

      $('#vac_btn2').click(function(){
         $('#vac_btn1').css('display','block');
         $('#vac_btn2').css('display','none');
         $('#vac').toggle();
      });


});

$(document).ready(function(){
	$('#donate_form').on('submit', function(event){
    event.preventDefault();
    var this_form = $(this);
    var url = this_form.attr('action');
    var data = this_form.serialize();



     $.ajax({
        type  : "GET",
        url   : url,
        data  : data,
       
        success : function(response){
            this_form[0].reset();
            $('#paypal_btn_area').html(response['data']);  
        },
        error :function(error){
            alert("Something is wrong");
        }
    })
    
  });
});

//___________________contact form____________________________________
$(document).ready(function(){
    $('#ContactForm2').on('submit', function(event){
    event.preventDefault();
    var this_form = $(this);
    var url = this_form.attr('action');
    var data = this_form.serialize();



     $.ajax({
        type  : "GET",
        url   : url,
        data  : data,
       
        success : function(response){
            this_form[0].reset();
            $('#contact_info').html('<p style="color:green;"><strong>Thank you for sending message to us</strong></p>')  
        },
        error :function(error){
            this_form[0].reset();
            $('#contact_info').html('<p style="color:red;"><strong>Something is wrong</strong></p>')
        }
    })
    
  });
});
//___________________________________________________________________
$(document).ready(function(){
	$('#mpamba_btn').click(function(){
         
		$.ajax({
        type  : "GET",
        url   : '/donation/mpamba/',
        data  : {'payment':"mpamba" , 'csrfmiddlewaretoken': '{{ csrf_token }}'},
       
        success : function(response){
            $('#paypal_btn_area').html(response['data']); 
            
        },
        error :function(error){
            alert("Something is wrong");
        }
    })

	});
});

$(document).ready(function(){
	$('#airtel_btn').click(function(){ 
		$.ajax({
        type  : "GET",
        url   : '/donation/airtelmoney/',
        data  : {'payment':"mpamba" , 'csrfmiddlewaretoken': '{{ csrf_token }}'},
       
        success : function(response){
            $('#paypal_btn_area').html(response['data']); 
             
        },
        error :function(error){
            alert("Something is wrong");
        }
    })

	});
});

/*$(document).ready(function(){
   var num = $("#mywap").attr('accesskey');
   var name = $("#mywap").attr('title');
  $('#mywap').floatingWhatsApp({
    phone: num,
    popupMessage: 'Hello,I am ' + name +', how can I help you?',
    showPopup: true
    //showOnIE: false,
    //headerTitle: 'Welcome!',
    //headerColor: 'crimson',
    //backgroundColor: 'crimson',
    });
});*/
//____________________Land scape croper______________________
$(document).ready(function(){
   var num = $("#mywap2").attr('accesskey');
   var name = $("#mywap2").attr('title');
  $('#mywap2').floatingWhatsApp({
    phone: num,
    popupMessage: 'Hello,Lets talk about ' + name +', how can I help you?',
    showPopup: true
    //showOnIE: false,
    //headerTitle: 'Welcome!',
    //headerColor: 'crimson',
    //backgroundColor: 'crimson',
    });
});

$(function ()  {

       $("#id_image").change(function () {
        if (this.files && this.files[0]) {
          var reader = new FileReader();
          
          reader.onload = function (e) {
            
            $("#ik_image").attr("src", e.target.result);
            $('#form_area').css("display","none");
            $("#ik_modal").css("display","block");
            var image = document.querySelector('#ik_image');


            var cropper = new Cropper(image, {
            dragMode: 'move',
            aspectRatio: 16 / 9,
            autoCropArea: 0.65,
            restore: false,
            guides: false,
            center: false,
            highlight: false,
            cropBoxMovable: true,
            cropBoxResizable: true,
            toggleDragModeOnDblclick: false,

          ready: function () {
           cropper.setCropBoxData(cropBoxData).setCanvasData(canvasData)

          }

          });
          count = 0.1;
          $("#plus").click(function () {
          cropper.zoomTo(count);
          count +=0.1;
          });
          
          count1 = 1;
          $("#minus").click(function () {
             cropper.zoomTo(count1);
             count1 -=0.1;
          });


          $("#send").click(function(){
            var cropData = cropper.getData();
            $("#id_x").val(cropData["x"]);
            $("#id_y").val(cropData["y"]);
            $("#id_height").val(cropData["height"]);
            $("#id_width").val(cropData["width"]);
            $("#formUpload").submit();

          })

        }

          reader.readAsDataURL(this.files[0]);
      }



      });  

});
//__________________________square cropper___________________________

$(function (){

       $("#id_file").change(function () {
        if (this.files && this.files[0]) {
          var reader = new FileReader();
          
          reader.onload = function (e) {
            
            $("#ik_image").attr("src", e.target.result);
            $('#form_area').css("display","none");
            $("#ik_modal").css("display","block");
            var image = document.querySelector('#ik_image');


            var cropper = new Cropper(image, {
            dragMode: 'move',
            aspectRatio:  1/1,
            autoCropArea: 0.5,
            restore: true,
            guides: false,
            center: true,
            highlight: false,
            cropBoxMovable: true,
            cropBoxResizable: true,
            toggleDragModeOnDblclick: false,

          ready: function () {
           cropper.setCropBoxData(cropBoxData).setCanvasData(canvasData)

          }

          });
          count = 0.1;
          $("#plus").click(function () {
          cropper.zoomTo(count);
          count +=0.1;
          });
          
          count1 = 1;
          $("#minus").click(function () {
             cropper.zoomTo(count1);
             count1 -=0.1;
          });


          $("#send").click(function(){
            var cropData = cropper.getData();
            $("#id_x").val(cropData["x"]);
            $("#id_y").val(cropData["y"]);
            $("#id_height").val(cropData["height"]);
            $("#id_width").val(cropData["width"]);
            $("#formUpload").submit();

          })

        }

          reader.readAsDataURL(this.files[0]);
      }



      });  

});
//____________________________________________________________________  
$(document).ready(function(){
  $('#verify_give').click(function(){ 
    var id = $(this).attr('accesskey');
    $.ajax({
        type  : "GET",
        url   : '/donation/donation_view/',
        data  : {'id':id , 'csrfmiddlewaretoken': '{{ csrf_token }}'},
       
        success : function(response){
            $('#donation_view').html(response['data']);
             
        },
        error :function(error){
            alert("Something is wrong");
        }
    })

  });
});

//_____________________________________________________________
  window.onscroll = function(){
    stickynv();
  }

  var nav = document.getElementById('nav_bar');
  var sticky = nav.offsetTop;

  function stickynv(){
     if(window.pageYOffset >= sticky ){
       nav.classList.add('sticky');

     }else{
       nav.classList.remove('sticky');
  
     }
  }