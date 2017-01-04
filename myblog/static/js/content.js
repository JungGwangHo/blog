$(function(){
	$("#id_content").hide();
	$("#id_textonly").hide();

	$("#frm").on("submit",function(event){
		var a = $("#id_fields_iframe").contents().find(".note-editable.panel-body");

		$("#id_content").val(a.html());	//id_content에 태그포함한 내용 저장

		var b = a.children("p");
		var txt = "aa";
		b.each(function(){
			txt+=$(this).text();
			txt+="\n";
		});
		$("#id_textonly").val(txt);		//id_content에 글만 저장
	});
});
