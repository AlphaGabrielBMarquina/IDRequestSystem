$(function(){
    $("input[name='optradio']").click(function(){
    if($("#stodent").is(":checked")){
    $("#fname").removeAttr("disabled");
    $("#fname").focus();
    $("#mname").removeAttr("disabled");
    
    $("#sname").removeAttr("disabled");
    
    $("#course").removeAttr("disabled");
    
    $("#deytrq").removeAttr("disabled");
    
    $("#imageup").removeAttr("disabled");
    
    $("#contactper").removeAttr("disabled");
    
    $("#contactno").removeAttr("disabled");
    
    $("#address").removeAttr("disabled");
    
    $("#studentno").removeAttr("disabled");
    
    $("#signature").removeAttr("disabled");
    

    $("#ffname").attr("disabled", "disabled");
    $("#faculfmname").attr("disabled", "disabled");
    $("#fsname").attr("disabled", "disabled");
    $("#femployeeno").attr("disabled", "disabled");
    $("#fdrequest").attr("disabled", "disabled");
    $("#fimageup").attr("disabled", "disabled");
    $("#fgsis").attr("disabled", "disabled");
    $("#fgsispol").attr("disabled", "disabled");
    $("#ftin").attr("disabled", "disabled");
    $("#flovelife").attr("disabled", "disabled");
    $("#fphealth").attr("disabled", "disabled");
    $("#fothers").attr("disabled", "disabled");
    $("#fcontactper").attr("disabled", "disabled");
    $("#fcontactno").attr("disabled", "disabled");
    $("#faddress").attr("disabled", "disabled");
    $("#fsignature").attr("disabled", "disabled");
    

    }
    else
    {
    $("#fname").attr("disabled", "disabled");
    $("#mname").attr("disabled", "disabled");
    $("#sname").attr("disabled", "disabled");
    $("#course").attr("disabled", "disabled");
    $("#deytrq").attr("disabled", "disabled");
    $("#imageup").attr("disabled", "disabled");
    $("#contactper").attr("disabled", "disabled");
    $("#contactno").attr("disabled", "disabled");
    $("#address").attr("disabled", "disabled");
    $("#studentno").attr("disabled", "disabled");
    $("#signature").attr("disabled", "disabled");


    $("#ffname").removeAttr("disabled");
    $("#ffname").focus();
    $("#faculfmname").removeAttr("disabled");
    
    $("#fsname").removeAttr("disabled");
    
    $("#femployeeno").removeAttr("disabled");
    
    $("#fdrequest").removeAttr("disabled");
    
    $("#fimageup").removeAttr("disabled");
    
    $("#fgsis").removeAttr("disabled");
    
    $("#fgsispol").removeAttr("disabled");
    
    $("#ftin").removeAttr("disabled");
    
    $("#flovelife").removeAttr("disabled");
    
    $("#fphealth").removeAttr("disabled");
    
    $("#fothers").removeAttr("disabled");
    
    $("#fcontactper").removeAttr("disabled");
    
    $("#fcontactno").removeAttr("disabled");
    
    $("#faddress").removeAttr("disabled");
    
    $("#fsignature").removeAttr("disabled");
    

    }
    });
    });

const stimageup = document.querySelector("#stimageup");
stimageup.addEventListener("change", function() {
const reader = new FileReader();
reader.addEventListener("load", () => {
const uploaded_image = reader.result;
document.querySelector("#display_image1").style.backgroundImage = url(${uploaded_image});
});
reader.readAsDataURL(this.files[0]);
});
const fimageup = document.querySelector("#fimageup");
fimageup.addEventListener("change", function() {
const reader = new FileReader();
reader.addEventListener("load", () => {
const uploaded_image = reader.result;
document.querySelector("#display_image2").style.backgroundImage = url(${uploaded_image});
});
reader.readAsDataURL(this.files[0]);
});
function opt(x) {
   if (x==0) {
      document.getElementById('stcard').style.display='block';
      document.getElementById('fcard').style.display='none';
   }
   else {
      document.getElementById('fcard').style.display='block';
      document.getElementById('stcard').style.display='none';
      return;
   }
}