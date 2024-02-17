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


let nav_menus = document.querySelectorAll('.nav_menu');
let dropdowns = document.querySelectorAll('.dropdown');

document.addEventListener('click', (event) => {
 
  if (!isDescendant(nav_menus, event.target) && !isDescendant(dropdowns, event.target)) {
    
    dropdowns.forEach((dropdown) => {
      dropdown.style.clipPath = 'polygon(100% 0, 100% 0, 100% 100%, 100% 100%)';
    });
  }
});

nav_menus.forEach((nav_menu, index) => {
  nav_menu.addEventListener('click', () => {
    
    dropdowns.forEach((dropdown) => {
      dropdown.style.clipPath = 'polygon(100% 0, 100% 0, 100% 100%, 100% 100%)';
    });

   
    dropdowns[index].style.clipPath = ' polygon(100% 0, 0 0, 0 100%, 99% 100%)';
  });
});


function isDescendant(nodeList, target) {
  for (let i = 0; i < nodeList.length; i++) {
    if (nodeList[i].contains(target)) {
      return true;
    }
  }
  return false;
}


