$(document).ready(function(){


//____________________________zoom function____________________________________
           $('#etalage').etalage({
            thumb_image_width:400,
            thumb_image_height:400,
            source_image_width:900,
            source_image_height:900,
            show_hint:true,
            show_icon:true,
            lazyLoad:'ondemand',
            //lazyLoad:'progressive',

            //show_descriptions: false,
            //small_thumbs: 0,
               
            //autoplay:false,
            //zoom_area_width: 340,               // Width of the zoomed image frame (including borders, padding) (value in pixels)
            //zoom_area_height:495,       // Height of the zoomed image frame (including borders, padding) (value in pixels / 'justify' = height of large thumb + small thumbs)
            //zoom_area_distance: 20,
          click_callback: function(image_anchor, instance_id){
            alert('Callback example:\nYou clicked on an image with the anchor: "'+image_anchor+'"\n(in Etalage instance: "'+instance_id+'")');
          }
        });

//_______________________________________________________________


$('.unsubscribe_btn').click(function(){
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var email = document.getElementById('Subscribe_email').value
    var this_form = document.getElementById('Subscribe-form');
    var url = "/unsubscribe/"

    if(email.match(mailformat)){
        $.ajax({
        type  : "GET",
        url   : url,
        data  :{'email':email , 'csrfmiddlewaretoken': '{{ csrf_token }}'},

        

        success : function(data){
            this_form.reset();
            if(data['data']=="true"){
              $('#subscr_info').html('<p style="color:green;">unsubscribing complete</p>');  
          }else{
            $('#subscr_info').html('<p style="color:red;">You did not subscribed</p>');
          }
            
        },
        error :function(error){
            $('#subscr_info').html('<p style="color:red;">Sorry!!,Something is wrong</p>');
        }
    })
    }else{
       $('#subscr_info').html('<p style="color:red;">Your email is not valid</p>'); 
    }
    
    
  });
//__________________________________________________________________
$('.Subscribe_btn').click(function(){
    
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var email = document.getElementById('Subscribe_email').value;
    var this_form = document.getElementById('Subscribe-form');
    var url = "/Subscribe"

    if(email.match(mailformat)){
        $.ajax({
        type  : "GET",
        url   : url,
        data  :{'email':email , 'csrfmiddlewaretoken': '{{ csrf_token }}'},

        

        success : function(data){
            this_form.reset();
            if(data['data']=="true"){
              $('#subscr_info').html('<p style="color:green;">Thank you for subscribing</p>');  
            }else{
              $('#subscr_info').html('<p style="color:red;">You have already subscribed</p>');  
            }
            
            
        },
        error :function(error){
            $('#subscr_info').html('<p style="color:red;">Sorry!!,Something is wrong</p>');
        }
    })
    }else{
      $('#subscr_info').html('<p style="color:red;">Your email is not valid</p>');  
    }
 });

})