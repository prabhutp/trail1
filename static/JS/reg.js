AOS.init({
    duration: 2000,
  })

  var conf = document.querySelectorAll(".fa-2x");
 
  for(let i=0;i<conf.length;i++)
  {
    conf[i].classList.add('c'+i);
   //  conf[i].classList.remove('fa-2x');
   //  conf[i].classList.add('fa-3x')
  }
  //top-nav
  function myFunction() {
   var x = document.getElementById("myTopnav");
   if (x.className === "topnav") {
     x.className += " responsive";
   } else {
     x.className = "topnav";
   }
 }


//   function ismatch(str){
//     var ret = null;
//     var tab = ['data-aos_', 'data-aos-delay_', 'data-aos-duration_', 'data-aos-easing_'];
//     Object.values(tab).forEach( function (value) {
//         if (String(str).match(value)){
//             ret = str.split('_');
//             return false;
//         }
//     });
//     return ret;
// }
// jQuery(document).ready(function ($) {
//     $('.some-class').each(function () {
//         var $this = $(this);
//         var tab = $this.attr('class').split(' ');
//         var keep;
//         Object.values(tab).forEach(function (item) {
//             var ello = ismatch(item) 
//             if (ello !== null)
//                 $this.attr(ello[0], ello[1]);
//             });
            
//         });
//         AOS.init({
//           duration: 3000
//         });
//     });              

  // particlesJS("particles-js", {"particles":{"number":{"value":260,
  // "density":{"enable":true,"value_area":800}},"color":{"value":"#ffffff"},
  // "shape":{"type":"circle","stroke":{"width":0,"color":"#000000"},
  // "polygon":{"nb_sides":5},"image":{"src":"img/github.svg","width":100,
  // "height":100}},"opacity":{"value":1,"random":true,"anim":{"enable":true,
  // "speed":1,"opacity_min":0,"sync":false}},"size":{"value":3,"random":true,
  // "anim":{"enable":false,"speed":4,"size_min":0.3,"sync":false}},
  // "line_linked":{"enable":false,"distance":150,"color":"#ffffff",
  // "opacity":0.4,"width":1},"move":{"enable":true,"speed":1,"direction":"none",
  // "random":true,"straight":false,"out_mode":"out","bounce":false,
  // "attract":{"enable":false,"rotateX":600,"rotateY":600}}},
  // "interactivity":{"detect_on":"canvas","events":{"onhover":
  // {"enable":true,"mode":"bubble"},"onclick":{"enable":true,"mode":"repulse"},
  // "resize":true},"modes":{"grab":{"distance":400,"line_linked":{"opacity":1}},
  // "bubble":{"distance":250,"size":0,"duration":2,"opacity":0,"speed":3},
  // "repulse":{"distance":400,"duration":0.4},"push":{"particles_nb":4},
  // "remove":{"particles_nb":2}}},"retina_detect":true})

  $("#tproceed").on("click", function(e) {
      var memberinfo = document.querySelectorAll("#memberinfo");

      for (let index = 0; index < memberinfo.length; index++) {
        if(!(memberinfo[index].classList.contains("card-hidden")))
        {
          memberinfo[index].classList.add("card-hidden");
        }
      }


    // if ($(".card-hidden").length >$("#teamsize")) {
    //    $(".card-hidden").first().slideToggle(function() {
    //      $(this).removeClass("card-hidden");
    //    });
    // } else {
    // //   console.log("No more cards to show.");
    var hid = document.getElementsByClassName("card-hidden").length;
    var t = document.getElementById("teamsize").value;
    console.log(t,hid);
    // $(".temdet").addClass("card-hidden");
    for (let index = 0; index < t; index++) {
      
      $(".card-hidden").first().removeClass("card-hidden");
      // $(".memberdet").first().classList.add("anim");
      // $(".memberdet").first().removeClass("memberdet");
      
      // $(".memberdet").first().animate({left: '500px'});
        console.log(index);
      };
      setTimeout(function() {
      $(".sub-hidden").first().removeClass("sub-hidden");
    }, 1500);
    }
   );


