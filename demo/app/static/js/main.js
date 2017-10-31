var host='http://127.0.0.1:5000/';


function DataIsReady(response){
  var prof = $('.product-info').clone();
  $("#products-div").empty();
  len=response['product_name'].length;
  for(var i=0; i<len;i++){
     var prof_card = prof.clone();
     prof_card.find('.product_name').text(response['product_name'][i]);
     prof_card.find('.price').text(response['price'][i]);
     prof_card.find('.source').text(response['source'][i]);
     prof_card.find('.product_image').attr('src',response['image_url'][i]);
     prof_card.find('.product_url').attr('href',response['product_url'][i]);
     $("#products-div").append(prof_card);

  }
        
}


$(document).ready(function(){
  $('#DivId2').hide()
	$('#search-button').click(function(){
   
    var val = $('#search-keyword').val();
    console.log(val);
    if(val && val.length>0){
      // var point=samplevisitors[val-1].slice(4,samplevisitors[val-1].length);

      $.post({
      url: host+'search_results',
      type: 'POST',
      data: JSON.stringify({ 'product': val}) ,
      contentType: 'application/json; charset=UTF-8',
      success: function (response) {
        console.log(response);
        DataIsReady(response);
        $('#DivId1').hide()
        $('#DivId2').show()
          
      },
      error: function () {
          console.log('Error in search')
          // alert("error");
      }
      });  
    }
    else{
      console.log('Search Keyword Empty');
    }
	});

  $('#home').click(function(){
    $('#DivId2').hide();
    $('#search-keyword').val('');
    $('#DivId1').show();


  });
});