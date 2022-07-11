const stimageup = document.querySelector("#stimageup");
stimageup.addEventListener("change", function () {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploaded_image = reader.result;
    document.querySelector("#display_image1").style.backgroundImage = url($, {
      uploaded_image,
    });
  });
  reader.readAsDataURL(this.files[0]);
});
const fimageup = document.querySelector("#fimageup");
fimageup.addEventListener("change", function () {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploaded_image = reader.result;
    document.querySelector("#display_image2").style.backgroundImage = url($, {
      uploaded_image,
    });
  });
  reader.readAsDataURL(this.files[0]);
});
