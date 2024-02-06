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
  // Check if the click is outside of any nav_menu or dropdown
  if (!isDescendant(nav_menus, event.target) && !isDescendant(dropdowns, event.target)) {
    // Hide all dropdowns
    dropdowns.forEach((dropdown) => {
      dropdown.style.clipPath = 'polygon(100% 0, 100% 0, 100% 100%, 100% 100%)';
    });
  }
});

nav_menus.forEach((nav_menu, index) => {
  nav_menu.addEventListener('click', () => {
    // Hide all dropdowns
    dropdowns.forEach((dropdown) => {
      dropdown.style.clipPath = 'polygon(100% 0, 100% 0, 100% 100%, 100% 100%)';
    });

    // Show the clicked dropdown
    dropdowns[index].style.clipPath = ' polygon(100% 0, 0 0, 0 100%, 99% 100%)';
  });
});

// Function to check if an element is a descendant of any element in a NodeList
function isDescendant(nodeList, target) {
  for (let i = 0; i < nodeList.length; i++) {
    if (nodeList[i].contains(target)) {
      return true;
    }
  }
  return false;
}


