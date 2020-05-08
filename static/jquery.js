// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

document.addEventListener('click', function(e) {
	if (document.activeElement.toString() == '[object HTMLButtonElement]') {
		document.activeElement.blur();
		}
	});



$(document).ready(function(){
	console.log("script running")    
	
	

	
    var $myForm = $('.my-ajax-form')
    $myForm.submit(function(event){
        event.preventDefault()
        var $formData = $(this).serialize()
        var $thisURL = $myForm.attr('data-url') || window.location.href // or set your own url
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })
    })





    function handleFormSuccess(data, textStatus, jqXHR){
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR)
        //$myForm.reset(); // reset form data
    }

    function handleFormError(jqXHR, textStatus, errorThrown){
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)
    }

//Fire Button
	$(document).on("click", "#fire-btn", function () {
		var data = {"firing": "yes_please"}
		$.ajax({
			type:				'POST',
			url: 				'fire/',
			data:			data
		});    	
    });


//Single colour preset buttons
	$(document).on("click", "#1-col-preset-btn-1", function () {
		var data = {"preset": 'sgl_col_1'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#1-col-preset-btn-2", function () {
		var data = {"preset": 'sgl_col_2'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });        
    
	$(document).on("click", "#1-col-preset-btn-3", function () {
		var data = {"preset": 'sgl_col_3'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });
    
	$(document).on("click", "#1-col-preset-btn-4", function () {
		var data = {"preset": 'sgl_col_4'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#1-col-preset-btn-5", function () {
		var data = {"preset": 'sgl_col_5'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#1-col-preset-btn-6", function () {
		var data = {"preset": 'sgl_col_6'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });        
    
	$(document).on("click", "#1-col-preset-btn-7", function () {
		var data = {"preset": 'sgl_col_7'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });
    
	$(document).on("click", "#1-col-preset-btn-8", function () {
		var data = {"preset": 'sgl_col_8'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });  
    
 
// Two-colour preset buttons   
	$(document).on("click", "#2-col-preset-btn-1", function () {
		var data = {"preset": 'dbl_col_1'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#2-col-preset-btn-2", function () {
		var data = {"preset": 'dbl_col_2'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });        
    
	$(document).on("click", "#2-col-preset-btn-3", function () {
		var data = {"preset": 'dbl_col_3'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });
    
	$(document).on("click", "#2-col-preset-btn-4", function () {
		var data = {"preset": 'dbl_col_4'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#2-col-preset-btn-5", function () {
		var data = {"preset": 'dbl_col_5'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#2-col-preset-btn-6", function () {
		var data = {"preset": 'dbl_col_6'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });        
    
	$(document).on("click", "#2-col-preset-btn-7", function () {
		var data = {"preset": 'dbl_col_7'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });
    
	$(document).on("click", "#2-col-preset-btn-8", function () {
		var data = {"preset": 'dbl_col_8'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });      
    
    
//Dynamic preset buttons
	$(document).on("click", "#dyn-preset-btn-1", function () {
		var data = {"preset": 'dyn_1'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#dyn-preset-btn-2", function () {
		var data = {"preset": 'dyn_2'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });        
    
	$(document).on("click", "#dyn-preset-btn-3", function () {
		var data = {"preset": 'dyn_3'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });
    
	$(document).on("click", "#dyn-preset-btn-4", function () {
		var data = {"preset": 'dyn_4'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#dyn-preset-btn-5", function () {
		var data = {"preset": 'dyn_5'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });

	$(document).on("click", "#dyn-preset-btn-6", function () {
		var data = {"preset": 'dyn_6'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });        
    
	$(document).on("click", "#dyn-preset-btn-7", function () {
		var data = {"preset": 'dyn_7'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });
    
	$(document).on("click", "#dyn-preset-btn-8", function () {
		var data = {"preset": 'dyn_8'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });          
    
    	$(document).on("click", "#dyn-preset-btn-9", function () {
		var data = {"preset": 'dyn_9'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });  

    	$(document).on("click", "#dyn-preset-btn-10", function () {
		var data = {"preset": 'dyn_10'}
		$.ajax({
			type:				'POST',
			url: 				'preset/',
			data:			data
		});    	
    });  
})