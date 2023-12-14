const words = [
  "Привет",
  "Как",
  "бб",
  "что",
  "делаешь",
  "Такие",
  "дела",
  "Отлично",
  "Хорошо",
  "Сплю",
  "Ем",
  "Не",
  "мешай",
  "Прикольно",
  "Добрый",
  "Обед",
  "Вечер",
  "утро",
  "Салам",
  "Благодарствую",
  "Круто",
  "Яблоко",
  "Лук",
  "Морковь",
  "пью",
  "Занимаюсь",
  "Занят",
  "На",
  "работе",
  "Учусь",
  "Кайфую",
];

words.sort();

const input = document.getElementById("input");
const suggestion = document.getElementById("suggestion");
let currentSuggestions = []; // Массив для хр анения текущих подсказок

window.onload = () => {
  input.value = "";
  clearSuggestions();
};

const clearSuggestions = () => {
  suggestion.innerHTML = "";
  currentSuggestions = []; // Очищаем массив текущих подсказок при очистке
};

const caseCheck = (input) => {
  input = input.toLowerCase();
  let word = input.split("");
  return word.join("");
};

input.addEventListener("input", (e) => {
  const inputValues = input.value.trim().split(" "); // Разделяем введенные слова по пробелам
  clearSuggestions();

  inputValues.forEach((inputValue) => {
    if (inputValue !== "") {
      const wordsMatchingInput = words.filter((word) =>
        word.toLowerCase().startsWith(inputValue.toLowerCase())
      );

      if (wordsMatchingInput.length > 0) {
        currentSuggestions.push(wordsMatchingInput); // Добавляем все совпадающие слова в массив подсказок
      }
    }
  });

  if (currentSuggestions.length > 0) {
    const combinedSuggestions = currentSuggestions.flat().join(', '); // Объединяем все подсказки в одну строку
    suggestion.innerHTML = caseCheck(combinedSuggestions); // Отображаем текущие подсказки
  }
});

input.addEventListener("keydown", function handleTabKey(e) {
  if (e.keyCode === 9) {
    if (currentSuggestions.length > 0) {
      e.preventDefault();
      input.value = caseCheck(currentSuggestions[0][0]);
      clearSuggestions();
    }
  }
});