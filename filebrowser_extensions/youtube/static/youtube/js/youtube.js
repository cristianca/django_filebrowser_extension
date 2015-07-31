django.jQuery(document).ready(function(){
   django.jQuery('.youtube-hide').click(function(){
       // hide youtube search
       django.jQuery('.grp-youtube').addClass('grp-youtube-hide');
       django.jQuery('.youtube-hide').hide();
       django.jQuery('.youtube-show').show();
       django.jQuery('.grp-youtube-labels').hide();
       return false;
   });
   django.jQuery('.youtube-show').click(function(){
       // show youtube search
       django.jQuery('.grp-youtube').removeClass('grp-youtube-hide');
       django.jQuery('.youtube-hide').show();
       django.jQuery('.youtube-show').hide();
       django.jQuery('.grp-youtube-labels').show();
       return false;
   });

   django.jQuery('.youtube_movelink').click(function(){
       // click on button to move link need to send proper form
       var form_id = django.jQuery(this).attr('rel');
       django.jQuery('#' + form_id).submit();
       return false;
   })

});