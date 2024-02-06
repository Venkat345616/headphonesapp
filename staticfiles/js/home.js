const productcontainers = [...document.querySelectorAll(".new")];

const nxtBtn = [...document.querySelectorAll(".right_arrow")];
const preBtn = [...document.querySelectorAll(".left_arrow")];

productcontainers.forEach((item, i) => {
  let containerDimensions = item.getBoundingClientRect();
  let containerWidth = containerDimensions.width;

  nxtBtn[i].addEventListener("click", () => {
    item.scrollLeft += 300;
  });

  preBtn[i].addEventListener("click", () => {
    item.scrollLeft -= 300;
  });
});

function changeImage(element, newImagePath) {
  element.src = newImagePath;
}

function restoreImage(element) {
  element.src = element.getAttribute("original-src");
}

document.addEventListener("DOMContentLoaded", function () {
  var productImages = document.querySelectorAll(".product-image");
  productImages.forEach(function (image) {
    image.setAttribute("original-src", image.src);
  });
});
