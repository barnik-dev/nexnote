const noteColors = document.querySelectorAll(".note-color-container > div");
const colorInput = document.querySelector("#note-color");

for (let i = 0; i < noteColors.length; i++) {
  noteColors[i].addEventListener("click", () => {
    const selectedColor = document.querySelector(".selected-color");
    if (selectedColor != noteColors[i]) {
      selectedColor.classList.remove("selected-color");
      noteColors[i].classList.add("selected-color");
    }
    const color = noteColors[i].style.backgroundColor;
    colorInput.value = color;
  });
}
