// const button = document.querySelector(".toggle");
const modalBttn = document.getElementById("htmlbtn1");
const modalBttn2 = document.getElementById("htmlbtn2")
const modalCancel = document.getElementById("copybtn2");
const modal = document.getElementById("modal");
const fontss = document.getElementById("left");

const getToggle = document.getElementById("toggle");

getToggle.addEventListener("click", () => {
  document.documentElement.classList.toggle("dark-theme");
});

// button.addEventListener("click", () => {
//   document.documentElement.classList.toggle("dark-theme");
// });

// Text html code Modal
modalBttn.addEventListener("click", () => {
  modal.style.display = "flex";
});

// Done button for text and icon modals
copybtn2.addEventListener("click", () => {
  modal.style.display = "none";
});

const copyToClipboard = () => {
  const getData = document.getElementById("htmlCode").innerHTML;
  navigator.clipboard.writeText(getData);
  alert("copied successfully");
};

// const copyToClipboards = () => {
//   const getCode = document.getElementById("htmlCodeImage").innerHTML;
//   navigator.clipboard.writeText(getCode);
//   alert("copied successfully");
// };


// html button 2

modalBttn2.addEventListener("click", () => {
  modal.style.display = "flex";
});

// ========================

// Handling Font family

// ========================

fetch(
  "https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyAyV-a0nP6SPoK30PmdMou92_CRz_qBSQs"
)
  .then(function (response) {
    // The API call was successful!
    return response.json();
  })
  .then(function (data) {
    data.items.forEach((el) => {
      fontss.innerHTML += `<option value="Robato" id="fontss">${el.family}</option>`;
    });
  })
  .catch(function (err) {
    // There was an error
    console.warn("Something went wrong.", err);
  });

// ========================

// menu

// ========================

const show = () => {
  document.getElementById("sidebar").style.right = "0";
};
const vanish = () => {
  document.getElementById("sidebar").style.right = "-100%";
};
