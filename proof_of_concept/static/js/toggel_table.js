//  let button = document.getElementById("submit_button")
//  button.onclick = function (){

//     let x = document.getElementById("output");
//     x.style.display= "block";
// }

    function toggle_visibility(id) {
       let e = document.getElementById(id);
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
    }

