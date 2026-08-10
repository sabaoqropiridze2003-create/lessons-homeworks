const button = document.getElementById('button');
const course = document.getElementById('course');
const student = document.getElementById('student');

let isOriginal = true;

button.addEventListener('click', function () {
  if (isOriginal) {
    course.innerText = 'javascript';
    student.innerText = 'davit';
  } else {
    course.innerText = 'Python';
    student.innerText = 'otar';
  }
  isOriginal = !isOriginal; // Switches the toggle state
});