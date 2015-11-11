// JavaScript Document
$(document).ready(function(){
	$("[data-toggle='tooltip']").tooltip();
	$('.share-with span').click(function(){
		$(this).parent().find( ".custom-checkbox").slideToggle( "fast" );
	})
	if($('#profile-manager').length){
		$("#profile-manager").slicknav({
			prependTo:'#profile-manager-container'
			});
	}
});