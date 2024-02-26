"use strict";

const noteColors = document.querySelectorAll(".note-color-container > div");
const colorInput = document.querySelector("#note-color");
const createNoteModal = document.querySelector(".create-note-modal");
const createNoteBtn = document.querySelector(".create-note-btn");
const closeCreateNoteModal = document.querySelector(".close-create-note-modal");
const navAccount = document.querySelector(".nav-account");
const dropDownContainer = document.querySelector(".drop-down-container");
const dropDownIcon = document.querySelector(".drop-down-icon");

for (let i = 0; i < noteColors.length; i++) {
  noteColors[i].addEventListener("click", () => {
    const selectedColor = document.querySelector(".selected-color");
    if (selectedColor != noteColors[i]) {
      selectedColor.classList.remove("selected-color");
      noteColors[i].classList.add("selected-color");
    }
    const color = noteColors[i].style.backgroundColor;
    console.log(color);
    colorInput.value = color;
  });
}

createNoteBtn.addEventListener("click", () => {
  createNoteModal.showModal();
});

closeCreateNoteModal.addEventListener("click", () => {
  createNoteModal.close();
});

navAccount.addEventListener("click", () => {
  dropDownContainer.classList.toggle("hide");
  dropDownIcon.classList.toggle("rotate");
});
