var form = $('form[name=post_episode]');
$('form').submit(function() {
  setTimeout( function() {
		form.off( 'submit' );
		form.submit();
	}, 2500);
  return false
});

  $(".send").on('click', function(){
    $(".text").addClass("active");
    $(".send").addClass("active");
    $(".loader").addClass("active");
    $(".send").delay(1700).queue(function(){
          $(this).addClass("finished").clearQueue();
      });
    if($('.input_episode').val().length>=5){
      $(".done").delay(1600).queue(function(){
        $(this).addClass("active").clearQueue();
      });
    }
    else{
      $(".failed").delay(1600).queue(function(){
        $(this).addClass("active").clearQueue();
      });
    }
  })

  $('.thank_you_input').on('click', function() {
    let $btn = $(this);
    $btn.addClass('on');
    $btn.addClass("HeartAnimation");
    setTimeout( function() {
      $btn.removeClass('on');
      $btn.removeClass("HeartAnimation");
      $btn.css("background-position","left");
    }, 800);
    $('.thank_you_input').prop("disable",true)
  });