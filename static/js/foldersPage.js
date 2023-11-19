"use strict";

const navAccount = document.querySelector(".nav-account");
const dropDownContainer = document.querySelector(".drop-down-container");
const dropDownIcon = document.querySelector(".drop-down-icon");
const closeModal = document.querySelector(".close-modal");
const createFolderModal = document.querySelector(".create-folder-modal");
const createFolderBtn = document.querySelector(".create-folder-btn");

navAccount.addEventListener("click", () => {
  dropDownContainer.classList.toggle("hide");
  dropDownIcon.classList.toggle("rotate");
});

closeModal.addEventListener("click", () => {
  createFolderModal.close();
});

createFolderBtn.addEventListener("click", () => {
  createFolderModal.showModal();
});
