var modal = document.getElementById("modal");
var closeModalBtn = document.getElementById("btnClose");
var predictBtn = document.getElementById("btnPredict");

// event listeners
closeModalBtn.addEventListener("click", closeModal);
predictBtn.addEventListener("click", showModal);

// function to show modal and also trigger the prediction algorithm
function showModal(e) {
  e.preventDefault();
  modal.style.display = "flex";
}

// function to close the modal
function closeModal() {
  modal.style.display = "none";
}
