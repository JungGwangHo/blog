$(function(){
	// var a = $("#username").closest("p");
	// var duplBtn = document.createElement("button");
	// duplBtn.innerHTML="중복확인";
	// a.append(duplBtn);

	var flag = false;
	// $("p").on("click","button",function(){
	$("#duplcheck").on("click",function(){
		$.ajax({
			url: "/duplcheck",
    	type: 'POST',
    	data: {
						"csrfmiddlewaretoken": jQuery("[name=csrfmiddlewaretoken]").val(),
        		'username': $("#username").val()
    	},
			dataType: 'json',
    	success: function (data) {
        	// TODO: do something.
					if (data.is_taken) {
            alert("이미 존재하는 ID입니다.");
          }
					else{
						alert("사용하실 수 있는 ID입니다.");
						flag = true;
					}
    	},
    	error: function (request, status, error) {
        	// console.log(err);
					alert("code: " + request.status + "\n" + "error:" + error);
    	}
		});
		return false;
	});
	$("#username").on("focusout",function(){
		if(flag){
			flag=false;
		}
	});
	// $("#signup").on("submit",function(event){
	// 	event.preventdefault();
	// 	alert("gg");
	// });
	$('#signup').on('submit',function(e){
		if(!flag){
			e.preventDefault();
			alert("ID 중복확인 해주세요.");
		}
	});
});
